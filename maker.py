# ARKATHON
#
# Carlos Albornoz
# http://carlos.debianchile.cl
# caralbornozc@gmail.com
#
# Sebastian Gonzalez
# http://brutalchrist.info/blog
# brutalchrist@gmail.com
#
# 6 de Julio de 2008

# Graficos ripeados del juego Arkanoid original de TAITO (1987)
# Musica y sonidos ripeados del juego arkanoid returns  de TAITO (1997)

# Licencia GNU/GPL v2
# Si lo usas, por favor, reconoce nuestro trabajo

# -*- coding: utf-8 -*-
from lxml.html.builder import FONT

import sys, pygame, os
from twisted.internet.tcp import _AbortingMixin
from constantes import *


class Bloque(object):
    def __init__(self):
        self.bloque = None
        self.x = 490
        self.y = 200

    def setBloque(self, bloque):
        self.bloque = bloque

    def getBloque(self):
        return self.bloque

    def setX(self, x):
        self.x = x

    def getX(self):
        return int(self.x)

    def setY(self, y):
        self.y = y

    def getY(self):
        return int(self.y)

    def getPos(self):
        return int(self.x), int(self.y)

class Boton(object):
    def __init__(self, sprite=None):
        self.upPush = False
        self.downPush = False
        self.sprite = sprite

    @property
    def upPush(self):
        return self.__upPush

    @upPush.setter
    def upPush(self, upPush):
        self.__upPush = upPush

    @property
    def downPush(self):
        return self.__downPush

    @downPush.setter
    def downPush(self, downPush):
        self.__downPush = downPush

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, sprite):
        self.__sprite = sprite

    def restablecerEstados(self):
        self.upPush = False
        self.downPush = False


