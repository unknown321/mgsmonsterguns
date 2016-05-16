# -*- coding: utf-8 -*-
# import ConfigParser
# config = ConfigParser.ConfigParser()
import json
import re
import xml.etree.ElementTree as ET
from string import Template
# # tpp_weapon.eng
# # tpp_item.eng
# # tpp_parts.eng
  # text strings

# # WeaponPartsCombinationSettings
  # which parts can be attached to other parts

# # WeaponPartsUiSetting
  # descriptions for part, path to icon

# # EquipDevelopFlowSetting
  # resources and time needed for development

# # EquipDevelopConstSetting
  # order of development

# # ChimeraPartsPackageTable
  # which models are used for a gun, enumerate and assign

# # EquipParameters
  # predefined guns' parts for every gun and their magic parameters

keys = {"weapon":{'name':"WP_",'type':-1},
		"frame":{'name':"RC_",'type':0},
		"barrel":{'name':"BA_",'type':1},
		"magazine":{'name':"AM_",'type':2},
		"stock":{'name':"SK_",'type':3},
		"muzzle":{'name':"MZ_",'type':4},
		"muzzle_option":{'name':"MO_",'type':5},
		"sight":{'name':"ST_",'type':6},
		"flashlight":{'name':"LT_",'type':8},
		"laser_sight":{'name':"LS_",'type':8},
		"foregrip":{"name":"UB_",'type':10}}

def prepare_lua(filename, crop_left, crop_right):
	f = open(filename)
	t = f.read()
	f.close()
	t = t[crop_left:crop_right]	
	return t

def split_string(string):
	result = {}
	keys = ['barrelID','partsType','partsIds','receiverID']
	parts = re.split('[=|}|{|,]',string)
	section_name = ""
	for key in parts:
		if key in keys:
			# start filling key with values
			result[key] = []
			section_name = key
		elif key and section_name:
			# not in keys and not empty - it has to be a value
			if section_name == 'partsType':
				result[section_name] = key
			else:
				result[section_name].append(key)
	return result

def get_names():
	names_langid = [] 	 # the ones with langid property so we can assign them
	names_key = []		 # only fox32 keys, fixed by adding more strings to dictionary
	broken_elements = [] # no langid or key

	names = ["tpp_item.eng.lng2.xml","tpp_weapon.eng.lng2.xml","tpp_parts.eng.lng2.xml"]
	for name in names:
		tree = ET.parse(name)
		item_root = tree.getroot()
		for entry in item_root[0]:
			if "Key" in entry.keys():
				names_key.append({"key":entry.attrib['Key'], "value":entry.attrib['Value']})
			elif "LangId" in entry.keys():
				names_langid.append({"key":entry.attrib['LangId'], "value":entry.attrib['Value']})
			else:
				broken_elements.append(entry)

	return names_langid, names_key, broken_elements

def parse_lua_table(filename, crop_left, crop_right):
	# ChimeraPartsPackageTable
	# EquipParameters
	# {"key":[{1,2},{1,2}]}
	t = prepare_lua(filename, crop_left, crop_right)
	parts = t.split('}},')
	results = {}
	for part in parts:
		keyvalue = part.split('=')
		results[keyvalue[0]] = []
		# remove {{
		keyvalue[1] = keyvalue[1][2:]
		appended_stuff = keyvalue[1].split('},{')
		for i in appended_stuff:
			if i[-2:] == '}}':
				i = i[0:-2]
			# removes issues because of weird '1' number in the beginning
			if i[0:2] == ',{':
				i = i[2:]
			i = i.split(',')
			results[keyvalue[0]].append(i)
			# print i
	return results

def parse_more_lua(filename,crop_left,crop_right,split_str):
	# EquipDevelopFlowSetting
	# EquipDevelopConstSetting
	# WeaponPartsUiSetting
	# {p00=1e3,....,p36=0}
	t = prepare_lua(filename, crop_left, crop_right)
	entries = t.split(split_str)
	results = []
	if not entries[0]:
		entries.pop(0)
	for entry in entries:
		# remove {}
		entry = entry[1:-1]
		entry_parts = entry.split(',')
		real_entry = {}
		for e in entry_parts:
			e = e.split('=')
			e[1] = e[1].strip('"')
			real_entry[e[0]] = e[1]
		results.append(real_entry)
	return results

