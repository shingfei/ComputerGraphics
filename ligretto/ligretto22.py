# Verdwijnpunt in het midden

from random import randint
from sys import exit

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

CARD_WIDTH = 50
CARD_HEIGHT = 75

WIDTH = 11 * CARD_WIDTH
HEIGHT = 6 * CARD_HEIGHT

RED = 1, 0, 0
GREEN = 0, 1, 0
YELLOW = 1, 1, 0
BLUE = 0, 0, 1
GREY = 0.5, 0.5, 0.5
WHITE = 1, 1, 1
COLOURS = [RED, GREEN, YELLOW, BLUE]

NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3

ANIMATION_TIME = 200

class Display:
    def __init__(self, windowName):
        glutInit()
        glutInitDisplayMode(GLUT_MULTISAMPLE | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(WIDTH, HEIGHT)
        glutCreateWindow(windowName.encode("ascii"))
        glFrustum(-0.5 * WIDTH, 0.5 * WIDTH, -0.5 * HEIGHT, 0.5 * HEIGHT, 100, 140) # gecentreerd op de oorsprong
        # let op: near (100) en far (140) zijn geen z-coordinaten maar afstand tot de "camera" in de kijkrichting
        glTranslate(-0.5 * WIDTH, -0.5 * HEIGHT, 0) # verschuif "camera"
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_BLEND)
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_DEPTH_TEST)

    animationCallbacks = []
    
    def reshape(self, x, y):
        if x / y > WIDTH / HEIGHT:
            glViewport(0, 0, int(y * WIDTH / HEIGHT), y)
        else:
            glViewport(0, 0, x, int(x * HEIGHT / WIDTH))
            
    def animate(self):
        for i in Display.animationCallbacks:
            i()

    def startDraw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
    def endDraw(self):
        glFlush()
        glutSwapBuffers()

    def drawString(self, x, y, z, colour, string):
        glColor(colour)
        glLineWidth(2)
        glDisable(GL_MULTISAMPLE)
        glPushMatrix()
        glDepthMask(GL_FALSE)
        glTranslate(x, y, z)
        glScale(0.15, 0.15, 1)
        width = 0
        for i in string:
            width += glutStrokeWidth(GLUT_STROKE_ROMAN, ord(i))
        glTranslate(-width / 2, 0, 0)
        for i in string:
            glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(i))
        glDepthMask(GL_TRUE)
        glPopMatrix()
        glEnable(GL_MULTISAMPLE)
        
    def drawCard(self, x, y, colour, value, number, onTop):
        z = -101 if onTop else -103 # verder weg gelegen
        glColor(GREY)
        for i in range(number):
            glBegin(GL_POLYGON) # verschuiving voor stapeltjes eruit
            glVertex(x + 2, y + 8, z - i)
            glVertex(x + 3, y + 5, z - i)
            glVertex(x + 5, y + 3, z - i)
            glVertex(x + 8, y + 2, z - i)
            glVertex(x + CARD_WIDTH - 8, y + 2, z - i)
            glVertex(x + CARD_WIDTH - 5, y + 3, z - i)
            glVertex(x + CARD_WIDTH - 3, y + 5, z - i)
            glVertex(x + CARD_WIDTH - 2, y + 8, z - i)
            glVertex(x + CARD_WIDTH - 2, y + CARD_HEIGHT - 8, z - i)
            glVertex(x + CARD_WIDTH - 3, y + CARD_HEIGHT - 5, z - i)
            glVertex(x + CARD_WIDTH - 5, y + CARD_HEIGHT - 3, z - i)
            glVertex(x + CARD_WIDTH - 8, y + CARD_HEIGHT - 2, z - i)
            glVertex(x + 8, y + CARD_HEIGHT - 2, z - i)
            glVertex(x + 5, y + CARD_HEIGHT - 3, z - i)
            glVertex(x + 3, y + CARD_HEIGHT - 5, z - i)
            glVertex(x + 2, y + CARD_HEIGHT - 8, z - i)
            glEnd()
        if colour != None:
            glColor(colour)
            glLineWidth(1)
            glBegin(GL_LINE_LOOP)
            glVertex(x + 7, y + 7, z + 0.01) # vlak boven de kaart zelf
            glVertex(x + CARD_WIDTH - 7, y + 7, z + 0.01)
            glVertex(x + CARD_WIDTH - 7, y + CARD_HEIGHT - 7, z + 0.01)
            glVertex(x + 7, y + CARD_HEIGHT - 7, z + 0.01)
            glEnd()
            self.drawString(x + 0.5 * CARD_WIDTH, y + 0.4 * CARD_HEIGHT, z + 0.01, colour, str(value))
        
