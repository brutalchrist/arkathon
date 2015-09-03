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
