def harvest_all():
	move_to_start()
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			harvest()
			move(North)
		move(East)

def plant_random():
	list = [Entities.Bush, Entities.Carrots, Entities.Grass, Entities.Pumpkin, Entities.Sunflower, Entities.Tree]
	index = random() * len(list) // 1
	return plant(list[index])
	
def buy_items_if_needed():
	items = [Items.Carrot_Seed, Items.Fertilizer, Items.Pumpkin_Seed, Items.Sunflower_Seed]
	max_needed = get_world_size() * get_world_size()
	for item in items:
		trade(item, max_needed - num_items(item))