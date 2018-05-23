from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

GRID_SIZE = 10

class Grid:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.points = []
        glutInit()
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(sizeX * GRID_SIZE, sizeY * GRID_SIZE)
        glutCreateWindow("Raster".encode("ascii"))
        glOrtho(0, sizeX * GRID_SIZE, sizeY * GRID_SIZE, 0, -1, 1)
        glutDisplayFunc(self.display)
        glutKeyboardFunc(self.end)

    def addPoint(self, x, y, c = 1):
        if 0 <= x < self.sizeX and 0 <= y < self.sizeY:
            x = round(x)
            y = round(y)
            self.points.append((x, y, c))
        
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT) 
        for i in self.points:
            x, y, c = i
            if type(c) == tuple:
                glColor(*c)
            else:
                glColor(c, c, c)
            glBegin(GL_POLYGON)
            glVertex(x * GRID_SIZE, y * GRID_SIZE)
            glVertex((x + 1) * GRID_SIZE, y * GRID_SIZE)
            glVertex((x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE)
            glVertex(x * GRID_SIZE, (y + 1) * GRID_SIZE)
            glEnd()
        glColor(.5, .5, .5)
        glBegin(GL_LINES)
        for i in range(1, self.sizeX):
            glVertex(i * GRID_SIZE, 0)
            glVertex(i * GRID_SIZE, self.sizeY * GRID_SIZE)
        for i in range(1, self.sizeY):
            glVertex(0, i * GRID_SIZE)
            glVertex(self.sizeX * GRID_SIZE, i * GRID_SIZE)
        glEnd()
        glFlush()

    def end(self, key, x, y):
        exit()

    def draw(self):
        glutMainLoop()
