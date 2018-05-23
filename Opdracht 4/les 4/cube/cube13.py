# Textuur, automatisch genereren van coordinaten

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
    glutSolidTeapot(1)
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
glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR) # mode voor genereren van horizontale textuur-coordinaten 
glTexGenfv(GL_S, GL_OBJECT_PLANE, [1, 0, 0, 0]) # vlak x = 0 (yz-vlak)
glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR) # mode voor genereren van verticale textuur-coordinaten
glTexGenfv(GL_T, GL_OBJECT_PLANE, [0, 1, 0, 0]) # vlak y = 0 (xz-vlak)
glEnable(GL_TEXTURE_GEN_S) # zet het automatisch genereren van horizontale textuur-coordinaten aan
glEnable(GL_TEXTURE_GEN_T) # zet het automatisch genereren van vericale textuur-coordinaten aan
glutDisplayFunc(display)
glutKeyboardFunc(end)
glutIdleFunc(glutPostRedisplay)
glutMainLoop()
