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
