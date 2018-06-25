# Anti-aliasing

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
    glDisable(GL_MULTISAMPLE) # Multisampling werkt niet met tekst
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
    glEnable(GL_MULTISAMPLE) # Zet multisampling weer aan

def drawCard(x, y, colour, value):
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
    drawString(x + 0.5 * CARD_WIDTH, y + 0.4 * CARD_HEIGHT, colour, str(value))

def endDraw():
    glFlush()

def display():
    startDraw()
    drawCard(10, 10, RED, 1)
    drawCard(80, 10, GREEN, 4)
    drawCard(10, 100, BLUE, 7)
    drawCard(80, 100, YELLOW, 10)
    endDraw()

glutInit()
glutInitDisplayMode(GLUT_MULTISAMPLE) # anti-aliasing
glutInitWindowSize(WIDTH, HEIGHT)
glutCreateWindow("Ligretto".encode("ascii"))
glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA) # anti-aliasing
glEnable(GL_BLEND) # anti-aliasing
glEnable(GL_LINE_SMOOTH) # anti-aliasing
glutDisplayFunc(display)
glutMainLoop()