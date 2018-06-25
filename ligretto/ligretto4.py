# Defineer een orthografische projectie

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

def doNothing():
    pass

	
	
glutInit()
glutInitWindowSize(400, 400)
glutCreateWindow("Ligretto".encode("ascii"))

glOrtho(0, 400, 0, 400, -1, 1) # links, rechts, onder, boven, dichtbij, veraf
glColor(1, 1, 1) # wit
glRectf(10, 10, 60, 85)
glColor(1, 0, 0)
glRectf(100, 10, 150, 85)
glColor(0, 1, 0)
glRectf(150, 10, 200, 85)
glColor(0, 0, 1)
glRectf(200, 10, 250, 85)
glFlush()
glutDisplayFunc(doNothing) # negeer dit voor nu
glutMainLoop() # negeer dit voor nu
