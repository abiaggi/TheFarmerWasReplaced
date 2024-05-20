# I'm pretty sure this is not the way to go, but it farms power to unlock drone speeds
move_to_start()
harvest_all()
while True:
	buy_items_if_needed()
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			move_to_pos(x,y)
			if can_harvest():
				harvest()
			plant(Entities.Sunflower)
			use_item(Items.Fertilizer)
			use_item(Items.Water_Tank)