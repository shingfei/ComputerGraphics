# Stapeltjes

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

def drawString(x, y, colour, string):
    glColor(colour)
    glLineWidth(2)
    glDisable(GL_MULTISAMPLE)
    glPushMatrix()
    glTranslate(x, y, 0)
    glScale(0.15, 0.15, 1)
    width = 0
    for i in string:
        width += glutStrokeWidth(GLUT_STROKE_ROMAN, ord(i))
    glTranslate(-width / 2, 0, 0)
    for i in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(i))
    glPopMatrix()
    glEnable(GL_MULTISAMPLE)

def drawCard(x, y, colour, value, number):
    glColor(GREY)
    for i in range(number - 1, -1, -1):
        glBegin(GL_POLYGON)
        glVertex(x + 2 + i, y + 8 + i, 0)
        glVertex(x + 3 + i, y + 5 + i, 0)
        glVertex(x + 5 + i, y + 3 + i, 0)
        glVertex(x + 8 + i, y + 2 + i, 0)
        glVertex(x + CARD_WIDTH - 8 + i, y + 2 + i, 0)
        glVertex(x + CARD_WIDTH - 5 + i, y + 3 + i, 0)
        glVertex(x + CARD_WIDTH - 3 + i, y + 5 + i, 0)
        glVertex(x + CARD_WIDTH - 2 + i, y + 8 + i, 0)
        glVertex(x + CARD_WIDTH - 2 + i, y + CARD_HEIGHT - 8 + i, 0)
        glVertex(x + CARD_WIDTH - 3 + i, y + CARD_HEIGHT - 5 + i, 0)
        glVertex(x + CARD_WIDTH - 5 + i, y + CARD_HEIGHT - 3 + i, 0)
        glVertex(x + CARD_WIDTH - 8 + i, y + CARD_HEIGHT - 2 + i, 0)
        glVertex(x + 8 + i, y + CARD_HEIGHT - 2 + i, 0)
        glVertex(x + 5 + i, y + CARD_HEIGHT - 3 + i, 0)
        glVertex(x + 3 + i, y + CARD_HEIGHT - 5 + i, 0)
        glVertex(x + 2 + i, y + CARD_HEIGHT - 8 + i, 0)
        glEnd()
    glColor(colour)
    glLineWidth(1)
    glBegin(GL_LINE_LOOP)
    glVertex(x + 7, y + 7, 0)
    glVertex(x + CARD_WIDTH - 7, y + 7, 0)
    glVertex(x + CARD_WIDTH - 7, y + CARD_HEIGHT - 7, 0)
    glVertex(x + 7, y + CARD_HEIGHT - 7, 0)
    glEnd()
    drawString(x + 0.5 * CARD_WIDTH, y + 0.4 * CARD_HEIGHT, colour, str(value))

def endDraw():
    glFlush()

def display():
    startDraw()
    drawCard(10, 10, RED, 1, 3)
    drawCard(80, 10, GREEN, 4, 5)
    drawCard(10, 100, BLUE, 7, 7)
    drawCard(80, 100, YELLOW, 10, 10)
    drawCard(150, 10, WHITE, "", 0) # leeg stapeltje
    endDraw()

glutInit()
glutInitDisplayMode(GLUT_MULTISAMPLE)
glutInitWindowSize(WIDTH, HEIGHT)
glutCreateWindow("Ligretto".encode("ascii"))
glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glEnable(GL_BLEND)
glEnable(GL_LINE_SMOOTH)
glutDisplayFunc(display)
glutMainLoop()
