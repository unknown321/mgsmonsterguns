# mgsmonsterguns

How does an MGSV weapon work?
Every customizable weapon consists of parts (using URAGAN-5P SLUG as example):

    type| id | localized string | description | notes
    ---|--------|----------|-------------|------
    **Main**|
    -|TppEquip.WP_10515|weapon id| self-explanatory|
    0|TppEquip.RC_10515|URAGAN SG-FRAME| frame with open slots, usually one per gun grade|
    1|TppEquip.BA_10504|URAGAN-5P L-BARREL| gun barrel, duh| 
    **Optional**|
    2|TppEquip.AM_10515|12GA SHELL (SLUG)| ammo type |
    3|TppEquip.SK_None|-| stock | 
    4|TppEquip.MZ_None|-| muzzle| attachable to barrel
    5|TppEquip.MO_None|-| muzzle option | attachable to barrel
    6|TppEquip.ST_20104|DOT SIGHT I|Scope (Upper Option Slot) | attachable to barrel
    7|TppEquip.ST_None|-| Second scope slot
    8|TppEquip.LT_10102|COMPACT F-LIGHT| Laser Sight 1 | attachable to barrel
    9|TppEquip.LT_None|-| Laser Sight 2 | attachable to barrel
    10|TppEquip.UD_None|-| Underbarrel/foregrip | attachable to barrel


These predefined parameters for each gun can be found in file `\master\0\00\Assets\tpp\level_asset\weapon\ParameterTables\parts\EquipParameters.lua` and vary from gun to gun (TppEquip.UD_None can be substituted by UB_None for example); color is not included. 
Note that some parameters are None by default - it means that frame used in this weapon doesn't allow changes in these slots.

If your gun's frame has litte to none open slots (marked red ingame), you can try to change the frame to another one with more options. However it may crash the game or hang it.

#Open slots

Let's say we want to change options for open slots such as scope. There are two ways of doing so:
* Changing it in `\master\0\00\Assets\tpp\level_asset\weapon\ParameterTables\parts\EquipParameters.lua` to another one. 
	* Pros: you will change every gun in the game including those that guards carry
	* Cons: small variety, you cannot select other scopes in game
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
This code adds 6 allowed scopes (partsType=6) to URAGAN-SG, but we definitely need more. Feel free to expand that list with any scopes from the [table below](#tables). Save the file, make a new customized gun, choose from gorillion scopes. ![Scopes](https://0x0.st/PWR.jpg)


#Closed slots
Closed slots are cannot be changed via ingame interface at all, so you will need to modify them in lua scripts (or change the gun frame to another one with more slots).

Changing barrel: changes fine ![New barrel](https://0x0.st/PWg.jpg)

##Changing frame
Changing frame may cause crashes, hangs etc.

Open `\master\0\00\Assets\tpp\level_asset\weapon\ParameterTables\parts\EquipParameters.lua`, find your gun's frame - `RC_10515` for URAGAN-SG, replace it with another frame from the [table below](#tables).

Changing frame to ZORN: open slots are changed according to a new frame (no modifications allowed) saving previous options (optics and flashlights) ![New frame](https://0x0.st/PWx.jpg)

Changing frame to RASP SG+P with more slots, game hangs on sortie prep: ![New frame](https://0x0.st/PWE.jpg)

##Changing closed slots
Open `\master\0\00\Assets\tpp\level_asset\weapon\ParameterTables\parts\EquipParameters.lua`, find your gun's frame - `RC_10515` for URAGAN-SG, replace stuff below the line with the frame - TppEquip.SK_, TppEquip.MZ_ etc. with anything you want from the [tables below](#tables), save the file, make a new customized gun, the end. Save your gun, revert changes in file. 

Changing muzzle for a Bambetov one (MZ_60203) - ![New muzzle](https://0x0.st/PW7.jpg)

#Notes
Adding lethal ammo to non-lethal guns won't work (by adding more entries).

If you cannot see your guns on sortie prep or in ACC - this is a bad sign.

Changing frame usually leads to invisible guns (see above).

Changing gas pistol components leads to nothing. Looks like it cannot be changed because reasons.

#Tables

Tables are huge so I moved them to another page - http://unknown321.github.io/mgsmonsterguns/ along with this readme.
