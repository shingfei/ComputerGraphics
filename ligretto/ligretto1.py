# Maak een venster

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

def doNothing():
    pass

glutInit()
glutInitWindowSize(400, 400)
glutCreateWindow("Ligretto".encode("ascii"))
glutDisplayFunc(doNothing) # negeer dit voor nu
glutMainLoop() # negeer dit voor nu