class ArkathonMaker(object):
    def __init__(self):
        # permite centrar la ventana a la pantalla usando SDL
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        # Inicializa el mixer
        pygame.mixer.pre_init(44100, -16, 2, 5000)
        # asigna cuantos pixeles avanza en X e Y
        self.bgsound = 0
        # ejecuta la ventana
        self.size = self.width, self.height = 540, 512
        self.screen = pygame.display.set_mode(self.size)
        pygame.draw.line(self.screen, (255,255,255), (448, 0), (448, 512), 2)
        # nombre del titulo de la ventana
        pygame.display.set_caption("Arkathon Maker")

        # Botones y sus posiciones
        self.up = pygame.image.load(BUTTON_UP_PATH)
        self.down = pygame.image.load(BUTTON_DOWN_PATH)
        #self.mas = pygame.image.load(BUTTON_MAS_PATH)
        self.mas = Boton(pygame.image.load(BUTTON_MAS_PATH))

        self.screen.blit(self.up, self.up.get_rect(center=(BUTTON_UP_POS)))
        self.screen.blit(self.down, self.down.get_rect(center=(BUTTON_DOWN_POS)))
        self.screen.blit(self.mas.sprite, self.mas.sprite.get_rect(center=(BUTTON_MAS_POS)))

        self.contadorListaBloques = 0

        self.listaBloques = []
        self.elBloque = Bloque()
        self.elBloque.setBloque(pygame.image.load(LIST_BLOCKS[self.contadorListaBloques]))
        self.listaBloques.append(self.elBloque)

        self.bloqueSeleccionado = False

        self.fondo = pygame.image.load(BACKGROUND_PATH)
        self.fondorect = self.fondo.get_rect()
        # fps
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(1)



    def Maker(self):
        # Da valores iniciales a los contadores
        bgsound = 0

        while 1:
            self.clock.tick(160)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            x, y = pygame.mouse.get_pos()



            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si se presiona el boton agregar
                if self.mas.sprite.get_rect(center=(BUTTON_MAS_POS)).collidepoint(x, y):
                    self.mas.downPush = True
                    #presionado[0] = True

                if event.button == LEFT_CLICK:
                    if self.elBloque.bloque.get_rect(center=(self.elBloque.getPos())).collidepoint(x, y):
                        self.bloqueSeleccionado = True

                if event.button == RIGHT_CLICK:
                    if self.bloqueSeleccionado:
                        self.bloqueSeleccionado = False


            if event.type == pygame.MOUSEBUTTONUP:
                # Si se suelta el boton agregar
                if self.mas.sprite.get_rect(center=(BUTTON_MAS_POS)).collidepoint(x, y):
                    if self.mas.downPush == True:
                        self.mas.downPush = False
                        self.mas.upPush = True

            # Solo una llamada al metodo nuevo bloque
            if self.mas.upPush == True:
                self.mas.restablecerEstados()
                self.nuevoBloques()

            if self.bloqueSeleccionado:
                self.elBloque.setX(x)
                self.elBloque.setY(y)

            # dibuja el fondo
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.fondo, self.fondorect)

            # dibuja los bloques
            for b in self.listaBloques:
                self.screen.blit(b.getBloque(), b.getBloque().get_rect(center=(b.getX(), b.getY())))

            self.mouseOver(x, y)

            self.displayFonts(x, y)


            pygame.display.flip()

    def displayFonts(self, x, y):
        if pygame.font:
            font = pygame.font.Font(FONT_PATH, 20)

            arkathonLogo = font.render('arkathon maker!', 0, (255, 0, 0))
            fontX = font.render('x  ' + str(x), 0, (255, 0, 0))
            fontY = font.render('y  ' + str(y), 0, (255, 0, 0))

            self.screen.blit(arkathonLogo, (150, 0))
            self.screen.blit(fontX, (10, 20))
            self.screen.blit(fontY, (130, 20))

    def mouseOver(self, x, y):
        """Genera una especie de mouse over.

        :parameter:
            - x: Posicion x del mouse
            - y: Posicion y del mouse

        """
        if self.up.get_rect(center=(BUTTON_UP_POS)).collidepoint(x, y):
            self.up = pygame.image.load(BUTTON_UP_RED_PATH)
            self.screen.blit(self.up, self.up.get_rect(center=(BUTTON_UP_POS)))
        else:
            self.up = pygame.image.load(BUTTON_UP_PATH)
            self.screen.blit(self.up, self.up.get_rect(center=(BUTTON_UP_POS)))

        if self.down.get_rect(center=(BUTTON_DOWN_POS)).collidepoint(x, y):
            self.down = pygame.image.load(BUTTON_DOWN_RED_PATH)
            self.screen.blit(self.down, self.down.get_rect(center=(BUTTON_DOWN_POS)))
        else:
            self.down = pygame.image.load(BUTTON_DOWN_PATH)
            self.screen.blit(self.down, self.down.get_rect(center=(BUTTON_DOWN_POS)))

        if self.mas.sprite.get_rect(center=(BUTTON_MAS_POS)).collidepoint(x, y):
            self.mas.sprite = pygame.image.load(BUTTON_MAS_RED_PATH)
            self.screen.blit(self.mas.sprite, self.mas.sprite.get_rect(center=(BUTTON_MAS_POS)))
        else:
            self.mas.sprite = pygame.image.load(BUTTON_MAS_PATH)
            self.screen.blit(self.mas.sprite, self.mas.sprite.get_rect(center=(BUTTON_MAS_POS)))


    def nuevoBloques(self):
        #TODO: a~adir
        self.elBloque = Bloque()
        siguienteBloque = self.siguienteBloque()
        #print siguienteBloque
        #print self.contadorListaBloques
        self.elBloque.setBloque(pygame.image.load(siguienteBloque))
        self.listaBloques.append(self.elBloque)

    def siguienteBloque(self):
        if self.contadorListaBloques == len(LIST_BLOCKS) - 1:
            self.contadorListaBloques = 0
        else:
            self.contadorListaBloques += 1

        return LIST_BLOCKS[self.contadorListaBloques]

    def anteriorBloque(self):
        if self.contadorListaBloques == 0:
            self.contadorListaBloques = len(LIST_BLOCKS)
        else:
            self.contadorListaBloques -= 1

        return LIST_BLOCKS[self.contadorListaBloques]


if __name__ == '__main__':
    theGame = ArkathonMaker()
    theGame.Maker()