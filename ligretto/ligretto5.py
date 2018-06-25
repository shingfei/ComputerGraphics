# Callback functie

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

def display():
    glColor(1, 1, 1) # wit
    glRectf(10, 10, 60, 85)
    glFlush()

glutInit()
glutInitWindowSize(400, 400)
glutCreateWindow("Ligretto".encode("ascii"))
glOrtho(0, 400, 0, 400, -1, 1) # links, rechts, boven, onder, dichtbij, veraf
glutDisplayFunc(display)
glutMainLoop()
