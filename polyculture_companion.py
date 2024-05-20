def plant_compaion():
	companion = get_companion()
	if companion != None:
		move_to_pos(companion[1],companion[2])
		if get_entity_type() == None:
			use_item(Items.Fertilizer)
			plant(companion[0])
			use_item(Items.Water_Tank)
			plant_compaion()

harvest_reverse()
while True:
	buy_items_if_needed()
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			move_to_pos(x,y)
			entity = get_entity_type()
			if entity == None:
				use_item(Items.Fertilizer)
				plant_random()
				use_item(Items.Water_Tank)
				plant_compaion()
	harvest_all()