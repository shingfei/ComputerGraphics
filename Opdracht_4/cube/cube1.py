# Matrices stapelen

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from sys import exit

SPEED = 0.02

def display():
    phi = SPEED * glutGet(GLUT_ELAPSED_TIME)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity() # wis de huidige matrix
    glFrustum(-1.333, 1.333, -1, 1, 5, 20) # perspectieftransformatie (als 3e uitgevoerd)
    glTranslate(0, 0, -6) # translatie (als 2e uitgevoerd)
    glRotate(phi, 0, 1, 0) # rotatie (als 1e uitgevoerd)
    glutWireCube(1) # kubus rond de oorsprong
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
glutDisplayFunc(display)
glutKeyboardFunc(end)
glutIdleFunc(glutPostRedisplay)
glutMainLoop()
