# Kleur

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

CARD_WIDTH = 50
CARD_HEIGHT = 75

WIDTH = 11 * CARD_WIDTH
HEIGHT = 6 * CARD_HEIGHT

RED = 1, 0, 0
GREEN = 0, 1, 0
YELLOW = 1, 1, 0
BLUE = 0, 0, 1
GREY = 0.5, 0.5, 0.5
WHITE = 1, 1, 1

def startDraw():
    glClear(GL_COLOR_BUFFER_BIT)    

def drawCard(x, y, colour):
    glColor(GREY)
    glBegin(GL_POLYGON)
    glVertex(x + 2, y + 8, 0)
    glVertex(x + 3, y + 5, 0)
    glVertex(x + 5, y + 3, 0)
    glVertex(x + 8, y + 2, 0)
    glVertex(x + CARD_WIDTH - 8, y + 2, 0)
    glVertex(x + CARD_WIDTH - 5, y + 3, 0)
    glVertex(x + CARD_WIDTH - 3, y + 5, 0)
    glVertex(x + CARD_WIDTH - 2, y + 8, 0)
    glVertex(x + CARD_WIDTH - 2, y + CARD_HEIGHT - 8, 0)
    glVertex(x + CARD_WIDTH - 3, y + CARD_HEIGHT - 5, 0)
    glVertex(x + CARD_WIDTH - 5, y + CARD_HEIGHT - 3, 0)
    glVertex(x + CARD_WIDTH - 8, y + CARD_HEIGHT - 2, 0)
    glVertex(x + 8, y + CARD_HEIGHT - 2, 0)
    glVertex(x + 5, y + CARD_HEIGHT - 3, 0)
    glVertex(x + 3, y + CARD_HEIGHT - 5, 0)
    glVertex(x + 2, y + CARD_HEIGHT - 8, 0)
    glEnd()
    glColor(colour)
    glLineWidth(1)
    glBegin(GL_LINE_LOOP)
    glVertex(x + 7, y + 7, 0)
    glVertex(x + CARD_WIDTH - 7, y + 7, 0)
    glVertex(x + CARD_WIDTH - 7, y + CARD_HEIGHT - 7, 0)
    glVertex(x + 7, y + CARD_HEIGHT - 7, 0)
    glEnd()

def endDraw():
    glFlush()

def display():
    startDraw()
    drawCard(10, 10, RED)
    drawCard(80, 10, GREEN)
    drawCard(10, 100, BLUE)
    drawCard(80, 100, YELLOW)
    endDraw()

glutInit()
glutInitWindowSize(WIDTH, HEIGHT)
glutCreateWindow("Ligretto".encode("ascii"))
glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)
glutDisplayFunc(display)
glutMainLoop()
