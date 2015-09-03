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

from pygame import image
from Constantes import DE_DOSPUNTOS

class Bloque(object):
    #TODO: Cambiar los getters and setter a la PythonWay.
    def __init__(self):
        self.bloque = None
        self.rect = None
        self.x = 490
        self.y = 200

        self.temp = None

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

    @property
    def rect(self):
        self.rect = self.bloque.get_rect(center=(self.x, self.y))
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    def getPos(self):
        return int(self.x), int(self.y)

    def cambiarADE(self):
        if self.temp == None:
            self.temp = self.bloque.copy()
            self.bloque = image.load(DE_DOSPUNTOS)

    def volverBloque(self):
        if self.temp != None:
            self.bloque = self.temp
            self.temp = None