# Textuur, bitmap plaatjes

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

from sys import exit
from PIL import Image # voor plaatjes

SPEED = 0.02

def display():
    phi = SPEED * glutGet(GLUT_ELAPSED_TIME)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotate(phi, 0, 1, 0)
    glBegin(GL_POLYGON)
    glTexCoord(0, 0) # specificeer welke coordinaten van textuur en object overeenkomen
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
img = Image.open("Wouter_vierkant.png") # laad plaatje
glPixelStorei(GL_UNPACK_ALIGNMENT, 1) # voor plaatjes met oneven aantal pixels
texture = glGenTextures(1) # maak een ID voor 1 textuur
glBindTexture(GL_TEXTURE_2D, texture) # gebruik de ID
glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST) # specificeer hoe de textuur geschaald moet worden
glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img.tobytes()) # laad het plaatje
glEnable(GL_TEXTURE_2D) # zet textuur aan
glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL) # zorgt dat de kleur van het plaatje gebruikt wordt, en niet de combinatie van verlichting en materiaal
glutDisplayFunc(display)
glutKeyboardFunc(end)
glutIdleFunc(glutPostRedisplay)
glutMainLoop()
