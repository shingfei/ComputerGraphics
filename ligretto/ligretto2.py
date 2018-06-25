# Defineer de achtergrondkleur

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

def doNothing():
    pass

glutInit()
glutInitWindowSize(400, 400)
glutCreateWindow("Ligretto".encode("ascii"))
glClearColor(0.5, 0.5, 0.5, 0) # rood, groen, blauw, alpha 
glClear(GL_COLOR_BUFFER_BIT)
glFlush()
glutDisplayFunc(doNothing) # negeer dit voor nu
glutMainLoop() # negeer dit voor nu
