from grid import *
#Door Shingfei Lam 0915328
#Niet helemaal werkend, alleen dalen werkt
grid = Grid (20,10)

def rasterline(x1,y1,x2,y2):
	
	dx = x2-x1
	dy = y2-y1
	
	#Functie om te checken of het op dezelfde pixel valt
	if x1 == x2 and y1 == y2:
		grid.addPoint(x1,y1)
		print('gelijk')
	
	elif dx < 0:
		x1 = x2
		for y3 in range (y1, y2+1):
			grid.addPoint(x1, y3)
	
	elif dy <0:
		y1 = y2
		for x3 in range (x1, x2+1):
			grid.addPoint(x3, y1)		
			
	elif abs(dy)< abs(dx):#lijn gaat stijgen of blijft gelijk
		alpha = dy / dx
		yDifference = y1 - alpha * x1	

		for x3 in range(x1, x2+1):
			grid.addPoint(x3,(round(alpha*(x3-x1))+yDifference))
			
	else :#lijn gaat dalen
		alpha = dx / dy
		xDifference = x1 - alpha * y1

		for y3 in range(y1, y2+1):
			grid.addPoint(abs(round(alpha*(y3-y1))+xDifference),y3)
		
rasterline(10,2,4,5)
grid.draw()