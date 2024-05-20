def move_to_pos(x,y):
	move_to_x(x)
	move_to_y(y)
def move_to_y(y):
	while get_pos_y() != y:
		if y > get_pos_y():
			move(North)
		else:
			move(South)
def move_to_x(x):
	while get_pos_x() != x:
		if x > get_pos_x():
			move(East)
		else:
			move(West)
def move_to_start():
	move_to_pos(0,0)