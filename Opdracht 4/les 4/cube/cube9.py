# Transparantie, blending

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from sys import exit

SPEED = 0.02

def display():
    phi = SPEED * glutGet(GLUT_ELAPSED_TIME)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotate(phi, 0, 1, 0)
    glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [1, 1, 0, 1]) # geel opaak materiaal
    glTranslate(-0.5, 0, 0)
    glutSolidSphere(1, 100, 100)
    glTranslate(1, 0, 0)
    glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [1, 0, 1, 0.5]) # paars doorzichtig materiaal
    glutSolidCube(1.5)
    glPopMatrix()
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
glMatrixMode(GL_PROJECTION)
glFrustum(-1.333, 1.333, -1, 1, 5, 20)
glMatrixMode(GL_MODELVIEW)
gluLookAt(3, 4, 5, 0, 0, 0, 0, 1, 0)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glLight(GL_LIGHT0, GL_POSITION, [-3, 4, 5])
glLight(GL_LIGHT0, GL_DIFFUSE, [0.5, 0.5, 0.5])
glLight(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5])
glLight(GL_LIGHT0, GL_SPECULAR, [1, 1, 1])
glMaterial(GL_FRONT_AND_BACK, GL_SPECULAR, [1, 1, 1])
glMaterial(GL_FRONT_AND_BACK, GL_SHININESS, 50)
glutDisplayFunc(display)
glutKeyboardFunc(end)
glutIdleFunc(glutPostRedisplay)
glutMainLoop()
