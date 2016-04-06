# mgsmonsterguns

How does an MGSV weapon work?
Every customizable weapon consists of parts (using URAGAN-5P SLUG as example):

    id | localized string | description
    ---|------------------|-------------
    TppEquip.WP_10515|weapon id| self-explanatory
    TppEquip.RC_10515|URAGAN SG-FRAME| frame with open slots, usually one per gun
    ---|---|---
    Parts which are added to the frame|
    TppEquip.BA_10504|URAGAN-5P L-BARREL| gun barrel, duh
    TppEquip.AM_10515|12GA SHELL (SLUG)| ammo type
    TppEquip.SK_None|-| stock
    TppEquip.MZ_None|-| muzzle
    TppEquip.MO_None|-| muzzle option
    TppEquip.ST_20104|DOT SIGHT I|Scope (Upper Option Slot)
    TppEquip.ST_None|-| Second scope slot
    TppEquip.UD_None|-| Underbarrel slot ?
    TppEquip.LT_10102|COMPACT F-LIGHT| Underbarrel slot (flashlights)
    TppEquip.LT_None|-| Side slot


These predefined parameters for each gun can be found in file `\master\0\00\Assets\tpp\level_asset\weapon\ParameterTables\parts\EquipParameters.lua` and vary from gun to gun (TppEquip.UD_None can be substituted by UB_None for example); color is not included. 
Note that some parameters are None by default - it means that frame used in this weapon doesn't allow changes in these slots.

If your gun's frame has litte to none open slots (marked red ingame), you can try to change the frame to another one with more options. However it may crash the game or hang it.

#Open slots

Let's say we want to change options for open slots such as scope. There are two ways of doing so:
* Changing it in `\master\0\00\Assets\tpp\level_asset\weapon\ParameterTables\parts\EquipParameters.lua` to another one. 
	* Pros: you will change every gun in the game including those that guards carry. 
	* Cons: small variety, you cannot select between other scopes
* Adding more entries to `\master\0\00\Assets\tpp\motherbase\script\WeaponPartsCombinationSettings.lua`, expanding the list.
	* Pros: a lot of options
	* Cons: none

##Replacing options
First method talks for itself: find a part you want on a gun, replace it (ie ST_20104 for ST_30305), save file, make a new customized gun.