class Card:
    def __init__(self, player, colour, value):
        self.player = player
        self.colour = colour
        self.value = value
        self.posX = None
        self.posY = None

    def draw(self, display, onTop):
        display.drawCard(self.posX, self.posY, self.colour, self.value, 1, onTop)
        
class Pile:
    def __init__(self, x = None, y = None):
        self.cards = []
        self.posX = x
        self.posY = y
        self.movingCard = None
        
    def fullDeck(self, player):
        for i in COLOURS:
            for j in range(1, 11):
                self.cards.append(Card(player, i, j))
        
    def addCard(self, c):
        c.posX = self.posX
        c.posY = self.posY
        self.cards.append(c)

    def size(self):
        return len(self.cards)

    def takeCard(self):
        if self.size() > 0:
            return self.cards.pop()

    def animate(self):
        remainingTime = ANIMATION_TIME - glutGet(GLUT_ELAPSED_TIME) + self.startTime
        if remainingTime <= 0:
            self.addCard(self.movingCard)
            self.movingCard = None
            Display.animationCallbacks.remove(self.animate)
        else:
            self.movingCard.posX = self.posX + self.vectorX * remainingTime
            self.movingCard.posY = self.posY + self.vectorY * remainingTime
        glutPostRedisplay()
            
    def moveCard(self, c):
        self.vectorX = float(c.posX - self.posX) / ANIMATION_TIME
        self.vectorY = float(c.posY - self.posY) / ANIMATION_TIME
        self.movingCard = c
        self.startTime = glutGet(GLUT_ELAPSED_TIME)
        Display.animationCallbacks.append(self.animate)

    def topCard(self):
        if self.size() > 0:
            return self.cards[-1]
    
    def draw(self, display):
        if self.size() > 0:
            display.drawCard(self.posX, self.posY, None, "", self.size(), False)
            self.topCard().draw(display, False)
        else:
            display.drawCard(self.posX, self.posY, WHITE, "", 0, False)
        if self.movingCard != None:
            self.movingCard.draw(display, True)
 
    def shuffle(self):
        for i in range(self.size()):
            j = randint(0, self.size() - 1)
            c = self.cards[i]
            self.cards[i] = self.cards[j]
            self.cards[j] = c

    def isEmpty(self):
        return self.size() == 0

class Player:
    def __init__(self, side, cards, noOfPiles):
        cards.shuffle()
        self.side = side
        self.deck = cards
        self.score = 0
        self.piles = []
        for i in range(noOfPiles + 2):
            if side == NORTH:
                x = (i + 2) * CARD_WIDTH
                y = 0
            elif side == EAST:
                x = 10 * CARD_WIDTH
                y = i * CARD_HEIGHT
            elif side == SOUTH:
                x = (i + 2) * CARD_WIDTH
                y = 5 * CARD_HEIGHT
            elif side == WEST:
                x = 0
                y = i * CARD_HEIGHT
            self.piles.append(Pile(x, y))
        self.discard = self.piles.pop()
        self.ligretto = self.piles.pop()
        for i in self.piles:
            i.addCard(cards.takeCard())
        for i in range(10):
            self.ligretto.addCard(cards.takeCard())

    def draw(self, display):
        for i in self.piles:
            i.draw(display)
        self.ligretto.draw(display)
        self.discard.draw(display)

    newX = CARD_WIDTH + 25
    newY = 3 * CARD_HEIGHT

    def tryCard(self, pile, piles):
        if pile.topCard().value == 1:
            p = Pile(Player.newX, Player.newY)
            p.moveCard(pile.takeCard())
            piles.append(p)
            Player.newX += CARD_WIDTH
            if Player.newX > 8 * CARD_WIDTH + 25:
                Player.newX = CARD_WIDTH + 25
                Player.newY -= CARD_HEIGHT
            return True
        for i in piles:
            if i.movingCard == None:
                if pile.topCard().colour == i.topCard().colour and pile.topCard().value == i.topCard().value + 1:
                    i.moveCard(pile.takeCard())
                    return True
        return False

    def drawThree(self):
        if self.deck.isEmpty():
            while not self.discard.isEmpty():
                self.deck.addCard(self.discard.takeCard())
            self.deck.shuffle()
        for i in range(3):
            if not self.deck.isEmpty():
                self.discard.addCard(self.deck.takeCard())
            else:
                break

    def play(self, piles):
        if self.tryCard(self.ligretto, piles):
            if self.ligretto.isEmpty():
                return True
            return False
        for i in self.piles:
            if i.isEmpty():
                if i.movingCard == None:
                    i.moveCard(self.ligretto.takeCard())
                    if self.ligretto.isEmpty():
                        return True
                return False
            if self.tryCard(i, piles):
                return False
        if self.discard.isEmpty():
            self.drawThree()
        if not self.tryCard(self.discard, piles):
            self.drawThree()
        return False

