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

'Generales'
BACKGROUND_PATH = "data/sprite/background.png"
FONT_PATH = "data/font/arc.ttf"

BLOCK_BLUE_PATH = "data/sprite/block01.png"
BLOCK_YELLOW_PATH = "data/sprite/block02.png"
BLOCK_CALYPSO_PATH = "data/sprite/block03.png"
BLOCK_RED_PATH = "data/sprite/block04.png"
BLOCK_GREY_PATH = "data/sprite/block05.png"

LIST_BLOCKS = [BLOCK_BLUE_PATH, BLOCK_YELLOW_PATH, BLOCK_CALYPSO_PATH, BLOCK_RED_PATH, BLOCK_GREY_PATH]

LEFT_CLICK = 1
MIDDLE_CLICK = 2
RIGHT_CLICK = 3

"""
Constantes para el Maker
"""
'Botones'
BUTTON_UP_PATH = "data/sprite/up.png"
BUTTON_UP_RED_PATH = "data/sprite/up_red.png"
BUTTON_DOWN_PATH = "data/sprite/down.png"
BUTTON_DOWN_RED_PATH = "data/sprite/down_red.png"
BUTTON_MAS_PATH = "data/sprite/mas.png"
BUTTON_MAS_RED_PATH = "data/sprite/mas_red.png"

DE_DOSPUNTOS = "data/sprite/dedospuntos.png"

'Posiciones'
BUTTON_UP_POS = 490, 150
BUTTON_DOWN_POS = 490, 250
BUTTON_MAS_POS = 490, 300