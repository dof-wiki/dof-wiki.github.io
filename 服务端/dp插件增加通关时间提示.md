# dp插件增加通关时间提示

用补丁大合集或者其他内辅跳过翻牌的话会看不到通关时间，可以通过dp插件来增加通关时间的提示，不过副本时长和地图时长的两个函数get不到正确数值（也许是姿势不对），所以改用系统时间差和来计算。该方法计算的通关时间是点击进入副本到击杀boss的实际时间，而游戏系统内的通关时间貌似是不计算加载副本以及过图的短暂加载时间，因此该方法获取的通关时间会比游戏系统计算的大。


```lua
---@type DP
local dp = _DP
---@type DPXGame
local dpx = _DPX


local game = require("df.game")
local logger = require("df.logger")


local luv = require("luv")
local world = require("df.game.mgr.world")


logger.info("opt: %s", dpx.opt())


-- see dp2/lua/df/doc for document !


local item_handler = { }


player_01 = 0


local function playerlogin(_user)
    player_01 = game.fac.user(_user)
    player_01:SendNotiPacketMessage(string.format("dp插件已开启功能 ： [地下城通关时间提示]"))
end

dpx.hook(game.HookType.Reach_GameWord, playerlogin)


local function EndDungeonTime(fnext, type, _party, param)
    if type == game.GameEventType.PARTY_DUNGEON_START then
        Joinmaptime = dp.mstime()
        player_01:SendNotiPacketMessage(string.format("进入地下城······"))
    end
    if type == game.GameEventType.PARTY_DUNGEON_CLEAR then
        local Clearmaptimemms = 0
        local party = game.fac.party(_party)
        local dungeon = party:GetDungeon()
        local dungeonname = dungeon:GetName()
        local Endmaptime = dp.mstime()
        local Clearmaptime = Endmaptime - Joinmaptime
        local Clearmaptimemin = math.modf(Clearmaptime/1000/60)
        local Clearmaptimes = math.modf(Clearmaptime/1000)
        for i = 1,Clearmaptimemin do
            if Clearmaptimes >= 60 then
                Clearmaptimes = Clearmaptimes - 60
            end
        end
        local Clearmaptimemmsf = Clearmaptime/1000
        while Clearmaptimemmsf >= 1 do
            Clearmaptimemmsf = Clearmaptimemmsf -1
        end
        if Clearmaptimemmsf < 1 then
            Clearmaptimemms = math.modf(Clearmaptimemmsf*100)
        end
        logger.info("通关副本: %s,通关时长: %d", dungeonname,Clearmaptime)
        player_01:SendNotiPacketMessage(string.format(" [%s]地下城通关时长 : %d分%d秒%d", dungeonname,Clearmaptimemin,Clearmaptimes,Clearmaptimemms))
    end
    return fnext()
end
dpx.hook(game.HookType.GameEvent, EndDungeonTime)
```