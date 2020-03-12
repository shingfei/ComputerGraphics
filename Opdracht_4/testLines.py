from lines import *

l = Lines(640, 480)
l.addLine((100, 100), (500, 300))
p = (100, 200)
for i in range(100, 600, 50):
    l.addLine(p, (i, 400))
l.draw()
