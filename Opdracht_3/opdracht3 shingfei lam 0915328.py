from grid import *
#Door Shingfei Lam 0915328
#Niet helemaal werkend, alleen dalen werkt

screen_width = 20
screen_height = 20
octant = [45,90,135,180,225,270,315,360]

grid = Grid (screen_width,screen_height)

def center_coords(x,y):
	return (round((x/2)),round((y/2)))

def start_line(x1,y1):
	pass

def end_line(x2,y2):
	pass

def draw_line(start,end):
	pass

def calculate_orientation(x1,x2,y1,y2):
	
	if x1 == x2:
		diff_x = x
	if y1 == y2:
		diff_y = y
	if x2 > x1 and y2 > y1:
		pass

	elif x2 > x1 and y2 < y1:
		pass
	elif x2 < x1 and y2 < y1:
		pass
	elif x2 < x1 and y2 > y1:
		pass
	


def check_rotation(degrees):
	remainder = abs(degrees) % 360
	if remainder != 0:
		return (degrees)
	else:
		return (degrees-(round(degrees/360)*degrees))

def orientation_line(degrees):
	orientation = check_rotation(degrees)
	
	if orientation <= octant[0]:
	
		# x = ((orientation/octant[0]))*x if (orientation/octant[0]) != 0 else x
		# y = y if (orientation/octant[0]) == 0 else  ((orientation/octant[0]))*y
		return (round(x),round(y))
	elif orientation <= octant[1]:
		pass
	elif orientation <= octant[2]:
		pass
	elif orientation <= octant[3]:
		pass
	elif orientation <= octant[4]:
		pass
	elif orientation <= octant[5]:
		pass
	elif orientation <= octant[6]:
		pass
	elif orientation <= octant[7]:
		pass

x ,y = (center_coords(screen_width,screen_height))
grid.addPoint(x,y)
x1 ,y1 = 14,14
x2, y2 = 16, 18


# for x in range(x, 15):
# 	grid.addPoint(x,y)

# for y in range(y,15):
# 	grid.addPoint(10,y)


grid.draw()