#!/usr/bin/env python3
"""SHA-gated, reversible SMB3 derived-ROM vault. No source ROMs are stored in vault.
Usage: python scripts/rom_delta_vault.py build|verify|restore NAME|status
Restore only creates absent targets. No delete operation in this tool.
"""
from pathlib import Path
import argparse, hashlib, importlib.util, json, os, tempfile, zlib, datetime
ROOT=Path(os.environ["SMB3_WORKSPACE_ROOT"]).resolve()
WORK=ROOT/"build/working"
VAULT=ROOT/"vault/derived_roms"
DELTA=VAULT/"deltas"
MANIFEST=VAULT/"manifest.json"
PRG1=Path(os.environ["SMB3_PRG1_SOURCE"]).resolve()
PRG0=Path(os.environ["SMB3_PRG0_SOURCE"]).resolve()
EXPECTED={"PRG1":"4377a7f5e6eb50bdd2ac6f249bf1a7085500aca8eb41f38545c3a2731c51a579",
          "PRG0":"6ea0777ca520ba7ad7b0ea0f6452140d59aa0b1dffe5045cb1e8020dde10c267"}
NAMES=(
"SMB3_NES_3HP_ALPHA.nes",
"SMB3_NES_3HP_HEAL_BETA.nes",
"SMB3_NES_SHIELDS_CLEAN_TILES_ALPHA.nes",
"SMB3_NES_SHIELDS_ONCHANGE_ALPHA.nes",
"SMB3_NES_SHIELDS_SUITFIX_ALPHA.nes",
"SMB3_NES_SHIELD_ALPHA.nes",
"SMB3_NES_SHIELD_RESET_BETA.nes")
def sha(data):return hashlib.sha256(data).hexdigest()
def stock():
 result={}
 for k,p in (("PRG0",PRG0),("PRG1",PRG1)):
  data=p.read_bytes()
  if sha(data)!=EXPECTED[k] or len(data)!=393232:raise RuntimeError("PRISTINE_BASE_MISMATCH "+k)
  result[k]=data
 return result
def encode(base,target):
 if len(base)!=len(target):raise ValueError("expected equal ROM sizes")
 i=0;out=bytearray(b"PATCH")
 while i<len(base):
  if base[i]==target[i]:i+=1;continue
  first=i
  while i<len(base) and base[i]!=target[i] and i-first<65535:i+=1
  block=target[first:i]
  out+=first.to_bytes(3,"big")+len(block).to_bytes(2,"big")+block
 return bytes(out+b"EOF")
def decode(base,ips):
 if not ips.startswith(b"PATCH"):raise ValueError("IPS HEADER")
 out=bytearray(base);p=5
 while True:
  if p+3>len(ips):raise ValueError("IPS TRUNCATED")
  offset_raw=ips[p:p+3];p+=3
  if offset_raw==b"EOF":break
  off=int.from_bytes(offset_raw,"big")
  if p+2>len(ips):raise ValueError("IPS LENGTH MISSING")
  n=int.from_bytes(ips[p:p+2],"big");p+=2
  if n==0:
   if p+3>len(ips):raise ValueError("IPS RLE TRUNCATED")
   size=int.from_bytes(ips[p:p+2],"big");p+=2
   block=ips[p:p+1]*size;p+=1
  else:
   if p+n>len(ips):raise ValueError("IPS DATA TRUNCATED")
   block=ips[p:p+n];p+=n
  if off+len(block)>len(out):raise ValueError("SIZE EXPANSION NOT EXPECTED")
  out[off:off+len(block)]=block
 if p!=len(ips):raise ValueError("IPS TRAILING DATA")
 return bytes(out)
def load_manifest():
 m=json.loads(MANIFEST.read_text(encoding="utf-8"))
 assert m["schema_version"]==1 and m["source_sha256"]==EXPECTED["PRG1"]
 assert len(m["targets"])==7
 return m
def verify_one(m,base,rec):
 p=DELTA/rec["delta_file"]
 compressed=p.read_bytes()
 if sha(compressed)!=rec["delta_sha256"]:raise RuntimeError("DELTA_HASH_MISMATCH "+rec["filename"])
 ips=zlib.decompress(compressed)
 if sha(ips)!=rec["ips_sha256"]:raise RuntimeError("IPS_HASH_MISMATCH "+rec["filename"])
 result=decode(base,ips)
 if len(result)!=rec["bytes"] or sha(result)!=rec["target_sha256"]:raise RuntimeError("REBUILD_HASH_MISMATCH "+rec["filename"])
 path=WORK/rec["filename"]
 if path.exists() and path.read_bytes()!=result:raise RuntimeError("EXISTING_TARGET_DRIFT "+rec["filename"])
 return result
