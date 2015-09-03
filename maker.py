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

import pygame
from sys import exit
from os import environ

from classes.Constantes import *
from classes.Boton import Boton
from classes.Bloque import Bloque


class ArkathonMaker(object):
    def __init__(self):
        # permite centrar la ventana a la pantalla usando SDL
        environ['SDL_VIDEO_CENTERED'] = '1'
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
        self.up = Boton(pygame.image.load(BUTTON_UP_PATH))
        self.down = Boton(pygame.image.load(BUTTON_DOWN_PATH))
        self.mas = Boton(pygame.image.load(BUTTON_MAS_PATH))

        self.screen.blit(self.up.sprite, self.up.sprite.get_rect(center=(BUTTON_UP_POS)))
        self.screen.blit(self.down.sprite, self.down.sprite.get_rect(center=(BUTTON_DOWN_POS)))
        self.screen.blit(self.mas.sprite, self.mas.sprite.get_rect(center=(BUTTON_MAS_POS)))

        self.contadorListaBloques = 0

        self.listaBloques = []
        self.elBloque = Bloque()
        self.elBloque.setBloque(pygame.image.load(LIST_BLOCKS[self.contadorListaBloques]))
        self.listaBloques.append(self.elBloque)

        self.bloqueSeleccionado = False
        self.bloquesColicionados = False

        self.fondo = pygame.image.load(BACKGROUND_PATH)
        self.fondorect = self.fondo.get_rect()
        # fps
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(1)



    def Maker(self):
        # Da valores iniciales a los contadores
        bgsound = 0

        while True:
            self.clock.tick(160)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            x, y = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si se presiona el boton agregar
                if self.mas.sprite.get_rect(center=(BUTTON_MAS_POS)).collidepoint(x, y):
                    self.mas.downPush = True
                elif self.up.sprite.get_rect(center=(BUTTON_UP_POS)).collidepoint(x, y):
                    self.up.downPush = True
                elif self.down.sprite.get_rect(center=(BUTTON_DOWN_POS)).collidepoint(x, y):
                    self.down.downPush = True

                if event.button == RIGHT_CLICK:
                        if self.bloqueSeleccionado and  not self.bloquesColicionados:
                            self.bloqueSeleccionado = False

            if event.type == pygame.MOUSEBUTTONUP:
                # Si se suelta el boton agregar
                if self.mas.sprite.get_rect(center=(BUTTON_MAS_POS)).collidepoint(x, y):
                    if self.mas.downPush == True:
                        self.mas.downPush = False
                        self.mas.upPush = True
                elif self.up.sprite.get_rect(center=(BUTTON_UP_POS)).collidepoint(x, y):
                    if self.up.downPush == True:
                        self.up.downPush = False
                        self.up.upPush = True
                elif self.down.sprite.get_rect(center=(BUTTON_DOWN_POS)).collidepoint(x, y):
                    if self.down.downPush == True:
                        self.down.downPush = False
                        self.down.upPush = True

            # Solo una llamada al metodo nuevo bloque
            if self.mas.upPush == True:
                self.mas.restablecerEstados()
                self.nuevoBloque()
            elif self.up.upPush == True:
                self.up.restablecerEstados()
                self.elBloque.setBloque(pygame.image.load(self.anteriorBloque()))
            elif self.down.upPush == True:
                self.down.restablecerEstados()
                self.elBloque.setBloque(pygame.image.load(self.siguienteBloque()))

            if self.bloqueSeleccionado:
                self.elBloque.setX(x)
                self.elBloque.setY(y)

            # dibuja el fondo
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.fondo, self.fondorect)

            # tratamiento de bloques
            for b in self.listaBloques:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == LEFT_CLICK:
                        if b.rect.collidepoint(x, y):
                            self.focoBloque(b)
                            self.bloqueSeleccionado = True


                if self.elBloque.rect.colliderect(b.rect):
                    if self.elBloque != b:
                        self.elBloque.cambiarADE()
                        self.bloquesColicionados = True
                else:
                    self.elBloque.volverBloque()
                    self.bloquesColicionados = False

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
        if self.up.sprite.get_rect(center=(BUTTON_UP_POS)).collidepoint(x, y):
            self.up.sprite = pygame.image.load(BUTTON_UP_RED_PATH)
            self.screen.blit(self.up.sprite, self.up.sprite.get_rect(center=(BUTTON_UP_POS)))
        else:
            self.up.sprite = pygame.image.load(BUTTON_UP_PATH)
            self.screen.blit(self.up.sprite, self.up.sprite.get_rect(center=(BUTTON_UP_POS)))

        if self.down.sprite.get_rect(center=(BUTTON_DOWN_POS)).collidepoint(x, y):
            self.down.sprite = pygame.image.load(BUTTON_DOWN_RED_PATH)
            self.screen.blit(self.down.sprite, self.down.sprite.get_rect(center=(BUTTON_DOWN_POS)))
        else:
            self.down.sprite = pygame.image.load(BUTTON_DOWN_PATH)
            self.screen.blit(self.down.sprite, self.down.sprite.get_rect(center=(BUTTON_DOWN_POS)))

        if self.mas.sprite.get_rect(center=(BUTTON_MAS_POS)).collidepoint(x, y):
            self.mas.sprite = pygame.image.load(BUTTON_MAS_RED_PATH)
            self.screen.blit(self.mas.sprite, self.mas.sprite.get_rect(center=(BUTTON_MAS_POS)))
        else:
            self.mas.sprite = pygame.image.load(BUTTON_MAS_PATH)
            self.screen.blit(self.mas.sprite, self.mas.sprite.get_rect(center=(BUTTON_MAS_POS)))


    def nuevoBloque(self):
        self.elBloque = Bloque()
        self.elBloque.setBloque(pygame.image.load(self.siguienteBloque()))
        self.listaBloques.append(self.elBloque)

    def siguienteBloque(self):
        if self.contadorListaBloques == len(LIST_BLOCKS) - 1:
            self.contadorListaBloques = 0
        else:
            self.contadorListaBloques += 1

        return LIST_BLOCKS[self.contadorListaBloques]

    def anteriorBloque(self):
        if self.contadorListaBloques == 0:
            self.contadorListaBloques = len(LIST_BLOCKS) - 1
        else:
            self.contadorListaBloques -= 1

        return LIST_BLOCKS[self.contadorListaBloques]

    def focoBloque(self, bloque):
        self.elBloque = bloque


if __name__ == '__main__':
    theGame = ArkathonMaker()
    theGame.Maker()