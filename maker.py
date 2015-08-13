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
        self.mas = pygame.image.load(BUTTON_MAS_PATH)

        self.screen.blit(self.up, self.up.get_rect(center=(BUTTON_UP_POS)))
        self.screen.blit(self.down, self.down.get_rect(center=(BUTTON_DOWN_POS)))
        self.screen.blit(self.mas, self.mas.get_rect(center=(BUTTON_MAS_POS)))

        self.listaBloques = []
        self.elBloque = Bloque()
        self.elBloque.setBloque(pygame.image.load(BLOCK_BLUE_PATH))
        self.listaBloques.append(self.elBloque)

        self.fondo = pygame.image.load(BACKGROUND_PATH)
        self.fondorect = self.fondo.get_rect()
        # fps
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(1)



    def Maker(self):
        # Da valores iniciales a los contadores
        bgsound = 0

        presionado = [False, False]

        while 1:
            self.clock.tick(160)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            x, y = pygame.mouse.get_pos()



            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si se presiona el boton agregar
                if self.mas.get_rect(center=(BUTTON_MAS_POS)).collidepoint(x, y):
                    presionado[0] = True

            if event.type == pygame.MOUSEBUTTONUP:
                # Si se suelta el boton agregar
                if self.mas.get_rect(center=(BUTTON_MAS_POS)).collidepoint(x, y):
                    if presionado[0] == True:
                        presionado[0] = False
                        presionado[1] = True

            # Solo una llamada al metodo nuevo bloque
            if presionado[1] == True:
                self.nuevoBloques()
                presionado = [False, False]

            # dibuja el fondo
            self.screen.blit(self.fondo, self.fondorect)

            # dibuja los bloques
            for b in self.listaBloques:
                self.screen.blit(b.getBloque(), b.getBloque().get_rect(center=(b.getX(), b.getY())))

            self.mouseOver(x, y)

            self.displayFonts(x, y)

            # pone letras en pantalla


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

        Parametros:
        x -- posicion x del mouse
        y -- posicion y del mouse

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

        if self.mas.get_rect(center=(BUTTON_MAS_POS)).collidepoint(x, y):
            self.mas = pygame.image.load(BUTTON_MAS_RED_PATH)
            self.screen.blit(self.mas, self.mas.get_rect(center=(BUTTON_MAS_POS)))
        else:
            self.mas = pygame.image.load(BUTTON_MAS_PATH)
            self.screen.blit(self.mas, self.mas.get_rect(center=(BUTTON_MAS_POS)))


    def nuevoBloques(self):
        #TODO: a~adir

        print("Nuevo bloque")


if __name__ == '__main__':
    theGame = ArkathonMaker()
    theGame.Maker()