def build():
 sources=stock();base=sources["PRG1"]
 VAULT.mkdir(parents=True,exist_ok=True);DELTA.mkdir(parents=True,exist_ok=True)
 if MANIFEST.exists():raise RuntimeError("VAULT_ALREADY_EXISTS; use verify instead")
 records=[]
 for filename in NAMES:
  path=WORK/filename;target=path.read_bytes()
  if len(target)!=len(base):raise RuntimeError("TARGET_SIZE "+filename)
  ips=encode(base,target)
  compressed=zlib.compress(ips,9)
  digest=sha(compressed)
  rec={"filename":filename,"revision":"PRG1","bytes":len(target),
       "target_sha256":sha(target),"ips_sha256":sha(ips),
       "delta_sha256":digest,"delta_file":digest+".ips.zlib",
       "compressed_bytes":len(compressed),"raw_ips_bytes":len(ips)}
  tmp=DELTA/(digest+".tmp")
  tmp.write_bytes(compressed)
  if decode(base,zlib.decompress(tmp.read_bytes()))!=target:raise RuntimeError("DELTA_ROUNDTRIP "+filename)
  os.replace(tmp,DELTA/rec["delta_file"])
  records.append(rec)
 manifest={"schema_version":1,"format":"zlib-compressed IPS","source_revision":"PRG1",
   "source_path":str(PRG1),"source_sha256":EXPECTED["PRG1"],
   "protected_pristine":{"PRG0":{"path":str(PRG0),"sha256":EXPECTED["PRG0"]},
                          "PRG1":{"path":str(PRG1),"sha256":EXPECTED["PRG1"]}},
   "created_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
   "retirement_state":"NOT_RETIRED_REQUIRE_DEPENDENCY_AND_REGRESSION_GATES",
   "targets":records}
 t=VAULT/"manifest.json.tmp";t.write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
 os.replace(t,MANIFEST)
 for rec in records:verify_one(manifest,base,rec)
 assert {k:sha(v) for k,v in stock().items()}==EXPECTED
 print(json.dumps({"status":"CREATED_VERIFIED","targets":len(records),
    "full_bytes":sum(x["bytes"] for x in records),"compressed_bytes":sum(x["compressed_bytes"] for x in records),
    "originals_removed":0},indent=2))
def verify():
 base=stock()["PRG1"];m=load_manifest()
 for rec in m["targets"]:verify_one(m,base,rec)
 print(json.dumps({"status":"VERIFIED","targets":len(m["targets"]),
  "existing_targets":sum((WORK/r["filename"]).exists() for r in m["targets"]),
  "retirement_state":m["retirement_state"]},indent=2))
def restore(name):
 if name not in NAMES:raise RuntimeError("UNKNOWN_NAME")
 base=stock()["PRG1"];m=load_manifest()
 rec=next(r for r in m["targets"] if r["filename"]==name)
 path=WORK/name
 if path.exists():
  if sha(path.read_bytes())==rec["target_sha256"]:
   print("ALREADY_PRESENT_VERIFIED "+str(path));return
  raise RuntimeError("REFUSING_TO_OVERWRITE_DRIFT")
 data=verify_one(m,base,rec)
 path.parent.mkdir(parents=True,exist_ok=True)
 with tempfile.NamedTemporaryFile(dir=path.parent,suffix=".part",delete=False) as t:
  t.write(data);temp=Path(t.name)
 if sha(temp.read_bytes())!=rec["target_sha256"]:raise RuntimeError("TEMP_HASH_MISMATCH")
 os.replace(temp,path)
 print("RESTORED "+str(path)+" SHA256 "+sha(path.read_bytes()))
def main():
 p=argparse.ArgumentParser()
 p.add_argument("operation",choices=["build","verify","restore","status"])
 p.add_argument("filename",nargs="?")
 a=p.parse_args()
 if a.operation=="build":build()
 elif a.operation=="verify":verify()
 elif a.operation=="restore":restore(a.filename)
 else:
  m=load_manifest()
  print(json.dumps({"targets":[{"name":x["filename"],"present":(WORK/x["filename"]).exists(),"delta":x["delta_file"]} for x in m["targets"]],
     "retirement_state":m["retirement_state"]},indent=2))
if __name__=="__main__":main()
