# Complexere polygonen

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
    glVertex(12, 18, 0)
    glVertex(13, 15, 0)
    glVertex(15, 13, 0)
    glVertex(18, 12, 0)
    glVertex(2 + CARD_WIDTH, 12, 0)
    glVertex(5 + CARD_WIDTH, 13, 0)
    glVertex(7 + CARD_WIDTH, 15, 0)
    glVertex(8 + CARD_WIDTH, 18, 0)
    glVertex(8 + CARD_WIDTH, 2 + CARD_HEIGHT, 0)
    glVertex(7 + CARD_WIDTH, 5 + CARD_HEIGHT, 0)
    glVertex(5 + CARD_WIDTH, 7 + CARD_HEIGHT, 0)
    glVertex(2 + CARD_WIDTH, 8 + CARD_HEIGHT, 0)
    glVertex(18, 8 + CARD_HEIGHT, 0)
    glVertex(15, 7 + CARD_HEIGHT, 0)
    glVertex(13, 5 + CARD_HEIGHT, 0)
    glVertex(12, 2 + CARD_HEIGHT, 0)
    glEnd()
    glFlush()

glutInit()
glutInitWindowSize(WIDTH, HEIGHT)
glutCreateWindow("Ligretto".encode("ascii"))
glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)
glutDisplayFunc(display)
glutMainLoop()
