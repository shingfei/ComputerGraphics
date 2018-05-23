# Textuur

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

from sys import exit

SPEED = 0.02

def display():
    phi = SPEED * glutGet(GLUT_ELAPSED_TIME)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotate(phi, 0, 1, 0)
    glBegin(GL_POLYGON)
    glTexCoord(0, 0) # specificeer welke cordinaten van textuur en object overeenkomen
    glVertex(-1, 1, 0)
    glTexCoord(0, 5) # TexCoord groter dan 1 geven herhaling
    glVertex(-1, -1, 0)
    glTexCoord(5, 5)
    glVertex(1, -1, 0)
    glTexCoord(5, 0)
    glVertex(1, 1, 0)
    glEnd()
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
glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, [1, 1, 0, 1])
glMaterial(GL_FRONT_AND_BACK, GL_SPECULAR, [1, 1, 1, 1])
glMaterial(GL_FRONT_AND_BACK, GL_SHININESS, 50)
SIZE = 64 # grootte in texels
check = (([255] * 3 * (SIZE // 2) + [127] * 3 * (SIZE // 2)) * (SIZE // 2 ) +\
         ([127] * 3 * (SIZE // 2) + [255] * 3 * (SIZE // 2)) * (SIZE // 2 )) # 2x2 schaakbord
texture = glGenTextures(1) # maak een ID voor 1 textuur
glBindTexture(GL_TEXTURE_2D, texture) # gebruik de ID
glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) # specificeer hoe de textuur geschaald moet worden
glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, SIZE, SIZE, 0, GL_RGB, GL_UNSIGNED_BYTE, check) # laad het schaakbord
glEnable(GL_TEXTURE_2D) # zet textuur aan
glutDisplayFunc(display)
glutKeyboardFunc(end)
glutIdleFunc(glutPostRedisplay)
glutMainLoop()
