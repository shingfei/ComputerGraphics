# Matrix opslaan op de stack

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from sys import exit

SPEED = 0.02

def display():
    phi = SPEED * glutGet(GLUT_ELAPSED_TIME)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix() # sla huidige matrix op (= projectiematrix * translatiematrix)
    glRotate(phi, 0, 1, 0)
    glutWireCube(1)
    glPopMatrix() # herstel opgeslagen matrix
    glutSwapBuffers()
      
def end(key, x, y):
    exit()

glutInit()
glutInitDisplayMode(GLUT_MULTISAMPLE | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(640, 480)
glutCreateWindow("Perspective view".encode("ascii"))
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glEnable(GL_BLEND)
glEnable(GL_LINE_SMOOTH)
glEnable(GL_DEPTH_TEST)
glLineWidth(1)
glFrustum(-1.333, 1.333, -1, 1, 5, 20) # hoeft maar 1 keer
glTranslate(0, 0, -6) # hoeft maar 1 keer
glutDisplayFunc(display)
glutKeyboardFunc(end)
glutIdleFunc(glutPostRedisplay)
glutMainLoop()
