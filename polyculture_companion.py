move_to_start()
harvest_all()
move_to_start()
while True:
	#buy seeds if needed
	buy_items_if_needed()
	# companionPlant
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			move_to_pos(x,y)
			use_item(Items.Water_Tank)
			entity = get_entity_type()
			if entity == None:
				use_item(Items.Fertilizer)
				plant_random()
			companion = get_companion()
			if companion != None:
				move_to_pos(companion[1],companion[2])
				if get_entity_type() == None:
					use_item(Items.Fertilizer)
					plant(companion[0])
	move_to_start()
	harvest_all()