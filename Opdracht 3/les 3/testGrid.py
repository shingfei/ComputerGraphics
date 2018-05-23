from grid import *

g = Grid(20, 10)
g.addPoint(1, 1)
for x in range(3, 17):
    g.addPoint(x, 3)
g.addPoint(19, 9)
g.addPoint(4, 5, .5)
g.addPoint(10, 7, (0, .5, 1))
g.draw()
