# hook点

### 掉落判定次数
默认普通怪物1次，深渊怪物6/8
```js
// ["0x08537070"] = "_ZN8WongWork12CMonsterDrop20generateSpecificItemERKNS_19stGenerateRefData_tERNS_18stGenerateResult_tE",
Interceptor.attach(ptr(0x08537070), {
    onEnter(args) {
        const dropcount = args[1].add(61).readU8() // 掉落次数
        args[1].add(61).writeU8(dropcount * 10) // 回写
    }
})
```

### 怪物普通掉落率
```js
// ["0x08535ed2"] = "_ZN8WongWork12CMonsterDrop19_generateRandomItemEhchhhiiRNS_18stGenerateResult_tERb",
Interceptor.attach(ptr(0x08535ed2), {
    onEnter(args) {
        // 掉落率，数字越大越容易掉，默认100
        args[7] = ptr(65535)
    }
})
```

### 强化/增幅

```js
// ["0x0854755a"] = "_ZN8WongWork12CItemUpgrade14_DoProcUpgradeEP5CUserP10Inven_ItemPK14upgrade_info_t",
Interceptor.attach(ptr(0x0854755a), {
    onEnter(args) {
        const user = args[1]
        const equ = args[2]  // 被强化装备
        const randMax = args[0].add(315) // 随机数最大值, 默认 100000
        const rand = args[3].add(8)  // 成功率, 随机数大于这个值时就成功了, 设为0则必成
    }
})
```

### 进入地下城

```js
// ["0x085a0954"] = "_ZN6CParty13dungeon_startEic17ENUM_DUNGEON_TYPE",
const dgnId = args[1].toInt32()  // dgn id
if (dgnId === 1) {
    args[1] = ptr(2)
}
```


### 附魔

```js
// ["0x0849ed1a"] = "_ZN10expert_job13CExpertJobMgr15OnEnchantByBeadEP5CUseriiii",
const user = args[1]
const slot1 = args[3]  // 宝珠格子
const slot2 = args[5]  // 装备格子

const inven = CUserCharacInfo_getCurCharacInvenW(user)
const item = CInventory_GetInvenRef(inven, INVENTORY_TYPE_ITEM, slot1.toInt32())
const equ = CInventory_GetInvenRef(inven, INVENTORY_TYPE_ITEM, slot2.toInt32())
```

### 烟花类道具使用
```js
// ["0x08233f38"] = "_ZN30Dispatcher_UseSharedEffectItem7processEP5CUserR8MSG_BASER9ParamBase"
const user = args[1]
const item_id = user.add(285).readU32()
```

### 获得物品
捡起道具时的，可用来代替日志hook
```js
// ["0x085b949c"] = "_ZN6CParty10_onGetItemEP5CUserjj",
const user = args[1]
const itemId = args[2].toInt32()
const num = args[3].toInt32()  // 注意如果是装备，这个数量是错误的
```

### 复制物品
```js
// ["0x08671eb2"] = "_ZN5CUser14copyItemOptionER10Inven_ItemS1_",
CUser_CopyItemOption(user, ptr(equ1), ptr(equ2))  // 将 equ1 的属性复制到 equ2
```


### 合成卡片
```js
// ["0x081d88b0"] = "_ZN26Dispatcher_MonstercardBind7processEP5CUserR8MSG_BASER9ParamBase",
const user = args[1]
const data = args[2]
const bindSlot = data.add(13).readU8() // 合成器槽位
const card1Slot = data.add(15).readU8() // 卡片1槽位
const card2Slot = data.add(17).readU8() // 卡片2槽位
```