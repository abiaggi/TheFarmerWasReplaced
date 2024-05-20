#Taken from this post https://steamcommunity.com/app/2060160/discussions/0/3775742435235781730/

def checked_move(dir):
	x = get_pos_x()
	y = get_pos_y()
	move(dir)
	if get_pos_x() == x and get_pos_y() == y:
		return False
	else:
		return True
def turn_left(dir):
	if dir == North:
		return West
	if dir == East:
		return North
	if dir == South:
		return East
	if dir == West:
		return South
def turn_right(dir):
	if dir == North:
		return East
	if dir == East:
		return South
	if dir == South:
		return West
	if dir == West:
		return North
def plant_maze():
	success = False
	while success == False:
		plant(Entities.Bush)
		if num_items(Items.Fertilizer) == 0:
			trade(Items.Fertilizer)
		use_item(Items.Fertilizer)
		if checked_move(South):
			move(North)
		else:
			success = True
def maze_solver():
	dir = North
	while get_entity_type() != Entities.Treasure:	
		dir = turn_right(dir)
		success = checked_move(dir)
		if success == False:
			dir = turn_left(dir)
		success = checked_move(dir)
		if success == False:
			dir = turn_left(dir)
		else:
			dir = turn_right(dir)
			success = checked_move(dir)
			if success == False:
				dir = turn_left(dir)
	harvest()