class Game:
    def __init__(self, noOfPlayers, msec):
        self.msec = msec
        self.ligretto = None
        self.players = []
        self.piles = []
        for i in range(noOfPlayers):
            cards = Pile()
            cards.fullDeck(i)
            self.players.append(Player(i, cards, 7 - noOfPlayers))
        self.display = Display("Ligretto")
        glutDisplayFunc(self.draw)
        glutTimerFunc(msec, self.play, 1)
        glutMouseFunc(self.mouseFunc)
        glutKeyboardFunc(self.keyboardFunc)
        glutIdleFunc(self.display.animate)
        glutReshapeFunc(self.display.reshape)
        glutMainLoop()

    def draw(self):
        self.display.startDraw()
        for i in self.players:
            i.draw(self.display)
        for i in self.piles:
            i.draw(self.display)
        if self.ligretto != None:
            self.display.drawString(275, 350, -100, WHITE, "Player %d has Ligretto!" % (self.ligretto.side + 1))
            self.display.drawString(275, 320, -100, WHITE, "Player %d wins!" % (self.winner.side + 1))
            for i in self.players:
                self.display.drawString(275, 135 - 18 * i.side, -100, WHITE, "Player %d scores %d points." % ((i.side + 1), i.score))            
        self.display.endDraw()

    def haveLigretto(self, player):
        glutMouseFunc(None)
        self.ligretto = player
        for i in self.piles:
            for j in i.cards:
                self.players[j.player].score += 1
        self.winner = self.players[0]
        for i in self.players:
            i.score -= 2 * i.ligretto.size() 
            if i.score > self.winner.score:
                self.winner = i
                
    def play(self, value):        
        if self.ligretto == None:
            if self.players[value].play(self.piles):
                self.haveLigretto(self.players[value])
            else:
                value += 1
                if value == len(self.players):
                    value = 1
                glutTimerFunc(self.msec, self.play, value)
            glutPostRedisplay()

    def testPos(self, pile, x, y):
        return pile.posX < x < pile.posX + CARD_WIDTH and pile.posY < y < pile.posY + CARD_HEIGHT

    def mouseFunc(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            dummy, dummy, width, height = glGetInteger(GL_VIEWPORT)
            x = WIDTH * x / width
            windowHeight = glutGet(GLUT_WINDOW_HEIGHT)
            y = HEIGHT * (windowHeight - y) / height
            if self.testPos(self.players[0].ligretto, x, y):
                if self.players[0].tryCard(self.players[0].ligretto, self.piles):
                    if self.players[0].ligretto.isEmpty():
                        self.haveLigretto(self.players[0])
                    glutPostRedisplay()
                    return
                for i in self.players[0].piles:
                    if i.isEmpty() and i.movingCard == None:
                        i.moveCard(self.players[0].ligretto.takeCard())
                        if self.players[0].ligretto.isEmpty():
                            self.haveLigretto(self.players[0])
                        glutPostRedisplay()                
                        return
            for i in self.players[0].piles:
                if self.testPos(i, x, y) and not i.isEmpty():
                    if self.players[0].tryCard(i, self.piles):
                        glutPostRedisplay()
                        return
            if self.testPos(self.players[0].discard, x, y):
                if not self.players[0].discard.isEmpty():
                    if self.players[0].tryCard(self.players[0].discard, self.piles):
                        glutPostRedisplay()
                        return
                self.players[0].drawThree()
                glutPostRedisplay()

    def keyboardFunc(self, key, x, y):
        if key == b"\x1b": # escape
            exit()
                       
Game(4, 1000)
