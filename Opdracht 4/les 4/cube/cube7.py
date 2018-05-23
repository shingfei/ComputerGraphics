# Belichting

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
    if i == 0:
        glutSolidSphere(1, 100, 100)
    elif i == 1:
        glutSolidCube(1)
    elif i == 2:
        glutSolidCone(1, 1, 100, 100)
    elif i == 3:
        glutSolidTorus(0.3, 0.8, 100, 100)
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
        glutSolidTeapot(1) # zie http://nautil.us/blog/the-most-important-object-in-computer-graphics-history-is-this-teapot
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
glMatrixMode(GL_PROJECTION) # lichtbronnen moeten niet geprojecteerd worden, dus om onderscheid te kunnen maken moet de projectiematrix in een andere "matrix modus"
glFrustum(-1.333, 1.333, -1, 1, 5, 20)
glMatrixMode(GL_MODELVIEW) # schakel terug naar de "model/view transformatiematrix modus"
gluLookAt(3, 4, 5, 0, 0, 0, 0, 1, 0)
glEnable(GL_LIGHTING) # belichting
glEnable(GL_RESCALE_NORMAL) # zorgt voor correcte belichting van geschaalde objecten
glEnable(GL_LIGHT0) # een lichtbron
glLight(GL_LIGHT0, GL_POSITION, [-3, 4, 5]) # positie lichtbron
glLight(GL_LIGHT0, GL_DIFFUSE, [1, 0, 1]) # kleur lichtbron (paars)
glLight(GL_LIGHT0, GL_AMBIENT, [1, 0, 1]) # kleur ambient licht (paars)
#glEnable(GL_LIGHT1) # nog een lichtbron
#glLight(GL_LIGHT1, GL_POSITION, [3, 4, 5]) # positie lichtbron
#glLight(GL_LIGHT1, GL_DIFFUSE, [1, 1, 0]) # kleur lichtbron (geel)
#glLight(GL_LIGHT1, GL_AMBIENT, [1, 1, 0]) # kleur ambient licht (geel)
glutDisplayFunc(display)
glutKeyboardFunc(end)
glutIdleFunc(glutPostRedisplay)
glutMainLoop()
