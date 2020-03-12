# Solid shapes

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
    if i == 0: # een aantal standaard vormen
        glutSolidSphere(1, 100, 100) # straal, aantal partjes, aantal schijven
    elif i == 1:
        glutSolidCube(1)
    elif i == 2:
        glutSolidCone(1, 1, 100, 100) # straal, hoogte, aantal partjes, aantal schijven
    elif i == 3:
        glutSolidTorus(0.3, 0.8, 100, 100) # binnenstraal, buitenstraal, aantal zijden, aaantal "taartpunten"
    elif i == 4:
        glScale(0.5, 0.5, 0.5)
        glutSolidDodecahedron()
    elif i == 5:
        glutSolidOctahedron()
    elif i == 6:
        glutSolidTetrahedron()
    elif i == 7:
        glutSolidIcosahedron()
    elif i == 8:
        glutSolidTeapot(1)
    glPopMatrix()
    glutSwapBuffers()
      
def end(key, x, y):
    global i
    if key == b"\x1b":
        exit()
    i = (i + 1) % 9

i = 0

glutInit()
glutInitDisplayMode(GLUT_MULTISAMPLE | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(640, 480)
glutCreateWindow("Perspective view".encode("ascii"))
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glEnable(GL_BLEND)
glEnable(GL_LINE_SMOOTH)
glEnable(GL_DEPTH_TEST)
glFrustum(-1.333, 1.333, -1, 1, 5, 20)
gluLookAt(3, 4, 5, 0, 0, 0, 0, 1, 0)
glutDisplayFunc(display)
glutKeyboardFunc(end)
glutIdleFunc(glutPostRedisplay)
glutMainLoop()
