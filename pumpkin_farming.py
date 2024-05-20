def all_grown_planting():
	move_to_start()
	allGrown = True
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			canHarvest = can_harvest()
			if not canHarvest:
				if num_items(Items.Pumpkin_Seed) < 1:
					trade(Items.Pumpkin_Seed)
				use_item(Items.Water_Tank)
				plant(Entities.Pumpkin)
			allGrown = allGrown and canHarvest
			move(North)
		move(East)
	return allGrown

while True:
	if all_grown_planting():
		harvest()
		move_to_start()