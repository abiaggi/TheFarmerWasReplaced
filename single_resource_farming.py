ENTITY = Entities.Grass
SEED = None
WATER_LEVEL = 0.25
move_to_start()
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			if get_water() < WATER_LEVEL:
				use_item(Items.Water_Tank)
			if SEED != None:
				if num_items(SEED) < 1:
					trade(SEED)
			plant(ENTITY)
			move(North)
		move(East)