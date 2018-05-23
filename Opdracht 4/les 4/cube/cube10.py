# Mist

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from sys import exit

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    for i in range(5):
        glTranslate(0, 0, -2)
        glutSolidSphere(1, 100, 100)
    glPopMatrix()
    glFlush()

def end(key, x, y):
    if key == b"\x1b":
        exit()
    if glIsEnabled(GL_FOG):
        glDisable(GL_FOG)
    else:
        glEnable(GL_FOG) # zet mist aan
    glutPostRedisplay()
    
glutInit()
glutInitDisplayMode(GLUT_MULTISAMPLE | GLUT_DEPTH)
glutInitWindowSize(640, 480)
glutCreateWindow("Perspective view".encode("ascii"))
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glEnable(GL_BLEND)
glEnable(GL_LINE_SMOOTH)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_PROJECTION)
glFrustum(-1.333, 1.333, -1, 1, 5, 20)
glMatrixMode(GL_MODELVIEW)
gluLookAt(3, 4, 5, 0, 0, -4, 0, 1, 0)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glLight(GL_LIGHT0, GL_POSITION, [-3, 4, 5])
glLight(GL_LIGHT0, GL_DIFFUSE, [0.5, 0.5, 0.5])
glLight(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5])
glLight(GL_LIGHT0, GL_SPECULAR, [1, 1, 1])
glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [1, 1, 0, 1])
glMaterial(GL_FRONT_AND_BACK, GL_SPECULAR, [1, 1, 1, 1])
glMaterial(GL_FRONT_AND_BACK, GL_SHININESS, 50)
glClearColor(0.5, 0.5, 0.5, 1) # grijze achtergrond
glFogfv(GL_FOG_COLOR, [0.5, 0.5, 0.5]) # grijze mist
glFogi(GL_FOG_MODE, GL_EXP2) # dubbel exponentieel afvallend kleurcontrast
glFogf(GL_FOG_DENSITY, 0.1) # factor voor exponent
glutDisplayFunc(display)
glutKeyboardFunc(end)
glutMainLoop()
