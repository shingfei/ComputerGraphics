# Twee kubussen draaien apart

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from sys import exit

SPEED = 0.02

def display():
    phi = SPEED * glutGet(GLUT_ELAPSED_TIME)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix() # sla huidige matrix op (= projectiematrix * translatiematrix)
    glTranslate(-0.5, 0, 0)
    glRotate(phi, 0, 1, 0)
    glutWireCube(0.5)
    glPopMatrix() # herstel opgeslagen matrix
    glPushMatrix() # sla huidige matrix op 
    glTranslate(0.5, 0, 0)
    glRotate(phi, 0, 1, 0)
    glutWireCube(0.5)
    glPopMatrix() # herstel opgeslagen matrix
    glutSwapBuffers()
      
def end(key, x, y):
    exit()

def increasePhi(val):
    global phi
    phi += 1
    glutTimerFunc(40, increasePhi, 0)
    glutPostRedisplay()

phi = 0

glutInit()
glutInitDisplayMode(GLUT_MULTISAMPLE | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(640, 480)
glutCreateWindow("Perspective view".encode("ascii"))
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glEnable(GL_BLEND)
glEnable(GL_LINE_SMOOTH)
glEnable(GL_DEPTH_TEST)
glLineWidth(1)
glFrustum(-1.333, 1.333, -1, 1, 5, 20)
glTranslate(0, 0, -6)
glutDisplayFunc(display)
glutKeyboardFunc(end)
glutIdleFunc(glutPostRedisplay)
glutMainLoop()
