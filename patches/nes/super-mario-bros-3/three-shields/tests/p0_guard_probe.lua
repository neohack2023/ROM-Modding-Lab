local o=assert(os.getenv("NES_TEST_OUT"))
local checkpoint=assert(os.getenv("NES_TEST_FIXTURE"))
local guard=assert(os.getenv("NES_GUARD_MODE"))
local f=assert(io.open(o.."\\events.tsv","w"))
f:write("frame\tevent\thp\tsig\tsuit\tflash\tstar\tlives\tscene\n")
local frame=0;local restored=false;local cpu=emu.cpuType.nes;local mem=emu.memType.nesMemory
local function rd(a)return emu.read(a,mem,false)end
local function wr(a,b)emu.write(a,b,mem)end
local function log(ev)
 f:write(frame,"\t",ev,"\t",rd(0x7FCE),"\t",rd(0x7FCF),"\t",rd(0xED),"\t",rd(0x552),"\t",rd(0x553),"\t",rd(0x736),"\t",rd(0x729),"\n");f:flush()
end
emu.addMemoryCallback(function()
 if not restored and frame>=45 then
  restored=true
  local h=assert(io.open(checkpoint,"rb"));local s=h:read("*a");h:close()
  local ok,err=pcall(emu.loadSavestate,s);log(ok and "RESTORED" or "ERROR_RESTORE")
 end
end,emu.callbackType.exec,0x8000,0xFFFF,cpu,mem)
for _,t in ipairs({{0xD9D3,"NATIVE_HURT"},{0xD9EC,"HP_HOOK"},{0xDA7C,"NATIVE_DIE"}})do
 emu.addMemoryCallback(function()log(t[2])end,emu.callbackType.exec,t[1],t[1],cpu,mem)
end
emu.addEventCallback(function()emu.setInput({},0,0)end,emu.eventType.inputPolled)
emu.addEventCallback(function()
 frame=frame+1
 if restored and frame==170 then
  wr(0xED,0);wr(0x7FCE,3);wr(0x7FCF,0xA5)
  if guard=="star" then wr(0x553,100)end
  if guard=="flash" then wr(0x552,100)end
  log("SEED_GUARD_"..guard)
 end
 if frame==185 or frame==200 or frame==220 or frame==270 then log("SAMPLE")end
 if frame>=290 then log("END");f:close();emu.stop(0)end
end,emu.eventType.endFrame)