def parse_even_more_lua(filename, crop_left, crop_right, split_str):
	# WeaponPartsCombinationSettings
	# {"key":{type={},partsType=№,partsIds={1,2,3}}}
	# keys:
	# 'RegistPartsInclusionInfo_BarrelBase'
	# 'RegistPartsInclusionInfo'
	# 'RegistPartsInclusionInfo_ReceiverBase'
	# 'RegistPartsInclusionInfo_ReceiverWithUnderBarrellBase'
	t = prepare_lua(filename, crop_left,crop_right)
	parts = t.split(split_str)
	results = {}

	for part in parts:
		if part:
			i = part.index('{')
			data = part[i+1:-1]
			superdata = split_string(data)
			if results.has_key(part[0:i]):
				results[part[0:i]].append(superdata)
			else:
				results[part[0:i]] = []
				results[part[0:i]].append(superdata)
	return results

def get_name_by_string(string):
	names = filter(lambda y:y['key']==string, names_key)
	if names:
		return names[0]['value']
	else:
		return None

def get_part_by_string(string):
	names = filter(lambda y:y['partsID']==string, parts_info)
	if names:
		return names[0]['messageID']
	else:
		return None

def default_weps_with_wep_name():
	dev_constant = parse_more_lua('EquipDevelopConstSetting.lua',7,-11,'TppMotherBaseManagement.RegCstDev')
	weapons_without_names = []	# you cannot develop this item
	weapons_with_names = []
	weapons_without_keys = []	# no key->fox32str

	for i in parts_parameters['gunBasic']:
		weapon = {'parts':i, 'names':{"name":None}, 'costs':['TODO, EquipDevelopFlowSetting']}
		development_w = filter(lambda x:x['p01'] == i[0].replace('WP','EQP_WP'), dev_constant)
		if development_w:
			item_id = development_w[0]['p00']
			if 'e3' in item_id:
				item_id = item_id.replace('e3','000')
			if 'e4' in item_id:
				item_id = item_id.replace('e4','0000')
			parent_id = development_w[0]['p03']
			if 'e3' in parent_id:
				parent_id = parent_id.replace('e3','000')
			if 'e4' in parent_id:
				parent_id = parent_id.replace('e4','0000')
			name = get_name_by_string(development_w[0]['p06'])
			info = get_name_by_string(development_w[0]['p07'])
			icon = development_w[0]['p08']
			long_name = get_name_by_string(development_w[0]['p30'])
			weapon['item_id'] = item_id
			weapon['parent_id'] = parent_id
			weapon['type'] = development_w[0]['p02']
			weapon['info'] = info
			weapon['icon'] = icon
			weapon['long_name'] = long_name
			weapon['can_customize'] = 0
			if development_w[0].has_key('p32'):
				weapon['can_customize'] = development_w[0]['p32']
			if name:
				weapon.update({'names':{"name":name}})
				weapons_with_names.append(weapon)
			else:
				weapon['names'].update({"name":development_w[0]['p06']})
				weapons_without_keys.append(weapon)
		else:
			weapon['item_id'] = '-1'
			weapon['parent_id'] = '-2'
			weapon['names'].update({"name":i[0]})
			weapons_without_names.append(weapon)
	return (weapons_with_names, weapons_without_names, weapons_without_keys)

