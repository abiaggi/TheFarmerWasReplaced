while True:
	buy_items_if_needed()
	plant(Entities.Bush)
	while not can_harvest():
		do_a_flip()
	while get_entity_type() == Entities.Bush:
		use_item(Items.Fertilizer)
	if get_entity_type() != Entities.Bush:
		maze_solver()
		till()