-- Passive native SMB3 pipe-state recorder for PRG0 and PRG1 (MMC3).
-- Detects actual transitions; it never writes any pipe control variable.
local output=assert(os.getenv("NES_TEST_OUT"))
local fixture=assert(os.getenv("NES_TEST_FIXTURE"))
local auto=os.getenv("NES_PIPE_AUTOPLAY")=="1"
local f=assert(io.open(output.."\\events.tsv","w"))
f:write("frame\tevent\tmapop\tpipe\tinpipe\tjct\thp\tsig\txlow\txhigh\ty\tsuit\tlives\n")
local frame=0;local restored=false;local cpu=emu.cpuType.nes;local mem=emu.memType.nesMemory
local function rd(a)return emu.read(a,mem,false)end
local function log(s)
 f:write(frame,"\t",s,"\t",rd(0x729),"\t",rd(0x571),"\t",rd(0x58C),"\t",rd(0x3DE),"\t",rd(0x7FCE),"\t",rd(0x7FCF),"\t",rd(0x90),"\t",rd(0x75),"\t",rd(0xA2),"\t",rd(0xED),"\t",rd(0x736),"\n");f:flush()
end
emu.addMemoryCallback(function()
 if not restored and frame>=45 then
  restored=true
  local h=assert(io.open(fixture,"rb"));local s=h:read("*a");h:close()
  local ok,e=pcall(emu.loadSavestate,s)
  log(ok and "RESTORE_OK" or "RESTORE_FAIL")
 end
end,emu.callbackType.exec,0x8000,0xFFFF,cpu,mem)
for _,spec in ipairs({{0x571,"PIPE_MOVE_WRITE"},{0x58C,"PLAYER_IN_PIPE_WRITE"},{0x3DE,"JCT_WRITE"}}) do
 local addr,kind=spec[1],spec[2]
 emu.addMemoryCallback(function(a,v)
  if restored and v~=rd(addr) then log(kind.."_NEW_"..tostring(v))end
 end,emu.callbackType.write,addr,addr,cpu,mem)
end
local lastpipe=-1;local lastin=-1;local lastop=-1
if auto then
 emu.addEventCallback(function()
  local b={a=false,b=false,select=false,start=false,up=false,down=false,left=false,right=false}
  if restored then
   b.right=frame<740
   b.b=frame<740
   b.a=(frame%110>=15 and frame%110<37)
   b.down=(frame%190>=154 and frame%190<183)
  end
  emu.setInput(b,0,0)
 end,emu.eventType.inputPolled)
end
emu.addEventCallback(function()
 frame=frame+1
 if restored then
  local p=rd(0x571);local i=rd(0x58C);local o=rd(0x729)
  if p~=lastpipe or i~=lastin or o~=lastop then log("TRANSITION_STATE");lastpipe=p;lastin=i;lastop=o end
  if frame%60==0 then log("SAMPLE")end
 end
 if frame==205 or frame==405 or frame==605 then
  local h=assert(io.open(output..string.format("\\frame_%04d.png",frame),"wb"));h:write(emu.takeScreenshot());h:close()
 end
 if frame>=805 then log("END");f:close();emu.stop(0)end
end,emu.eventType.endFrame)