def default_weps_with_all_names():
	weps = default_weps_with_wep_name()
	for wep_category in weps:
		for weapon in wep_category:
			p = weapon['parts'][:]
			weapon['parts'] = {}
			for part in p:
				for key, value in keys.iteritems():
					if ('TppEquip.'+value['name'] in part) and ('None' not in part):
						if key != 'sight':
							# there can be 2 sights
							weapon['parts'][key] = part
							part_messageid = get_part_by_string(part)
							if part_messageid:
								part_name = get_name_by_string(part_messageid)
								if part_name:
									weapon['names'][key] = part_name
							else:
								weapon['names'][key] = part
						else:
							if not weapon['parts'].has_key('sight'):
								weapon['parts']['sight'] = []
								weapon['names']['sight'] = []
							weapon['parts']['sight'].append(part)
							part_messageid = get_part_by_string(part)
							if part_messageid:
								part_name = get_name_by_string(part_messageid)
								if part_name:
									weapon['names']['sight'].append(part_name)
				if part.isdigit():
					weapon['names']['grade'] = 'Grade ' + part
					weapon['parts']['grade'] = part
	return weps

def bullet_params():
	results = []
	for i in parts_parameters['bullet']:
		results.append({'partID':i[0],'works_with':i[12]})
	return results

def magazine_params():
	results = []
	bullet_p = bullet_params()
	works_with = None
	for i in parts_parameters['magazine']:
		b = filter(lambda x:x['partID'] == i[4], bullet_p)
		if b:
			works_with = b[0]['works_with']
		results.append({'partID':i[0],'magazine_size':i[2],'magazine_total':i[3],'bullet_type':i[4], 'works_with':works_with})

	return results

def parts_with_names():
	parts_info = parse_more_lua('WeaponPartsUiSetting.lua',7,-11,'TppMotherBaseManagement.RegistWeaponPartsInfo')
	for part in parts_info:
		part['partID'] = part.pop('partsID')
		part['icon'] = part.pop('ftexPath')
		part.pop('displayInfo')
		part['name'] = get_name_by_string(part.pop('messageID'))
		if not part['name']:
			part['name'] = part['partID']
		part['type'] = int(part['type'])
		for key in part.keys():
			if 'langPower' in key:
				if not part.has_key('abilities'):
					part['abilities'] = []
				if part[key]:
					ability_name = get_name_by_string(part[key])
					part['abilities'].append(ability_name)
				part.pop(key)
	magazine_p = magazine_params()
	for mag in magazine_p:
		p = filter(lambda x:x['partID'] == mag['partID'], parts_info)
		if p:
			mag.pop('partID')
			p[0]['stats'] = mag
	missing_parts = find_missing_parts(parts_info)
	for i in missing_parts:
		missing = {'partID':i,'icon':None,'name':i,'abilities':[]}
		for key, value in keys.iteritems():
			if value['name'] in i:
				missing['type'] = value['type']
		parts_info.append(missing)
	return parts_info

def open_slots():
	# horrible
	parts_comb_settings = parse_even_more_lua('WeaponPartsCombinationSettings.lua',7,-11,'TppMotherBaseManagement.')
	results = {}
	part_types = [{'name':'receiverID','type':0,'type_name':'Receiver'},
				  {'name':'barrelID','type':1,'type_name':'Barrel'}]

	for key, category in parts_comb_settings.iteritems():
		for receiver in category:
			for p in part_types:
				if p['name'] in receiver.keys():
					for part in receiver[p['name']]:
						if not results.has_key(part):
							results[part] = {"slots":[], 'names':{"part":None, 'slots':[],'receiver_type':p['type_name']},
											'receiver':part,'receiver_type':p['type']}
						results[part]['slots'].append(int(receiver['partsType']))
						for key in keys:
							if keys[key]['type'] == int(receiver['partsType']):
								results[part]['names']['slots'].append(key.capitalize())
						a = get_part_by_string(part)
						results[part]['names']['part'] = get_name_by_string(a)

					# horrible
					unique = []
					[unique.append(item) for item in results[part]['slots'] if item not in unique]
					results[part]['slots'] = unique

					unique = []
					[unique.append(item) for item in results[part]['names']['slots'] if item not in unique]
					results[part]['names']['slots'] = unique

	return results.values()

