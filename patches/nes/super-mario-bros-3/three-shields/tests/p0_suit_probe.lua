-- PRG0/PRG1 bounded P0 suit-collision probe.
-- A Mesen-native per-revision checkpoint is restored. Writes only fixture RAM.
-- Seeded suit byte is not proof of acquiring suit through actual item pickup.
local output=assert(os.getenv("NES_TEST_OUT"),"NES_TEST_OUT missing")
local checkpoint=assert(os.getenv("NES_TEST_FIXTURE"),"NES_TEST_FIXTURE missing")
local suit=assert(tonumber(os.getenv("NES_TEST_SUIT")),"NES_TEST_SUIT missing")
local f=assert(io.open(output.."\\events.tsv","w"))
f:write("frame\tevent\tpc\tscene\thp\tsig\tsuit\tqueue\tgrow\tlost\tinv\tlives\tstar\n")
local frame=0
local restored=false
local seeded=false
local cpu=emu.cpuType.nes
local mem=emu.memType.nesMemory
local count={hurt=0,hook=0,die=0,native=0}
local function rd(a)return emu.read(a,mem,false)end
local function wr(a,v)emu.write(a,v,mem)end
local function log(ev)
 local s=emu.getCpuState(cpu)
 f:write(frame,"\t",ev,"\t",string.format("%04X",s.pc or 0),"\t",
 rd(0x729),"\t",rd(0x7FCE),"\t",rd(0x7FCF),"\t",rd(0xED),"\t",
 rd(0x578),"\t",rd(0x551),"\t",rd(0x554),"\t",rd(0x552),"\t",
 rd(0x736),"\t",rd(0x553),"\n")
 f:flush()
end
emu.addMemoryCallback(function()
 if not restored and frame>=45 then
  restored=true
  local h=assert(io.open(checkpoint,"rb"));local b=h:read("*a");h:close()
  local ok,e=pcall(emu.loadSavestate,b)
  log(ok and "RESTORE_OK" or ("RESTORE_FAIL_"..tostring(e)))
 end
end,emu.callbackType.exec,0x8000,0xFFFF,cpu,mem)
for _,x in ipairs({
 {0xD9D3,"hurt","NATIVE_HURT"},
 {0xD9EC,"hook","HP_HOOK"},
 {0xDA15,"native","NATIVE_SUIT_PATH"},
 {0xDA4E,"native","NATIVE_SMALL_BIG"},
 {0xDA7C,"die","NATIVE_DIE"}}) do
 local pc,key,ev=x[1],x[2],x[3]
 emu.addMemoryCallback(function()
  count[key]=count[key]+1
  if count[key]<=8 then log(ev)end
 end,emu.callbackType.exec,pc,pc,cpu,mem)
end
emu.addEventCallback(function()emu.setInput({},0,0)end,emu.eventType.inputPolled)
emu.addEventCallback(function()
 frame=frame+1
 if restored and frame==65 and not seeded then
  seeded=true
  wr(0xED,suit)
  wr(0x7FCE,3)
  wr(0x7FCF,0xA5)
  wr(0x552,0)
  log("SEEDED_SUIT_BYTE_ONLY")
 end
 if frame==95 or frame==150 or frame==205 or frame==230 or frame==245 or frame==265 or frame==320 or frame==410 then
  log("SAMPLE")
 end
 if frame==245 or frame==320 then
  local h=assert(io.open(output..string.format("\\frame_%04d.png",frame),"wb"))
  h:write(emu.takeScreenshot());h:close()
 end
 if frame>=420 then
  log("END")
  f:write("#COUNTS\t",count.hurt,"\t",count.hook,"\t",count.die,"\t",count.native,"\n")
  f:close()
  emu.stop(0)
 end
end,emu.eventType.endFrame)