##Adding more entries
Open `\master\0\00\Assets\tpp\motherbase\script\WeaponPartsCombinationSettings.lua`, find a frame for your gun - `RC_10515` for URAGAN-SG. There will be multiplie entries such as 
```
TppMotherBaseManagement.RegistPartsInclusionInfo{
	receiverID=
		{TppEquip.RC_10515},
	partsType=6,
	partsIds={
		TppEquip.ST_20104,
		TppEquip.ST_20205,
		TppEquip.ST_30114,
		TppEquip.ST_30305,
		TppEquip.ST_60102,
		TppEquip.ST_60001
	}
```
This code adds 6 allowed scopes (partsType=6) to URAGAN-SG, but we definitely need more. Feel free to expand that list with any scopes from the table below. Save the file, make a new customized gun, choose from gorillion scopes. ![Scopes](https://0x0.st/PWR.jpg)


#Closed slots
Closed slots are cannot be changed via ingame interface at all, so you will need to modify them in lua scripts (or change the gun frame to another one with more slots).

Changing barrel: changes fine ![New barrel](https://0x0.st/PWg.jpg)

##Changing frame
Changing frame may cause crashes, hangs etc.

Open `\master\0\00\Assets\tpp\level_asset\weapon\ParameterTables\parts\EquipParameters.lua`, find your gun's frame - `RC_10515` for URAGAN-SG, replace it with another frame from the table below.

Changing frame to ZORN: open slots are changed according to a new frame (no modifications allowed) saving previous options (laser sights) ![New frame](https://0x0.st/PWx.jpg)

Changing frame to RASP SG+P with more slots, game hangs on sortie prep: ![New frame](https://0x0.st/PWE.jpg)

##Changing closed slots
Open `\master\0\00\Assets\tpp\level_asset\weapon\ParameterTables\parts\EquipParameters.lua`, find your gun's frame - `RC_10515` for URAGAN-SG, replace stuff below the line with the frame - TppEquip.SK_, TppEquip.MZ_ etc. with anything you want from the table below, save the file, make a new customized gun, the end. Save your gun, revert changes in file. 

Changing muzzle for a Bambetov one (MZ_60203) - ![New muzzle](https://0x0.st/PW7.jpg)

#Tables

* [0 - Frames aka receivers](#0)
* [1 - Barrels](#1)
* [2 - Ammo/magazines](#2)
* [3 - Stock](#3)
* [4 - Muzzle](#4)
* [5 - Muzzle options](#5)
* [6 and 7 - first and second sights](#6)
* [8 and 9 - Lasers/Flashlights](#8)
* [10 - underbarrels and foregrips](#10)


###<a name="0">0 - Frames aka receivers</a>
type|script name|real name|options
-----|-----|-----|-----
    0|TppEquip.RC_10001|D114 FRAME|
    0|TppEquip.RC_10003|D114 EX-FRAME|Undermount (Lower Option Slot)
    0|TppEquip.RC_10004|D114 HS-FRAME|Undermount (Lower Option Slot), Operating Precision Up (Grouping/Auto-Aim Range Up)
    0|TppEquip.RC_10006|D114 CB-FRAME|Undermount (Lower Option Slot), Carbine Conversion (Closer Shot Grouping), Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_10006_u|D114 UBCB-FRAME|Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_10015|D114-9 FRAME|Undermount (Lower Option Slot), Operating Precision Up (Grouping/Auto-Aim Range Up), Piercing Round Conversion (Penetration Up)
    0|TppEquip.RC_10024|D114LB FRAME|Undermount (Lower Option Slot), Long Barrel Conversion (Effective Range Up), Operating Precision Up (Grouping/Auto-Aim Range Up)
    0|TppEquip.RC_10035|D114LB-9 FRAME|Undermount (Lower Option Slot), Long Barrel Conversion (Effective Range Up), Operating Precision Up (Grouping/Auto-Aim Range Up), Piercing Round Conversion (Penetration Up)
    0|TppEquip.RC_10101|S.PISTOL FRAME|
    0|TppEquip.RC_10102|S.PISTOL L-FRAME|Long Barrel Conversion (Effective Range Up), Undermount (Lower Option Slot)
    0|TppEquip.RC_10105|S.PISTOL ITG-FRAME|Long Barrel Conversion (Effective Range Up), Undermount (Lower Option Slot), Built-in Suppressor (Durability: Unlimited)
    0|TppEquip.RC_10107|S.P CB-FRAME|Long Barrel Conversion (Effective Range Up), Undermount (Lower Option Slot), Built-in Suppressor (Durability: Unlimited), Carbine Conversion (Closer Shot Grouping), Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_10107_u|S.P UBCB-FRAME|Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_10117|S.P +SB FRAME|Long Barrel Conversion (Effective Range Up), Undermount (Lower Option Slot), Built-in Suppressor (Durability: Unlimited), Tranquilizer Round Fast-acting Conversion (Damage Up)
    0|TppEquip.RC_10125|S.P AP FRAME|Long Barrel Conversion (Effective Range Up), Undermount (Lower Option Slot), Tranquilizer Round Glass-piercing Conversion (Penetration Up)
    0|TppEquip.RC_10134|S.P9 FRAME|Long Barrel Conversion (Effective Range Up), Undermount (Lower Option Slot), 9mm Live Round Conversion (Attack Type: Lethal)
    0|TppEquip.RC_10136|S.P9 ITG-FRAME|Long Barrel Conversion (Effective Range Up), Undermount (Lower Option Slot), 9mm Live Round Conversion (Attack Type: Lethal), Built-in Suppressor (Durability: Unlimited)
    0|TppEquip.RC_10201|BURKOV FRAME|
    0|TppEquip.RC_10203|BURKOV EX-FRAME|Undermount (Lower Option Slot)
    0|TppEquip.RC_10205|BURKOV ITG-FRAME|Undermount (Lower Option Slot), Built-in Suppressor (Durability: Unlimited)
    0|TppEquip.RC_10214|BURKOV TB FRAME|Undermount (Lower Option Slot), Tranquilizer Round Conversion (Attack Type: Non-lethal)
    0|TppEquip.RC_10216|BURKOV HS FRAME|Undermount (Lower Option Slot), Tranquilizer Round Conversion (Attack Type: Non-lethal), Built-in Suppressor (Durability: Unlimited)
    0|TppEquip.RC_10302|GEIST FRAME|
    0|TppEquip.RC_10303|GEIST EX-FRAME|Undermount (Lower Option Slot)
    0|TppEquip.RC_10304|GEIST 3B-FRAME|Undermount (Lower Option Slot), 3-round Burst Conversion (Enables 3-round Burst Fire)
    0|TppEquip.RC_10306|GEIST 3BSP-FRAME|Undermount (Lower Option Slot), 3-round Burst Conversion (Enables 3-round Burst Fire), Compensator (Closer Shot Grouping)
    0|TppEquip.RC_10307|GEIST CB-FRAME|Undermount (Lower Option Slot), 3-round Burst Conversion (Enables 3-round Burst Fire), Compensator (Closer Shot Grouping), Carbine Conversion (Closer Shot Grouping), Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_10307_u|GEIST UBCB-FRAME|Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_10403|S333 FRAME|
    0|TppEquip.RC_10405|S333 +P FRAME|Undermount (Lower Option Slot), Overpressure Round Conversion (Damage Up)
    0|TppEquip.RC_10407|S333 +P+ FRAME|Undermount (Lower Option Slot), Overpressure Round Conversion (Damage Up), Enhanced Overpressure Rounds (Damage Up)
    0|TppEquip.RC_10503|URAGAN FRAME|
    0|TppEquip.RC_10504|URAGAN EX-FRAME|Undermount (Lower Option Slot), Scope Mount (Upper Option Slot)
    0|TppEquip.RC_10515|URAGAN SG-FRAME|Undermount (Lower Option Slot), Scope Mount (Upper Option Slot), Slug Round Conversion (Damage Up)
    0|TppEquip.RC_10526|URAGAN AS-FRAME|Undermount (Lower Option Slot), Scope Mount (Upper Option Slot), Air Shock Round Conversion (Attack Type: Non-lethal)
    0|TppEquip.RC_10603|ZORN FRAME|
    0|TppEquip.RC_10604|ZORN EX-FRAME|Undermount (Lower Option Slot)
    0|TppEquip.RC_10615|ZORN SM-FRAME|Undermount (Lower Option Slot), Smoke Round Conversion (Attack Type: Non-lethal)
    0|TppEquip.RC_10626|ZORN ST-FRAME|Undermount (Lower Option Slot), Stun Round Conversion (Attack Type: Non-lethal)
    0|TppEquip.RC_10637|ZORN SL-FRAME|Undermount (Lower Option Slot), Sleeping Gas Round Conversion (Attack Type: Non-lethal)
    0|TppEquip.RC_10703|WATER-PI FRAME|
    0|TppEquip.RC_10704|WATER-PII FRAME|Effective Range Up 1, Stopping Power Up
    0|TppEquip.RC_10705|WATER-PIII FRAME|Effective Range Up 1, Stopping Power Up
    0|TppEquip.RC_20002|Sz. RECEIVER|
    0|TppEquip.RC_20004|Sz. EX2RECEIVER|Scope Mount (Upper Option Slot), Undermount (Lower Option Slot)
    0|TppEquip.RC_20006|Sz. LW-RECEIVER|Scope Mount (Upper Option Slot), Undermount (Lower Option Slot), Lightweight Conversion (Auto-Aim Range Up)
    0|TppEquip.RC_20015|Sz. HS-RECEIVER|Scope Mount (Upper Option Slot), Undermount (Lower Option Slot), High Firing Rate Receiver (Firing Speed Up)
    0|TppEquip.RC_20103|ZEEV RECEIVER|
    0|TppEquip.RC_20104|ZEEV EX1RECEIVER|Scope Mount (Upper Option Slot)
    0|TppEquip.RC_20105|ZEEV EX2RECEIVER|Scope Mount (Upper Option Slot), Undermount (Lower Option Slot)
    0|TppEquip.RC_20116|ZEEV-10 RECEIVER|Scope Mount (Upper Option Slot), Undermount (Lower Option Slot), 10mm Conversion (Damage Up)
    0|TppEquip.RC_20203|MACHT RECEIVER|
    0|TppEquip.RC_20204|MACHT EX1RECEIVER|Undermount (Lower Option Slot)
    0|TppEquip.RC_20205|MACHT EX2RECEIVER|Undermount (Lower Option Slot), Scope Mount (Upper Option Slot)
    0|TppEquip.RC_20215|MACHT L-RECEIVER|Undermount (Lower Option Slot), Scope Mount (Upper Option Slot), Long Barrel Conversion (Effective Range Up)
    0|TppEquip.RC_20225|MACHT S-RECEIVER|Undermount (Lower Option Slot), Scope Mount (Upper Option Slot), Short Barrel Conversion (Firing Speed/Auto-Aim Range Up)
    0|TppEquip.RC_20302|RIOT EX2RECEIVER|
    0|TppEquip.RC_20303|RIOT EX2RECEIVER|Scope Mount (Upper Option Slot)
    0|TppEquip.RC_20304|RIOT EX2RECEIVER|Scope Mount (Upper Option Slot), Undermount (Lower Option Slot)
    0|TppEquip.RC_20307|RIOT EX2RECEIVER|Scope Mount (Upper Option Slot), Undermount (Lower Option Slot)
    0|TppEquip.RC_30001|SVG76 RECEIVER|
    0|TppEquip.RC_30003|SVG76 EX1RECEIVER|Scope Mount (Upper Option Slot)
    0|TppEquip.RC_30005|SVG76 EX2RECEIVER|Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_30014|SVG67 EX1RECEIVER|7.62mm Conversion (Damage Up), Scope Mount (Upper Option Slot)
    0|TppEquip.RC_30016|SVG67 EX2RECEIVER|7.62mm Conversion (Damage Up), Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_30034|SVG67 RECEIVER|7.62mm Conversion (Damage Up)
    0|TppEquip.RC_30101|MRS-4 RECEIVER|
    0|TppEquip.RC_30102|MRS-4 EX1RECEIVER|Scope Mount (Upper Option Slot)
    0|TppEquip.RC_30104|MRS-4 EX2RECEIVER|Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_30117|MRS-4 EX2RECEIVER|Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_30201|ARC RECEIVER|
    0|TppEquip.RC_30202|ARC EX2RECEIVER|Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_30232|ARCNL RECEIVER|Rubber Bullet Conversion (Attack Type: Non-lethal)
    0|TppEquip.RC_30233|ARCNL EX1RECEIVER|Rubber Bullet Conversion (Attack Type: Non-lethal), Scope Mount (Upper Option Slot)
    0|TppEquip.RC_30235|ARCNL EX2RECEIVER|Rubber Bullet Conversion (Attack Type: Non-lethal), Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_30237|ARCNL EX2RECEIVER|Rubber Bullet Conversion (Attack Type: Non-lethal), Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_30303|G44 RECEIVER|
    0|TppEquip.RC_30305|G44 EX1RECEIVER|Scope Mount (Upper Option Slot)
    0|TppEquip.RC_30306|G44 EX2RECEIVER|Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_30325|G44MG RECEIVER|9mm Conversion (Portable Ammo Count Up)
    0|TppEquip.RC_30327|G44MG EX2RECEIVER|9mm Conversion (Portable Ammo Count Up), Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_40001|RASP RECEIVER|
    0|TppEquip.RC_40002|RASP EX1-RECEIVER|Side Mount (Side Option Slot)
    0|TppEquip.RC_40003|RASP EX2-RECEIVER|Side Mount (Side Option Slot), Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_40004|RASP +P RECEIVER|Side Mount (Side Option Slot), Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots), Magnum Shotshell Conversion (Damage Up)
    0|TppEquip.RC_40012|RASP SG-RECEIVER|Slug Round Conversion (Damage Up)
    0|TppEquip.RC_40013|RASP EX1S-RECEIVER|Slug Round Conversion (Damage Up), Side Mount (Side Option Slot)
    0|TppEquip.RC_40014|RASP EX2S-RECEIVER|Slug Round Conversion (Damage Up), Side Mount (Side Option Slot), Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_40015|RASP SG+P RECEIVER|Slug Round Conversion (Damage Up), Side Mount (Side Option Slot), Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots), Slug Round Enhancement (Damage Up)
    0|TppEquip.RC_40023|RASP AS-RECEIVER|Air Shock Round Conversion (Attack Type: Non-lethal)
    0|TppEquip.RC_40024|RASP EX1A-RECEIVER|Air Shock Round Conversion (Attack Type: Non-lethal), Side Mount (Side Option Slot)
    0|TppEquip.RC_40025|RASP EX2A-RECEIVER|Air Shock Round Conversion (Attack Type: Non-lethal), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_40032|RASP L-RECEIVER|Long Barrel Conversion (Effective Range Up)
    0|TppEquip.RC_40033|RASP EX2L-RECEIVER|Long Barrel Conversion (Effective Range Up), Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_40034|RASP EX3L-RECEIVER|Ultra-long Barrel Conversion (Effective Range Up), Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots), Side Mount (Side Option Slot)
    0|TppEquip.RC_40035|RASP L+P RECEIVER|Ultra-long Barrel Conversion (Effective Range Up), Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots), Side Mount (Side Option Slot), Magnum Shotshell Conversion (Damage Up)
    0|TppEquip.RC_40042|RASP S-RECEIVER|Short Barrel Conversion (Firing Speed/Auto-Aim Range Up)
    0|TppEquip.RC_40042_u|RASP UB-RECEIVER|Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_40044|RASP EX2S-RECEIVER|Short Barrel Conversion (Firing Speed/Auto-Aim Range Up), Scope Mount (Upper Option Slot), Side Mount (Side Option Slot), Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_40045|RASP S+P RECEIVER|Short Barrel Conversion (Firing Speed/Auto-Aim Range Up), Scope Mount (Upper Option Slot), Side Mount (Side Option Slot), Magnum Shotshell Conversion (Damage Up), Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_40045_u|RASP UB+P RECEIVER|Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_40102|S1000 RECEIVER|
    0|TppEquip.RC_40102_u|S1000 UB-RECEIVER|Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_40103|S1000 EX1RECEIVER|Scope Mount (Upper Option Slot)
    0|TppEquip.RC_40105|S1000 SPL-RECEIVER|Scope Mount (Upper Option Slot), Reload Speed Up
    0|TppEquip.RC_40115|S1000 SG-RECEIVER|Slug Round Conversion (Damage Up), Scope Mount (Upper Option Slot)
    0|TppEquip.RC_40123|S1000 AS-RECEIVER|Air Shock Round Conversion (Attack Type: Non-lethal), Scope Mount (Upper Option Slot)
    0|TppEquip.RC_40126|S1000 AS-RECEIVER|Air Shock Round Conversion (Attack Type: Non-lethal), Scope Mount (Upper Option Slot)
    0|TppEquip.RC_40136|S1000 EX2RECEIVER|Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots), Shotshell Holder (Portable Ammo Count Up)
    0|TppEquip.RC_40203|KAB83 RECEIVER|
    0|TppEquip.RC_40204|KAB83 EX1RECEIVER|Scope Mount (Upper Option Slot)
    0|TppEquip.RC_40207|KAB83 EX2RECEIVER|Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_40304|BULL-H RECEIVER|
    0|TppEquip.RC_40305|BULL-H EX2RECEIVER|Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    0|TppEquip.RC_40306|BULL-H EX3RECEIVER|Side Mount (Side Option Slot), Undermount (Lower Option Slot), Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_40307|BULL-H FA-RECEIVER|Side Mount (Side Option Slot), Undermount (Lower Option Slot), Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots), Full Auto Conversion (Firing Speed Up)
    0|TppEquip.RC_50002|FAKEL RECEIVER|
    0|TppEquip.RC_50003|FAKEL EX1RECEIVER|Scope Mount (Upper Option Slot), Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_50004|FAKEL EX2RECEIVER|Scope Mount (Upper Option Slot), Side Mount (Side Option Slot), Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_50005|FAKEL EX3RECEIVER|Scope Mount (Upper Option Slot), Side Mount (Side Option Slot), Additional Option Slot (2x Upper Option Slots), Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_50015|FAKEL SM-RECEIVER|Scope Mount (Upper Option Slot), Side Mount (Side Option Slot), Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_50026|FAKEL ST-RECEIVER|Scope Mount (Upper Option Slot), Side Mount (Side Option Slot), Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_50047|FAKEL SL-RECEIVER|Scope Mount (Upper Option Slot), Side Mount (Side Option Slot), Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_50033|FAK-2B RECEIVER|Double-barrel Conversion (Loaded Ammo Count Up)
    0|TppEquip.RC_50034|FAK-2B EX2RECEIVER|Double-barrel Conversion (Loaded Ammo Count Up), Scope Mount (Upper Option Slot), Side Mount (Side Option Slot)
    0|TppEquip.RC_50035|FAK-3B EX2RECEIVER|Triple-barrel Conversion (Loaded Ammo Count Up), Scope Mount (Upper Option Slot), Side Mount (Side Option Slot)
    0|TppEquip.RC_50036|FAK-3B EX3RECEIVER|Triple-barrel Conversion (Loaded Ammo Count Up), Scope Mount (Upper Option Slot), Side Mount (Side Option Slot), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_50102|DGL103 RECEIVER|
    0|TppEquip.RC_50103|DGL103 EX1RECEIVER|Scope Mount (Upper Option Slot), Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_50104|DGL103 EX2RECEIVER|Scope Mount (Upper Option Slot), Side Mount (Side Option Slot), Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_50105|DGL103 EX3RECEIVER|Scope Mount (Upper Option Slot), Side Mount (Side Option Slot), Additional Option Slot (2x Upper Option Slots), Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_50115|DGL103 SM-RECEIVER|Scope Mount (Upper Option Slot), Side Mount (Side Option Slot), Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_50126|DGL103 ST-RECEIVER|Scope Mount (Upper Option Slot), Side Mount (Side Option Slot), Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_50147|DGL103 SL-RECEIVER|Scope Mount (Upper Option Slot), Side Mount (Side Option Slot), Underbarrel Conversion (Undermount Slot)
    0|TppEquip.RC_50133|DGL EX1L-RECEIVER|Long Barrel Conversion (Effective Range Up), Scope Mount (Upper Option Slot)
    0|TppEquip.RC_50134|DGL EX2L-RECEIVER|Long Barrel Conversion (Effective Range Up), Scope Mount (Upper Option Slot), Side Mount (Side Option Slot)
    0|TppEquip.RC_50135|DGL RH-RECEIVER|Long Barrel Conversion (Effective Range Up), Scope Mount (Upper Option Slot), Side Mount (Side Option Slot), RPG Conversion (Effective Range Up)
    0|TppEquip.RC_50136|DGL RH-EX2RECEIVER|Long Barrel Conversion (Effective Range Up), Scope Mount (Upper Option Slot), Side Mount (Side Option Slot), RPG Conversion (Effective Range Up), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_50202|RGL RECEIVER|
    0|TppEquip.RC_50203|RGL EX2RECEIVER|Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_50204|RGL EX3RECEIVER|Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots), Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    0|TppEquip.RC_50215|RGL SM-RECEIVER|Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots), Side Mount (Side Option Slot), Undermount (Lower Option Slot), Smoke Round Conversion (Attack Type: Non-lethal)
    0|TppEquip.RC_50226|RGL ST-RECEIVER|Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots), Side Mount (Side Option Slot), Undermount (Lower Option Slot), Stun Round Conversion (Attack Type: Non-lethal)
    0|TppEquip.RC_50237|RGL SL-RECEIVER|Scope Mount (Upper Option Slot), Additional Option Slot (2x Upper Option Slots), Side Mount (Side Option Slot), Undermount (Lower Option Slot), Sleeping Gas Round Conversion (Attack Type: Non-lethal)
    0|TppEquip.RC_50303|HAIL RECEIVER|
    0|TppEquip.RC_50305|HAIL EX3RECEIVER|Enhanced Barrel Accuracy (Effective Range Up), Additional Option Slot (2x Upper Option Slots), Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    0|TppEquip.RC_60001|RENOV L-RECEIVER|
    0|TppEquip.RC_60002|RENOV RECEIVER|
    0|TppEquip.RC_60007|RENOV RF-RECEIVER|Magnum Round Conversion (Damage Up)
    0|TppEquip.RC_60005|RENOV EX2RECEIVER|Magnum Round Conversion (Damage Up), Additional Option Slot (2x Upper Option Slots), Side Mount (Side Option Slot)
    0|TppEquip.RC_60012|RENOV TPL-RECEIVER|Tranquilizer Round Conversion (Attack Type: Non-lethal)
    0|TppEquip.RC_60013|RENOV TP-RECEIVER|Tranquilizer Round Conversion (Attack Type: Non-lethal)
    0|TppEquip.RC_60016|RENOV TP2-RECEIVER|Tranquilizer Round Conversion (Attack Type: Non-lethal), Additional Option Slot (2x Upper Option Slots), Side Mount (Side Option Slot)
    0|TppEquip.RC_60102|M2000 L-RECEIVER|
    0|TppEquip.RC_60103|M2000 RECEIVER|
    0|TppEquip.RC_60106|M2000 RF-RECEIVER|Magnum Round Conversion (Damage Up)
    0|TppEquip.RC_60107|M2000 EX2RECEIVER|Magnum Round Conversion (Damage Up), Additional Option Slot (2x Upper Option Slots), Side Mount (Side Option Slot)
    0|TppEquip.RC_60114|M2000 NL-RECEIVER|Tranquilizer Round Conversion (Attack Type: Non-lethal)
    0|TppEquip.RC_60117|M2000 NL2-RECEIVER|Tranquilizer Round Conversion (Attack Type: Non-lethal), Additional Option Slot (2x Upper Option Slots), Side Mount (Side Option Slot)
    0|TppEquip.RC_60203|BAMBETOV1 RECEIVER|
    0|TppEquip.RC_60206|BAMBETOV2 RECEIVER|Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_60303|MRS71 RECEIVER|
    0|TppEquip.RC_60306|MRS71 EX2RECEIVER|Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_60315|MRS73 RECEIVER|5.56mm Conversion (Closer Shot Grouping)
    0|TppEquip.RC_60317|MRS73 EX2RECEIVER|5.56mm Conversion (Closer Shot Grouping), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_60325|MRS-NL RECEIVER|Tranquilizer Round Conversion (Attack Type: Non-lethal)
    0|TppEquip.RC_60327|MRS-NL EX2RECEIVER|Tranquilizer Round Conversion (Attack Type: Non-lethal), Additional Option Slot (2x Upper Option Slots)
    0|TppEquip.RC_60404|BRENNAN1 RECEIVER|
    0|TppEquip.RC_60405|BRENNAN2 RECEIVER|Additional Option Slot (2x Upper Option Slots), Side Mount (Side Option Slot)
    0|TppEquip.RC_60415|SERVAL1 RECEIVER|Automatic Conversion (Firing Speed Up)
    0|TppEquip.RC_60416|SERVAL2 RECEIVER|Additional Option Slot (2x Upper Option Slots), Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    0|TppEquip.RC_70002|ALM-1 RECEIVER|
    0|TppEquip.RC_70003|ALM-2 RECEIVER|Scope Mount (Upper Option Slot)
    0|TppEquip.RC_70015|ALM-H RECEIVER|Scope Mount (Upper Option Slot), High Firing Rate Receiver (Firing Speed Up)
    0|TppEquip.RC_70103|AAM-1 RECEIVER|
    0|TppEquip.RC_70104|AAM-2 RECEIVER|Scope Mount (Upper Option Slot)
    0|TppEquip.RC_70114|AAMF-1 RECEIVER|7.62mm Conversion (Damage Up)
    0|TppEquip.RC_70115|AAMF-2 RECEIVER|7.62mm Conversion (Damage Up), Scope Mount (Upper Option Slot)
    0|TppEquip.RC_70203|LPG-1 RECEIVER|
    0|TppEquip.RC_70204|LPG-2 RECEIVER|Scope Mount (Upper Option Slot)
    0|TppEquip.RC_80002|GROM LAUNCHER|
    0|TppEquip.RC_80004|GROM-H LAUNCHER|Stopping Power Up
    0|TppEquip.RC_80006|GROM-H2 LAUNCHER|Tandem Warhead Conversion (Damage Up), Side Mount (Side Option Slot)
    0|TppEquip.RC_80103|MR LAUNCHER|
    0|TppEquip.RC_80104|MR SH-LAUNCHER|Stopping Power Up, Added Shield
    0|TppEquip.RC_80105|MR EX1-LAUNCHER|Stopping Power Up, Added Shield, Side Mount (Side Option Slot)
    0|TppEquip.RC_80116|MR SL-LAUNCHER|Sleeping Gas Round Conversion (Attack Type: Non-lethal), Added Shield, Side Mount (Side Option Slot)
    0|TppEquip.RC_80124|MR HE1-LAUNCHER|Grenade Conversion (Blast Radius Up)
    0|TppEquip.RC_80125|MR HE2-LAUNCHER|Grenade Conversion (Blast Radius Up), Added Shield, Stopping Power Up
    0|TppEquip.RC_80126|MR HE3-LAUNCHER|Grenade Conversion (Blast Radius Up), Added Shield, Stopping Power Up, Side Mount (Side Option Slot)
    0|TppEquip.RC_80203|K-BEE LAUNCHER|
    0|TppEquip.RC_80204|K-BEE1 LAUNCHER|Stopping Power Up, Lock-on Speed Up
    0|TppEquip.RC_80205|K-BEE2 LAUNCHER|Stopping Power Up, Enhanced Homing
    0|TppEquip.RC_80206|K-BEE3 LAUNCHER|Stopping Power Up, Lock-on Speed Up
    0|TppEquip.RC_80303|CGM LAUNCHER|
    0|TppEquip.RC_80304|CGM1 LAUNCHER|Stopping Power Up, Enhanced Homing
    0|TppEquip.RC_80305|CGM2 LAUNCHER|Warhead No. Up (Max. Lock-ons: 8)
    0|TppEquip.RC_80306|CGM3 LAUNCHER|Stopping Power Up, Lock-on Speed Up
    0|TppEquip.RC_SkullFace_hg_010|S333 FRAME|
    0|TppEquip.RC_SP_hg_010|S333 FRAME|
    0|TppEquip.RC_SP_hg_020|S333 FRAME|
    0|TppEquip.RC_SP_sm_010|Sz. RECEIVER|
    0|TppEquip.RC_SP_sg_010|RASP RECEIVER|
    0|TppEquip.RC_HoneyBee|K-BEE LAUNCHER|
    

###<a name="1">1 - Barrels</a>
type|script name|real name|options
-----|-----|-----|-----
    1|TppEquip.BA_10001|D114 BARREL|
    1|TppEquip.BA_10004|D114 HP-BARREL|
    1|TppEquip.BA_10024|D114 L-BARREL|
    1|TppEquip.BA_10101|S.PISTOL BARREL|
    1|TppEquip.BA_10102|S.PISTOL L-BARREL |
    1|TppEquip.BA_10201|BURKOV BARREL |
    1|TppEquip.BA_10302|GEIST P3 BARREL |
    1|TppEquip.BA_10403|S333 BARREL |
    1|TppEquip.BA_10405|S333 R-BARREL |Scope Mount (Upper Option Slot)
    1|TppEquip.BA_10407|S333 MF-BARREL |Scope Mount (Upper Option Slot), Counterweight (Closer Shot Grouping)
    1|TppEquip.BA_10414|S324LB L-BARREL |Long Barrel Conversion (Effective Range Up)
    1|TppEquip.BA_10415|S324LB R-BARREL|Long Barrel Conversion (Effective Range Up), Scope Mount (Upper Option Slot)
    1|TppEquip.BA_10417|S324LB MF-BARREL|Long Barrel Conversion (Effective Range Up), Scope Mount (Upper Option Slot), Counterweight (Closer Shot Grouping)
    1|TppEquip.BA_10424|S362SB S-BARREL |Snub Nose Conversion (Firing Speed/Auto-Aim Range Up)
    1|TppEquip.BA_10425|S362SB MF-BARREL |Snub Nose Conversion (Firing Speed/Auto-Aim Range Up), Compensator (Closer Shot Grouping), Scope Mount (Upper Option Slot)
    1|TppEquip.BA_10503|URAGAN-5 BARREL|
    1|TppEquip.BA_10504|URAGAN-5P L-BARREL|Long Barrel Conversion (Effective Range Up)
    1|TppEquip.BA_10603|ZORN-KP BARREL|
    1|TppEquip.BA_10703|WATER-P BARREL |
    1|TppEquip.BA_10704|WATER-P BARREL |
    1|TppEquip.BA_10705|WATER-P BARREL |
    1|TppEquip.BA_20002|Sz.-336 BARREL |
    1|TppEquip.BA_20103|ZEEV BARREL|
    1|TppEquip.BA_20203|MACHT 37 BARREL|
    1|TppEquip.BA_20215|MACHT 37 L-BARREL|
    1|TppEquip.BA_20225|MACHT 37 S-BARREL|
    1|TppEquip.BA_30001|SVG TYPE BARREL|
    1|TppEquip.BA_30003|SVG TYPE R-BARREL|Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_30023|SVG TYPE S-BARREL|Short Barrel Conversion (Firing Speed/Auto-Aim Range Up)
    1|TppEquip.BA_30024|SVG TYPE SR-BARREL|Short Barrel Conversion (Firing Speed/Auto-Aim Range Up), Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_30035|SVG TYPE SS-BARREL|Ultra-short Barrel Conversion (Firing Speed/Auto-Aim Range Up)
    1|TppEquip.BA_30036|SVG TYPE S2-BARREL|Ultra-short Barrel Conversion (Firing Speed/Auto-Aim Range Up), Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_30043|SVG TYPE FS-BARREL|LMG Barrel Conversion (Closer Shot Grouping)
    1|TppEquip.BA_30044|SVG TYPE F2-BARREL|LMG Barrel Conversion (Closer Shot Grouping), Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_30102|MRS TYPE BARREL|
    1|TppEquip.BA_30103|MRS TYPE R-BARREL|Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_30107|MRS TYPE SR-BARREL|Short Barrel Conversion (Firing Speed/Auto-Aim Range Up), Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_30113|MRS TYPE L-BARREL|Long Barrel Conversion (Effective Range Up)
    1|TppEquip.BA_30115|MRS TYPE LR-BARREL|Stout Barrel Conversion (Closer Shot Grouping), Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_30123|MRS TYPE FS-BARREL|LMG Barrel Conversion (Closer Shot Grouping)
    1|TppEquip.BA_30124|MRS TYPE F2-BARREL|LMG Barrel Conversion (Closer Shot Grouping), Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_30201|ARC TYPE L-BARREL|
    1|TppEquip.BA_30203|ARC TYPE LR-BARREL|Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_30213|ARC TYPE S-BARREL|Short Barrel Conversion (Firing Speed/Auto-Aim Range Up)
    1|TppEquip.BA_30214|ARC TYPE SR-BARREL|Short Barrel Conversion (Firing Speed/Auto-Aim Range Up), Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_30223|ARC TYPE FS-BARREL|LMG Barrel Conversion (Closer Shot Grouping)
    1|TppEquip.BA_30224|ARC TYPE F2-BARREL|LMG Barrel Conversion (Closer Shot Grouping), Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_30303|G44 TYPE BARREL|
    1|TppEquip.BA_30304|G44 TYPE R-BARREL|Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_30314|G44 TYPE S-BARREL|Short Barrel Conversion (Firing Speed/Auto-Aim Range Up)
    1|TppEquip.BA_30315|G44 TYPE SR-BARREL|Short Barrel Conversion (Firing Speed/Auto-Aim Range Up), Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_30325|G44 TYPE 9-BARREL|Ultra-short Barrel Conversion (Firing Speed/Auto-Aim Range Up)
    1|TppEquip.BA_30326|G44 TYPE 9R-BARREL|Ultra-short Barrel Conversion (Firing Speed/Auto-Aim Range Up), Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_30334|G44 TYPE FS-BARREL|Heavy Barrel Conversion (Closer Shot Grouping)
    1|TppEquip.BA_30335|G44 TYPE F2-BARREL|Heavy Barrel Conversion (Closer Shot Grouping), Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_40001|RASP BARREL|
    1|TppEquip.BA_40032|RASP L-BARREL|
    1|TppEquip.BA_40034|RASP LL-BARREL|
    1|TppEquip.BA_40042|RASP S-BARREL|
    1|TppEquip.BA_40043|RASP SS-BARREL|Sawed-off Conversion (Firing Speed/Auto-Aim Range Up)
    1|TppEquip.BA_40102|S1000 BARREL|
    1|TppEquip.BA_40103|S1000 R-BARREL|Side Mount (Side Option Slot)
    1|TppEquip.BA_40133|S1000 L-BARREL|Magazine Tube Extension 1 (Loaded Ammo Count Up)
    1|TppEquip.BA_40134|S1000 LR-BARREL|Magazine Tube Extension 1 (Loaded Ammo Count Up), Side Mount (Side Option Slot)
    1|TppEquip.BA_40135|S1000 LLR-BARREL|Magazine Tube Extension 2 (Loaded Ammo Count Up), Side Mount (Side Option Slot)
    1|TppEquip.BA_40143|S1000 S-BARREL|Short Barrel Conversion (Firing Speed/Auto-Aim Range Up)
    1|TppEquip.BA_40203|KAB83 BARREL|
    1|TppEquip.BA_40205|KAB83 R-BARREL|Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_40304|BULL-H BARREL|
    1|TppEquip.BA_50002|FAKEL BARREL|
    1|TppEquip.BA_50102|DGL103 BARREL|
    1|TppEquip.BA_50133|DGL103 L-BARREL|
    1|TppEquip.BA_50202|RGL-220 BARREL|
    1|TppEquip.BA_50203|RGL-220 L-BARREL|Long Barrel Conversion (Semi-long/Effective Range Up)
    1|TppEquip.BA_50204|RGL-220 LL-BARREL|Long Barrel Conversion (Long/Effective Range Up)
    1|TppEquip.BA_50303|HAIL BARREL|
    1|TppEquip.BA_50305|HAIL HP-BARREL|
    1|TppEquip.BA_60001|RENOV BARREL|
    1|TppEquip.BA_60004|RENOV HP-BARREL|High-accuracy Barrel 1 (Effective Range Up)
    1|TppEquip.BA_60005|RENOV MF-BARREL|High-accuracy Barrel 2 (Effective Range Up)
    1|TppEquip.BA_60102|M2000 BARREL|
    1|TppEquip.BA_60105|M2000 B-BARREL|Bull Barrel 1 (Closer Shot Grouping)
    1|TppEquip.BA_60107|M2000 MF-BARREL|Bull Barrel 2 (Closer Shot Grouping)
    1|TppEquip.BA_60203|BAMBETOV BARREL|
    1|TppEquip.BA_60205|BAMBETOV R-BARREL|Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_60303|MRS SP BARREL|
    1|TppEquip.BA_60305|MRS SP MF-BARREL|Bull Barrel (Closer Shot Grouping), Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_60404|BRENNAN BARREL|
    1|TppEquip.BA_60405|BRENNAN HP-BARREL|Enhanced Barrel Accuracy 1 (Effective Range Up)
    1|TppEquip.BA_60407|BRENNAN MF-BARREL|Enhanced Barrel Accuracy 2 (Effective Range Up)
    1|TppEquip.BA_60415|SERVAL BARREL|
    1|TppEquip.BA_60416|SERVAL HP-BARREL|Enhanced Barrel Accuracy 1 (Effective Range Up)
    1|TppEquip.BA_60417|SERVAL MF-BARREL|Enhanced Barrel Accuracy 2 (Effective Range Up)
    1|TppEquip.BA_70002|ALM 48 BARREL|
    1|TppEquip.BA_70004|ALM 48 F-BARREL|Heat Sink (Firing Speed Up), Side Mount (Side Option Slot)
    1|TppEquip.BA_70006|ALM 48 P-BARREL|Heat Guard (Firing Speed Up), Side Mount (Side Option Slot)
    1|TppEquip.BA_70024|ALM 48 S-BARREL|Short Barrel Conversion (Firing Speed/Auto-Aim Range Up), Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_70103|AAM BARREL|
    1|TppEquip.BA_70105|AAM R-BARREL|Side Mount (Side Option Slot)
    1|TppEquip.BA_70106|AAM S-BARREL|Short Barrel Conversion (Firing Speed/Auto-Aim Range Up), Side Mount (Side Option Slot), Undermount (Lower Option Slot)
    1|TppEquip.BA_70116|AAM HS-BARREL|Heat Sink (Firing Speed Up), Side Mount (Side Option Slot)
    1|TppEquip.BA_70203|LPG-61 BARREL|
    1|TppEquip.BA_70205|LPG-61 R-BARREL|Side Mount (Side Option Slot)
    1|TppEquip.BA_70207|LPG-61 S-BARREL|Short Barrel Conversion (Firing Speed/Auto-Aim Range Up), Side Mount (Side Option Slot), Undermount (Lower Option Slot)
  
  
###<a name="2">2 - Ammo/magazines</a>
type|script name|real name|options
-----|-----|-----|-----
    2|TppEquip.AM_10001|.45 MAG x7|
    2|TppEquip.AM_10003|.45 MAG x10|Long Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_10015|AP 9 MAG x10|Long Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_10015_0|AP 9 MAG x7|
    2|TppEquip.AM_10101|ANEST.9 MAG x7|
    2|TppEquip.AM_10103|ANEST.9 MAG x10|Long Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_10125|AP ANEST.9 MAG x10|Long Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_10125_0|AP ANEST.9 MAG x7|
    2|TppEquip.AM_10134|9 MAG x10|Long Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_10134_0|9 MAG x7|
    2|TppEquip.AM_10201|9 MAG x9|
    2|TppEquip.AM_10203|9 MAG x12|Long Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_10214|ANEST. 9 MAG x12|Long Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_10214_0|ANEST. 9 MAG x9|
    2|TppEquip.AM_10302|9 MAG x17|
    2|TppEquip.AM_10303|9 MAG x30|Long Magazine 1 (Loaded Ammo Count Up)
    2|TppEquip.AM_10305|9 MAG x42|Long Magazine 2 (Loaded Ammo Count Up)
    2|TppEquip.AM_10403|R-MAGNUM|
    2|TppEquip.AM_10404|R-MAGNUM S-LOADER |Reload Speed Up
    2|TppEquip.AM_10405|R-MAGNUM +P|Reload Speed Up
    2|TppEquip.AM_10407|R-MAGNUM +P+|Reload Speed Up
    2|TppEquip.AM_10503|12GA SHELL|
    2|TppEquip.AM_10515|12GA SHELL (SLUG)|
    2|TppEquip.AM_10526|12A SHELL (AIR-S)|
    2|TppEquip.AM_10603|GRENADE|
    2|TppEquip.AM_10615|GRENADE (SMOKE)|
    2|TppEquip.AM_10626|GRENADE(STUN)|
    2|TppEquip.AM_10637|GRENADE (SLEEP)|
    2|TppEquip.AM_10703|WATER|
    2|TppEquip.AM_10704|WATER (HP)|
    2|TppEquip.AM_10705|WATER (UHP)|
    2|TppEquip.AM_20002|SMG MAG x20|
    2|TppEquip.AM_20003|SMG MAG x30|Long Magazine 1 (Loaded Ammo Count Up)
    2|TppEquip.AM_20005|SMG LONG-MAG x40|Long Magazine 2 (Loaded Ammo Count Up)
    2|TppEquip.AM_20103|SMG MAG x20|
    2|TppEquip.AM_20104|SMG MAG x30|Long Magazine 1 (Loaded Ammo Count Up)
    2|TppEquip.AM_20105|SMG DUAL-MAG x30|Dual Magazine (Reload Speed Up)
    2|TppEquip.AM_20106|SMG LONG-MAG x40|Long Magazine 2 (Loaded Ammo Count Up)
    2|TppEquip.AM_20116|10 DUAL-MAG x30|Dual Magazine (Reload Speed Up)
    2|TppEquip.AM_20116_0|10 MAG x20|
    2|TppEquip.AM_20116_1|10 LONG-MAG x30|Long Magazine 1 (Loaded Ammo Count Up)
    2|TppEquip.AM_20203|SMG MAG x30|
    2|TppEquip.AM_20206|SMG DUAL-MAG x30|Dual Magazine (Reload Speed Up)
    2|TppEquip.AM_20302|SMG MAG x20 (STUN)|
    2|TppEquip.AM_20303|SMG MAG x30 (STUN)|Long Magazine 1 (Loaded Ammo Count Up)
    2|TppEquip.AM_20304|SMG DUAL-MAG x30 (STUN)|Dual Magazine (Reload Speed Up)
    2|TppEquip.AM_20305|SMG LONG-MAG x40 (STUN)|Long Magazine 2 (Loaded Ammo Count Up)
    2|TppEquip.AM_30001|5.56 MAG x30|
    2|TppEquip.AM_30003|5.56 DUAL-MAG x30|Dual Magazine (Reload Speed Up)
    2|TppEquip.AM_30014|7.62 DUAL-MAG x30|Dual Magazine (Reload Speed Up)
    2|TppEquip.AM_30034|7.62 MAG x30|
    2|TppEquip.AM_30043|5.56 LONG-MAG x40|Long Banana Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_30047|5.56 DRUM-MAG x75|5.56mm Drum Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_30054|7.62 LONG-MAG x40|Long Banana Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_30055|7.62 DRUM-MAG x75|Drum Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_30102|5.56 MAG-U x30|
    2|TppEquip.AM_30103|5.56 DUAL-MAG-U x30|Dual Magazine (Reload Speed Up)
    2|TppEquip.AM_30123|5.56 LONG-MAG-U x40|Extended Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_30125|5.56 DRUM-MAG x100|Drum Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_30201|7.62 MAG x20 |
    2|TppEquip.AM_30203|7.62 DUAL-MAG x20|Dual Magazine (Reload Speed Up)
    2|TppEquip.AM_30223|7.62 LONG-MAG x30|Long Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_30225|7.62 DRUM-MAG x50|Drum Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_30232|7.62 MAG x20 (STUN)|
    2|TppEquip.AM_30303|5.56 MAG-B x30|
    2|TppEquip.AM_30305|5.56 DUAL-MAG-B x30|Dual Magazine (Reload Speed Up)
    2|TppEquip.AM_30306|5.56 LONG-MAG-B x40|Extended Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_30325|9 MAG x30|
    2|TppEquip.AM_40001|12GA SHELL|
    2|TppEquip.AM_40004|12GA SHELL (MAGNUM)|
    2|TppEquip.AM_40012|12GA SHELL (SLUG)|
    2|TppEquip.AM_40015|12GA SHELL (S-SLUG)|
    2|TppEquip.AM_40023|12GA SHELL (AIR-S)|
    2|TppEquip.AM_40102|12GA SHELL|
    2|TppEquip.AM_40105|12GA S-LOADER|
    2|TppEquip.AM_40115|12GA SHELL (SLUG)|
    2|TppEquip.AM_40123|12GA SHELL (AIR-S)|
    2|TppEquip.AM_40126|12GA SHELL (AIR-S)|
    2|TppEquip.AM_40133|12GA SHELL|
    2|TppEquip.AM_40135|12GA SHELL|
    2|TppEquip.AM_40136|12GA SHELL|
    2|TppEquip.AM_40143|12GA SHELL|
    2|TppEquip.AM_40203|12GA MAG x6|
    2|TppEquip.AM_40204|12GA LONG-MAG x9|Long Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_40206|12GA DRUM-MAG x20|Drum Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_40304|12GA SHELL|
    2|TppEquip.AM_50002|40mmG|
    2|TppEquip.AM_50015|40mmG (SMOKE)|
    2|TppEquip.AM_50026|40mmG (STUN)|
    2|TppEquip.AM_50047|40mmG (SLEEP)|
    2|TppEquip.AM_50033|40mmG|
    2|TppEquip.AM_50035|40mmG|
    2|TppEquip.AM_50102|40mmG|
    2|TppEquip.AM_50115|40mmG (SMOKE)|
    2|TppEquip.AM_50126|40mmG (STUN)|
    2|TppEquip.AM_50147|40mmG (SLEEP)|
    2|TppEquip.AM_50136|40mmG (R-HE)|
    2|TppEquip.AM_50202|40mmG|
    2|TppEquip.AM_50215|40mmG (SMOKE)|
    2|TppEquip.AM_50226|40mmG (STUN)|
    2|TppEquip.AM_50237|40mmG (SLEEP)|
    2|TppEquip.AM_50303|25mmG MAG x6|
    2|TppEquip.AM_50304|25mmG L-MAG x10|Long Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_50306|25mmG D-MAG x20|Drum Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_60001|.308 MAG x5|5-round Magazine
    2|TppEquip.AM_60007|.338 MAG x5|
    2|TppEquip.AM_60013|ANEST.308 MAG x5|
    2|TppEquip.AM_60102|.308 MAG x5|5-round Magazine
    2|TppEquip.AM_60107|.338 MAG x4|
    2|TppEquip.AM_60114|ANEST.308 MAG x5|
    2|TppEquip.AM_60203|.308 MAG x8|8-round Magazine
    2|TppEquip.AM_60303|.308 MAG x20|
    2|TppEquip.AM_60315|.223 MAG x20|
    2|TppEquip.AM_60325|ANEST.308 MAG x20|
    2|TppEquip.AM_60404|AP12.7 MAG x5|
    2|TppEquip.AM_60406|AP12.7 LONG-MAG x10|Extended Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_60415|AP12.7 MAG x5|
    2|TppEquip.AM_60417|AP12.7 LONG-MAG x10|Extended Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_70002|7.62 H-MAG x100|
    2|TppEquip.AM_70003|7.62 H-MAG x150|150-round Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_70005|7.62 H-MAG x200|200-round Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_70103|5.56 S-MAG x100|
    2|TppEquip.AM_70104|5.56 S-MAG x150|150-round Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_70105|5.56 S-MAG x200|200-round Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_70114|7.62 S-MAG x100|
    2|TppEquip.AM_70115|7.62 S-MAG x150|150-round Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_70116|7.62 S-MAG x200|200-round Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_70203|7.62 R-MAG x100|
    2|TppEquip.AM_70204|7.62 R-MAG x150|150-round Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_70205|7.62 R-MAG x200|200-round Magazine (Loaded Ammo Count Up)
    2|TppEquip.AM_80002|HEAT-I RG|
    2|TppEquip.AM_80004|HEAT-II RG|
    2|TppEquip.AM_80006|HEAT-III RG|
    2|TppEquip.AM_80103|MEM-84|
    2|TppEquip.AM_80104|MEM-84 |
    2|TppEquip.AM_80105|MEM-84 |
    2|TppEquip.AM_80116|MEM-84 (SLEEP)|
    2|TppEquip.AM_80124|MEM-84 (HE-1)|
    2|TppEquip.AM_80125|MEM-84 (HE-2)|
    2|TppEquip.AM_80126|MEM-84 (HE-3)|
    2|TppEquip.AM_80203|TCS-M|
    2|TppEquip.AM_80204|TCS-M VER.2|
    2|TppEquip.AM_80205|TCS-M VER.3|
    2|TppEquip.AM_80206|TCS-M VER.4|
    2|TppEquip.AM_80303|CG-M|
    2|TppEquip.AM_80304|CG-M MK.II|
    2|TppEquip.AM_80305|CG-M MK.III|
    2|TppEquip.AM_80306|CG-M MK.IV|
    2|TppEquip.AM_SkullFace_hg_010|R-MAGNUM|
    2|TppEquip.AM_SP_hg_010|R-MAGNUM|
    2|TppEquip.AM_SP_hg_020|.45 MAG x7|
    2|TppEquip.AM_SP_sm_010|SMG MAG x30|
    2|TppEquip.AM_SP_sg_010|12GA SHELL|

###<a name="3">3 - Stock</a>
type|script name|real name|options
-----|-----|-----|-----
    3|TppEquip.SK_20002|Sz.-336 STOCK|Standard Stock 1
    3|TppEquip.SK_20015|Sz.-336 SLIDESTOCK|Standard Stock 2 (Improved Stability While Moving)
    3|TppEquip.SK_20103|ZEEV STOCK|Standard Stock 1
    3|TppEquip.SK_20106|ZEEV RRS-STOCK|Standard Stock 2 (Improved Stability While Moving)
    3|TppEquip.SK_20203|MACHT 37 STOCK|"Sharpshooters Stock 1"
    3|TppEquip.SK_20216|MACHT 37 AD-STOCK|"Sharpshooters Stock 2 (Improved Stability While Moving)"
    3|TppEquip.SK_30001|SVG TYPE STOCK|Standard Stock 1
    3|TppEquip.SK_30002|SVG TYPE SK-STOCK|Standard Stock 2 (Improved Stability While Moving)
    3|TppEquip.SK_30024|SVG TYPE PR-STOCK|Standard Stock 3 (Improved Stability While Moving)
    3|TppEquip.SK_30043|SVG TYPE FS-STOCK|LMG Stock 1 (Improved Stability While Moving)
    3|TppEquip.SK_30045|SVG TYPE F2-STOCK|LMG Stock 2 (Improved Stability While Moving)
    3|TppEquip.SK_30102|MRS TYPE STOCK|Standard Stock 1
    3|TppEquip.SK_30113|MRS TYPE AD-STOCK|"Sharpshooters Stock 1 (Improved Stability While Moving)"
    3|TppEquip.SK_30123|MRS TYPE FS-STOCK|LMG Stock 1 (Improved Stability While Moving)
    3|TppEquip.SK_30201|ARC TYPE AD-STOCK|"Sharpshooters Stock 1"
    3|TppEquip.SK_30205|ARC TYPE A2-STOCK|"Sharpshooters Stock 2 (Improved Stability While Moving)"
    3|TppEquip.SK_30213|ARC TYPE STOCK|Standard Stock 1
    3|TppEquip.SK_30223|ARC TYPE FS-STOCK|LMG Stock 1 (Improved Stability While Moving)
    3|TppEquip.SK_40001|RASP STOCK2|
    3|TppEquip.SK_40043|RASP SAWED-OFF|
    3|TppEquip.SK_40102|S1000 STOCK|Standard Stock 1
    3|TppEquip.SK_40144|S1000 SK-STOCK|Standard Stock 2 (Improved Stability While Moving)
    3|TppEquip.SK_40203|KAB83 STOCK|Standard Stock 1
    3|TppEquip.SK_40306|BULL-H STOCK|
    3|TppEquip.SK_50002|FAKEL STOCK|Standard Stock 1
    3|TppEquip.SK_50004|FAKEL SK-STOCK|Standard Stock 2 (Improved Stability While Moving)
    3|TppEquip.SK_50102|DGL103 STOCK|Standard Stock 1
    3|TppEquip.SK_50202|RGL-220 STOCK|Standard Stock 1
    3|TppEquip.SK_50303|HAIL STOCK|"Sharpshooters Stock 1"
    3|TppEquip.SK_60001|RENOV STOCK|
    3|TppEquip.SK_60002|RENOV SK-STOCK|"Sharpshooters Stock 2 (Improved Stability While Moving)"
    3|TppEquip.SK_60102|M2000 STOCK|
    3|TppEquip.SK_60103|M2000 AD-STOCK|"Sharpshooters Stock 2 (Improved Stability While Moving)"
    3|TppEquip.SK_60203|BAMBETOV STOCK|"Sharpshooters Stock 1"
    3|TppEquip.SK_60205|BAMBETOV AD-STOCK|"Sharpshooters Stock 2 (Improved Stability While Moving)"
    3|TppEquip.SK_60303|MRS TYPE STOCK2|"Sharpshooters Stock 1"
    3|TppEquip.SK_60304|MRS TYPE AD-STOCK2|"Sharpshooters Stock 2 (Improved Stability While Moving)"
    3|TppEquip.SK_60405|BRENNAN STOCK|
    3|TppEquip.SK_70103|AAM STOCK|LMG Stock
    3|TppEquip.SK_70203|LPG-61 STOCK|LMG Stock
    
###<a name="4">4 - Muzzle</a>
type|script name|real name|options
-----|-----|-----|-----
    4|TppEquip.MZ_30001|SVG TYPE MUZZLE|Normal Barrel Muzzle
    4|TppEquip.MZ_30023|SVG TYPE F-HIDER|Muzzle for Short Barrel
    4|TppEquip.MZ_30102|MRS TYPE MUZZLE|Normal Barrel Muzzle
    4|TppEquip.MZ_30105|MRS TYPE S-MUZZLE|Muzzle for Short Barrel
    4|TppEquip.MZ_30123|MRS TYPE FS-MUZZLE|Muzzle for LMG Barrel
    4|TppEquip.MZ_30201|ARC TYPE MUZZLE|Normal Barrel Muzzle
    4|TppEquip.MZ_30213|ARC TYPE S-MUZZLE|Muzzle for Short Barrel
    4|TppEquip.MZ_30223|ARC TYPE FS-MUZZLE|Muzzle for LMG Barrel
    4|TppEquip.MZ_30232|ARC TYPE NL-MUZZLE|Normal Barrel Muzzle
    4|TppEquip.MZ_30303|G44 TYPE MUZZLE|Normal Barrel Muzzle
    4|TppEquip.MZ_40102|S1000 C-MUZZLE|Normal Barrel Muzzle
    4|TppEquip.MZ_40203|KAB83 C-MUZZLE|Normal Barrel Muzzle
    4|TppEquip.MZ_40206|KAB83 F-HIDER|Flash Hider
    4|TppEquip.MZ_40304|BULL-H C-MUZZLE|Normal Barrel Muzzle
    4|TppEquip.MZ_60001|RENOV MUZZLE|Normal Barrel Muzzle
    4|TppEquip.MZ_60102|M2000 MUZZLE|Normal Barrel Muzzle
    4|TppEquip.MZ_60105|M2000 B-MUZZLE|Muzzle for High-accuracy Barrel
    4|TppEquip.MZ_60203|BAMBETOV MUZZLE|Normal Barrel Muzzle
    4|TppEquip.MZ_60303|MRS TYPE MUZZLE2|Normal Barrel Muzzle
    4|TppEquip.MZ_60305|MRS TYPE B-MUZZLE|Normal Barrel Muzzle
    4|TppEquip.MZ_60404|AMR TYPE MUZZLE|Normal Barrel Muzzle
    4|TppEquip.MZ_60405|AMR TYPE HP-MUZZLE|Muzzle for High-accuracy Barrel
    4|TppEquip.MZ_60416|AMR TYPE HH-MUZZLE|Muzzle for High-accuracy Barrel
    4|TppEquip.MZ_70002|ALM 48 MUZZLE|Normal Barrel Muzzle
    4|TppEquip.MZ_70103|AAM MUZZLE|Normal Barrel Muzzle
    4|TppEquip.MZ_70106|AAM S-MUZZLE|Muzzle for Short Barrel
    4|TppEquip.MZ_70203|LPG-61 MUZZLE|Normal Barrel Muzzle
    4|TppEquip.MZ_70207|LPG-61 S-MUZZLE|Muzzle for Short Barrel

###<a name="5">5 - Muzzle options</a>
type|script name|real name|options
-----|-----|-----|-----
    5|TppEquip.MO_10101|SUP. PISTOL (R1)|Suppressor (Durability: Low)
    5|TppEquip.MO_10105|SUP. PISTOL-S (R4)|
    5|TppEquip.MO_10002|SUP. PISTOL (R1B)|Suppressor (Durability: Low)
    5|TppEquip.MO_10004|SUP. PISTOL-D (R2)|Suppressor (Durability: Medium)
    5|TppEquip.MO_10026|MUZZLE-OP D114|Compensator (Closer Shot Grouping)
    5|TppEquip.MO_10202|SUP. PISTOL-B (R1)|Suppressor (Durability: Low)
    5|TppEquip.MO_10205|SUP. PISTOL-B (R4)|
    5|TppEquip.MO_10306|MUZZLE-OP GEIST|
    5|TppEquip.MO_10407|COUNTER-W S333 |
    5|TppEquip.MO_10425|MUZZLE-OP S362SB|
    5|TppEquip.MO_20002|SUP. SMG-Sz. (R1)|Suppressor (Durability: Low)
    5|TppEquip.MO_20005|SUP. SMG-Sz. (R2)|Suppressor (Durability: Medium)
    5|TppEquip.MO_20006|MUZZLE-OP Sz.|Recoil Dampening Muzzle (Closer Shot Grouping)
    5|TppEquip.MO_20204|SUP. SMG (R1)|Suppressor (Durability: Low)
    5|TppEquip.MO_20205|SUP. SMG-MACHT (R2)|Suppressor (Durability: Medium)
    5|TppEquip.MO_20206|SUP. SMG-MACHT (R3)|Suppressor (Durability: High)
    5|TppEquip.MO_20302|SUP. SMG-RIOT (R1)|Suppressor (Durability: Low)
    5|TppEquip.MO_20307|SUP. SMG-RIOT (R2)|Suppressor (Durability: Medium)
    5|TppEquip.MO_30002|MUZZLE-OP SVG (A)|Recoil Dampening Muzzle (Closer Shot Grouping)
    5|TppEquip.MO_30005|MUZZLE-OP SVG (B)|Compensator (Closer Shot Grouping)
    5|TppEquip.MO_30046|MUZZLE-OP PG (A)|Compensator (Closer Shot Grouping)
    5|TppEquip.MO_30025|MUZZLE-OP PG (B)|Muzzle Brake (Closer Shot Grouping)
    5|TppEquip.MO_30102|SUP. GP-W (R1)|Suppressor (Durability: Low)
    5|TppEquip.MO_30105|SUP. GP-W (R2)|Suppressor (Durability: Medium)
    5|TppEquip.MO_30115|MUZZLE-OP MRS|Recoil Dampening Muzzle (Closer Shot Grouping)
    5|TppEquip.MO_30117|SUP. GP-W (R3)|Suppressor (Durability: High)
    5|TppEquip.MO_30205|MUZZLE-OP ARC|Recoil Dampening Muzzle (Closer Shot Grouping)
    5|TppEquip.MO_30235|SUP. AR-ARC (R1)|Suppressor (Durability: Low)
    5|TppEquip.MO_30237|SUP. AR-ARC (R2)|Suppressor (Durability: Medium)
    5|TppEquip.MO_40104|SUP. SG-S1000 (R1)|Suppressor (Durability: Low)
    5|TppEquip.MO_40106|SUP. SG-S1000 (R2)|Suppressor (Durability: Medium)
    5|TppEquip.MO_40306|MUZZLE-OP BULLHORN|Compensator (Closer Shot Grouping)
    5|TppEquip.MO_60103|SUP. GP-W (R1B)|Suppressor (Durability: Low)
    5|TppEquip.MO_60106|SUP. GP-W (R2B)|Suppressor (Durability: Medium)
    5|TppEquip.MO_60204|SUP. SR-SV (R1)|Suppressor (Durability: Low)
    5|TppEquip.MO_60206|MUZZLE-OP BAMBETOV|High-power Muzzle Brake (Closer Shot Grouping)
    5|TppEquip.MO_60406|SUP. AMR (R1)|Suppressor (Durability: Low)
    5|TppEquip.MO_70025|MUZZLE-OP ALM|Recoil Dampening Muzzle (Closer Shot Grouping)
    
###<a name="6">6 and 7 - first and second sights</a> 
type|script name|real name|options
-----|-----|-----|-----
    6|TppEquip.ST_20104|DOT SIGHT I|Dot Sight 1
    6|TppEquip.ST_20205|DOT SIGHT III|Dot Sight 3
    6|TppEquip.ST_30114|DOT SIGHT II|Dot Sight 2
    6|TppEquip.ST_30202|BOOSTER (2x)|2x Booster (Magnifier)
    6|TppEquip.ST_30204|BOOSTER VM (2-4x)|4x Variable Zoom Booster (Magnifier/2-step)
    6|TppEquip.ST_30303|G44 SCOPE (2x)|2x Fixed Scope
    6|TppEquip.ST_30305|SHORT SCOPE (3x)|3x Short Scope
    6|TppEquip.ST_30306|NV SCOPE|Night Vision Scope
    6|TppEquip.ST_50003|RANGE-FINDER E (3x)|3x Rangefinding Scope (Soviet)
    6|TppEquip.ST_50133|RANGE-FINDER W (3x)|3x Rangefinding Scope (U.S.)
    6|TppEquip.ST_50136|RANGE-FINDER (2-6x)|6x Variable Zoom Rangefinding Scope (U.S./2-step)
    6|TppEquip.ST_50303|RANGE-FINDER SP (3x)|3x Rangefinding Scope
    6|TppEquip.ST_60001|RIFLE SCOPE E (4x)|4x Rifle Scope (Soviet 1)
    6|TppEquip.ST_60004|RIFLE SCOPE (2-8x)|8x Variable Zoom Rifle Scope 1 (3-step)
    6|TppEquip.ST_60102|RIFLE SCOPE W (4x)|4x Rifle Scope (U.S. 1)
    6|TppEquip.ST_60105|RF SCOPE (2-8x)|8x Variable Zoom Rangefinding Rifle Scope (3-step)
    6|TppEquip.ST_60203|RIFLE SCOPE E2 (4x)|4x Rifle Scope (Soviet 2)
    6|TppEquip.ST_60303|RIFLE SCOPE W2 (4x)|4x Rifle Scope (U.S. 2)
    6|TppEquip.ST_60304|VM SCOPE (2-6x)|6x Variable Zoom Rifle Scope (U.S./2-step)
    6|TppEquip.ST_60407|VM SCOPE (4-8x)|8x Variable Zoom Rifle Scope 2 (3-step)
    6|TppEquip.ST_80002|GROM-11 O-SIGHT|
    6|TppEquip.ST_80103|FB MR O-SIGHT|
    6|TppEquip.ST_80203|GUIDED SCOPE-S|
    6|TppEquip.ST_80303|GUIDED SCOPE-M|

###<a name="8">8 and 9 - Lasers/Flashlights</a>
type|script name|real name|options
-----|-----|-----|-----
    8|TppEquip.LT_10102|COMPACT F-LIGHT|Flashlight
    8|TppEquip.LT_10104|FLASH-LASER MODULE|Flashlight + Laser Sight
    8|TppEquip.LT_30025|FLASH-LIGHT ST|Flashlight (Soviet)
    8|TppEquip.LT_30105|FLASH-LIGHT CB|Flashlight (U.S. 1)
    8|TppEquip.LT_40103|FLASH-LIGHT TA|Flashlight (U.S. 2)
    8|TppEquip.LS_10415|COMPACT LASER-M 1|Laser Sight 1
    8|TppEquip.LS_20004|COMPACT LASER-M 2|Laser Sight 2
    8|TppEquip.LS_30104|LASER-A-MODULE CB|Laser Sight (U.S. 1)
    8|TppEquip.LS_40034|LASER-A-MODULE TA|Laser Sight (U.S. 2)

###<a name="10">10 - underbarrels and foregrips</a>
type|script name|real name|options
-----|-----|-----|-----
    10|TppEquip.UB_20105|V-FOREGRIP|Foregrip (Improved Stability While Moving)
    10|TppEquip.UB_30005|S-FOREGRIP|Foregrip (Soviet/Improved Stability While Moving)
    10|TppEquip.UB_30105|M-FOREGRIP|Foregrip (U.S./Improved Stability While Moving)
    10|TppEquip.UB_30304|F-FOREGRIP|Foregrip (European/Improved Stability While Moving)
    10|TppEquip.UB_10006|D114 UDBL-CB|
    10|TppEquip.UB_10107|S.P UDBL-CB|
    10|TppEquip.UB_10207|GEIST UDBL-CB|
    10|TppEquip.UB_40043|RASP UDBL-SG|
    10|TppEquip.UB_40045|RASP UDBL-SG+P|Magnum Shotshell Conversion (Damage Up)
    10|TppEquip.UB_40144|S1000 UDBL-SG|
    10|TppEquip.UB_50002|FAKEL UDBL-GL|
    10|TppEquip.UB_50015|FAKEL UDBL-GL (SMO)|Smoke Round Conversion (Attack Type: Non-lethal)
    10|TppEquip.UB_50026|FAKEL UDBL-GL (STN)|Stun Round Conversion (Attack Type: Non-lethal)
    10|TppEquip.UB_50047|FAKEL UDBL-GL (SLE)|Sleeping Gas Round Conversion (Attack Type: Non-lethal)
    10|TppEquip.UB_50033|FAKEL UDBL-GL II|
    10|TppEquip.UB_50035|FAKEL UDBL-GL III|
    10|TppEquip.UB_50102|DGL UDBL-GL|
    10|TppEquip.UB_50115|DGL UDBL-GL (SMO)|Smoke Round Conversion (Attack Type: Non-lethal)
    10|TppEquip.UB_50126|DGL UDBL-GL (STN)|Stun Round Conversion (Attack Type: Non-lethal)
    10|TppEquip.UB_50147|DGL UDBL-GL (SLE)|Sleeping Gas Round Conversion (Attack Type: Non-lethal)
    10|TppEquip.UB_50133|DGL UDBL-GL-L|
    10|TppEquip.UB_50136|DGL UDBL-GL-LR|