def find_missing_parts(parts_info):
	# parts which are appended to guns, but are not mentioned in WeaponPartsUiSetting
	missing_parts = []
	for weapon in sum(default_weps_with_all_names(),[]):
		for key, value in weapon['parts'].iteritems():
			if key not in ['weapon','grade']:
				if isinstance(value, list):
					for i in value:
						e = filter(lambda x:x['partID'] == i, parts_info)	
						if not e:
							if i not in missing_parts:
								missing_parts.append(i)
				else:
					e = filter(lambda x:x['partID'] == value, parts_info)
					if not e:
						if value not in missing_parts:
							missing_parts.append(value)
	return missing_parts

def generate_parent_relationships_v3():
	# I wanna vomit
	# all weapons have to be sorted properly!!
	relations = []
	weps = sum(default_weps_with_all_names(),[])
	
	i = 0
	while True:
		weps_with_parents = 0
		weps = sorted(weps, key=lambda y: (int(y['item_id']),), reverse=True )
		for weapon in weps:
			parent = find_parent(weapon['parent_id'],weps)
			if parent:
				weps_with_parents=+1
				# I am pretty sure this can be improved
				if has_more_children(weapon['item_id'],weps):
					pass
				else:
					if not parent.has_key('children'):
						parent['children'] = []
						
					parent['children'].append(weapon)
					weps.remove(weapon)
		i = i+1
		if weps_with_parents == 0:
			break
	return weps

def strip_parent(parent):
	for key in parent.keys():
		if key not in ['item_id','children','names','grade','parent_id', 'name','parts','weapon']:
			del parent[key]
		elif key == 'names':
			parent['name'] = parent['names']['name']
			del parent['names']
		elif key=='parts':
			parent['weapon'] = parent['parts']['weapon']
			parent['grade'] = int(parent['parts']['grade'])
			del parent['parts']
	return parent


def find_parent(parent_id, weps):
	r = None
	r = filter(lambda x:x['item_id']==parent_id, weps)
	if r:
		r = r[0]
	return r


def has_more_children(parent_id, weps):
	r = filter(lambda x:x['parent_id']==parent_id, weps)
	return len(r)

def process_children(u):
	u = strip_parent(u)
	if u.has_key('children'):
		for c in u['children']:
			c = strip_parent(c)
			process_children(c)

def write_to_json():
	osf = open('open_slots.json','w')
	a = sorted(open_slots(), key=lambda x:(x['receiver_type'],len(x['slots']),x['names']['part']))
	osf.write(json.dumps(a,indent=4))
	osf.close()

	def_wepsf = open('default_gun_components.json','w')
	def_wepsf.write(json.dumps(sum(default_weps_with_all_names(),[]),indent=4))
	def_wepsf.close()

	partsf = open('parts.json','w')
	a = sorted(parts_with_names(), key=lambda x:(x['type'],x['name']))
	partsf.write(json.dumps(a, indent=4))
	partsf.close()

	relationsf = open('relations.json','w')
	a = generate_parent_relationships_v3()
	for i in a:
		process_children(i)
	a = sorted(a, key=lambda x:x['item_id'])
	relationsf.write(json.dumps(a,indent=4))
	relationsf.close()

def move_json():
	import shutil
	shutil.copy('relations.json', '../js/relations.json')
	shutil.copy('open_slots.json', '../js/open_slots.json')
	shutil.copy('parts.json', '../js/parts.json')
	shutil.copy('default_gun_components.json', '../js/default_gun_components.json')

# parts_model_info = parse_lua_table('ChimeraPartsPackageTable.lua',44,-12)
# dev_constant = parse_more_lua('EquipDevelopConstSetting.lua',7,-11,'TppMotherBaseManagement.RegCstDev')
# dev_flow = parse_more_lua('EquipDevelopFlowSetting.lua',7,-11,'TppMotherBaseManagement.RegFlwDev')
# parts_comb_settings = parse_even_more_lua('WeaponPartsCombinationSettings.lua',7,-11,'TppMotherBaseManagement.')

parts_parameters = parse_lua_table('EquipParameters.lua',44,-12)
parts_info = parse_more_lua('WeaponPartsUiSetting.lua',7,-11,'TppMotherBaseManagement.RegistWeaponPartsInfo')
names_key, names_langid, broken_elements = get_names()
write_to_json()
move_json()