# Polygonen

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

CARD_WIDTH = 50
CARD_HEIGHT = 75

WIDTH = 11 * CARD_WIDTH
HEIGHT = 6 * CARD_HEIGHT

def display():
    glColor(1, 1, 1) # wit
    glBegin(GL_POLYGON)
    glVertex(10, 10, 0)
    glVertex(10 + CARD_WIDTH, 10, 0)
    glVertex(10 + CARD_WIDTH, 10 + CARD_HEIGHT, 0)
    glVertex(10, 10 + CARD_HEIGHT, 0)
    glEnd()
    glFlush()

glutInit()
glutInitWindowSize(WIDTH, HEIGHT)
glutCreateWindow("Ligretto".encode("ascii"))
glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)
glutDisplayFunc(display)
glutMainLoop()
