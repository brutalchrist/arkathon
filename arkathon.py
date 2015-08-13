# ARKATHON
#
# Carlos Albornoz
# http://carlos.debianchile.cl
# caralbornozc@gmail.com
#
# Sebastian Gonzalez
# http://sgonzalez.debianchile.cl
# brutalchrist@gmail.com
#
# 6 de Julio de 2008

# Graficos ripeados del juego Arkanoid original de TAITO (1987)
# Musica y sonidos ripeados del juego arkanoid returns  de TAITO (1997)

# Licencia GNU/GPL v2
# Si lo usas, por favor, reconoce nuestro trabajo

# -*- coding: utf-8 -*-

import sys, pygame, os, time
import ConfigParser
from string import maketrans
from pygame.locals import *


class Arkathon(object):
    def __init__(self):

        # permite centrar la ventana a la pantalla usando SDL
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        # Inicializa el mixer
        pygame.mixer.pre_init(44100, -16, 2, 5000)
        # asiga el tamano de la ventana
        self.size = self.width, self.height = 448, 512
        # asigna cuantos pixeles avanza en X e Y
        self.speed = [3, 3]
        self.bgsound = 0
        # high scores
        self.contador = 0
        self.lugar = 1
        self.hgScore = ConfigParser.ConfigParser()
        self.hgScore.read([".arkathon.scr"])
        # lalala
        self.scoreTablaVa = maketrans("1234567890", "tkg-csm!ja")
        self.nombreTablaVa = maketrans("qwertyuiopasdfghjklzxcvbnm", "qpwoeirutyghfjdkslazmxncvb")
        self.scoreTablaVie = maketrans("tkg-csm!ja", "1234567890")
        self.nombreTablaVie = maketrans("qpwoeirutyghfjdkslazmxncvb", "qwertyuiopasdfghjklzxcvbnm")
        # Variable para ver en la pantalla que va
        self.pantalla = 0
        # variable de dificultad
        self.nivel = 1
        # ejecuta la ventana
        self.screen = pygame.display.set_mode(self.size)
        # nombre del titulo de la ventana
        pygame.display.set_caption("Arkathon")
        # carga la imagen de la pelota
        self.ball = pygame.image.load("data/sprite/ball.png")
        # carga la barra
        self.barra = pygame.image.load("data/sprite/barra.png")
        # carga el fondo
        self.fondo = pygame.image.load("data/sprite/background.png")
        # carga la pantalla de inicio
        # self.index = pygame.image.load("data/sprite/index.png")
        # carga la pantalla gameover
        self.gameover = pygame.image.load("data/sprite/gameover.png")
        # carga la pantalla de menu y opciones
        self.menu = pygame.image.load("data/sprite/menubg.png")
        self.Mnuevo = pygame.image.load("data/sprite/inicio.png")
        self.Mopciones = pygame.image.load("data/sprite/opciones.png")
        self.Msalir = pygame.image.load("data/sprite/salir.png")
        self.MnuevoB = pygame.image.load("data/sprite/inicio_.png")
        self.MopcionesB = pygame.image.load("data/sprite/opciones_.png")
        self.MsalirB = pygame.image.load("data/sprite/salir_.png")
        self.Ovolver = pygame.image.load("data/sprite/volver.png")
        self.Omas = pygame.image.load("data/sprite/mas.png")
        self.Omenos = pygame.image.load("data/sprite/menos.png")
        self.BGOpciones = pygame.image.load("data/sprite/menuopciones.png")
        # cargamos la musica
        self.Mgameplay = pygame.mixer.Sound('data/sound/ogg/gameplay1.ogg')
        self.Mcblock = pygame.mixer.Sound('data/sound/ogg/choque_block.ogg')
        self.Mcborde = pygame.mixer.Sound('data/sound/ogg/choque_borde.ogg')
        self.Mcpad = pygame.mixer.Sound('data/sound/ogg/choque_pad.ogg')
        self.Mgameover = pygame.mixer.Sound('data/sound/ogg/gameover2.ogg')
        self.Mintro = pygame.mixer.Sound('data/sound/ogg/intro.ogg')
        self.Mend = pygame.mixer.Sound('data/sound/ogg/end.ogg')
        self.Mhs = pygame.mixer.Sound('data/sound/ogg/hs.ogg')
        # cargamos los blockes
        self.ba = pygame.image.load("data/sprite/block01.png")
        self.bb = pygame.image.load("data/sprite/block02.png")
        self.bc = pygame.image.load("data/sprite/block03.png")
        self.bd = pygame.image.load("data/sprite/block04.png")
        self.be = pygame.image.load("data/sprite/block05.png")
        self.baa = pygame.image.load("data/sprite/block01.png")
        self.bbb = pygame.image.load("data/sprite/block02.png")
        self.bcc = pygame.image.load("data/sprite/block03.png")
        self.bdd = pygame.image.load("data/sprite/block04.png")
        self.bee = pygame.image.load("data/sprite/block05.png")

        self.ballrect = self.ball.get_rect()
        self.barrarect = self.barra.get_rect()
        self.fondorect = self.fondo.get_rect()
        # fps
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(1)
        # pone la barra en el medio de la pantalla
        self.barrarect.midbottom = self.screen.get_rect().midbottom
        self.ballrect.midbottom = self.barrarect.midbottom
        self.vidas = 3

    def Jugar(self):
        # Da valores iniciales a los contadores

        inicio = 1
        bgsound = 0
        theGame.LlenarBloques()
        while 1:
            self.clock.tick(160)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # la bola no se mueve hasta ke se haga click
            if inicio == 0:
                self.ballrect = self.ballrect.move(self.speed)
            # verifica si toca con los bordes de la ventana
            if self.ballrect.left < 0 or self.ballrect.right > self.width:
                self.speed[0] = -self.speed[0]
                self.Mcborde.play()
            if self.ballrect.top < 0:  # or ballrect.bottom > height:
                self.speed[1] = -self.speed[1]
                self.Mcborde.play()
            if self.ballrect.bottom > self.height:
                inicio = 1
                self.vidas -= 1
            # permite saber la posicion del mouse y centrar la barra a ello
            self.barrarect.centerx = pygame.mouse.get_pos()[0]
            # permite ke la bola salga desde el PAD
            if inicio == 1:
                self.ballrect.centerx = self.barrarect.centerx - 3
                self.ballrect.centery = self.barrarect.centery - 16
                # vefirica el click del mouse para empesar
                if pygame.mouse.get_pressed()[0] == 1:
                    self.ballrect.centerx = self.barrarect.centerx - 3
                    self.ballrect.centery = self.barrarect.centery - 16
                    inicio = 0
                    if bgsound == 0:
                        self.Mgameplay.set_volume(0.7)
                        self.Mgameplay.play(-1)
                        bgsound = 1
                    # elif print 'bgsound ok'
            # dibuja el fondo, la bola y el pad
            self.screen.blit(self.fondo, self.fondorect)
            self.screen.blit(self.ball, self.ballrect)
            self.screen.blit(self.barra, self.barrarect)
            # pone letras en pantalla
            if pygame.font:
                scoreA = pant = puntaje = dificultad = font = pygame.font.Font("data/font/arc.ttf", 20)
                # tvida = pygame.font.Font("data/font/arc.ttf", 10)
                arkathonLogo = font.render('arkathon', 0, (255, 0, 0))
                score = puntaje.render('hi  ' + str(self.contador), 0, (255, 0, 0))
                panta = pant.render('stage  ' + str(self.pantalla), 0, (255, 0, 0))
                dificultadB = dificultad.render('nivel  ' + str(self.nivel), 0, (255, 0, 0))
                txtvida = font.render('P  ' + str(self.vidas), 0, (255, 0, 0))
                # scoreB = scoreA.render('Hi ', 0, (255, 0, 0))
                # self.screen.blit(scoreB, (5, 20))
                self.screen.blit(arkathonLogo, (180, 0))
                self.screen.blit(score, (10, 20))
                self.screen.blit(panta, (130, 20))
                self.screen.blit(dificultadB, (270, 20))
                self.screen.blit(txtvida, (410, 20))
            # si esta bX_activo activo lo dibujamos
            if self.ba_activo:
                self.screen.blit(self.ba, self.blockeA)
            if self.bb_activo:
                self.screen.blit(self.bb, self.blockeB)
            if self.bc_activo:
                self.screen.blit(self.bc, self.blockeC)
            if self.bd_activo:
                self.screen.blit(self.bd, self.blockeD)
            if self.be_activo:
                self.screen.blit(self.be, self.blockeE)
            if self.baa_activo:
                self.screen.blit(self.baa, self.blockeAA)
            if self.bbb_activo:
                self.screen.blit(self.bbb, self.blockeBB)
            if self.bcc_activo:
                self.screen.blit(self.bcc, self.blockeCC)
            if self.bdd_activo:
                self.screen.blit(self.bdd, self.blockeDD)
            if self.bee_activo:
                self.screen.blit(self.bee, self.blockeEE)
            # si la bola colisiona con la barra, la bola rebota en ella
            if self.barrarect.colliderect(self.ballrect):
                self.speed[1] = -self.speed[1]
                self.Mcpad.play()
            # si la bola colisiona con los blockes, la bola rebota en ella
            # y desaparecemos el blocke dandole a bX_activo = 0
            if self.blockeA.colliderect(self.ballrect):
                self.speed[1] = -self.speed[1]
                self.ba_activo = 0
                # SOLUCION CHANTA PARA DESAPARECER LOS BLOQUES
                # AL COLISIONAR LOS MUEVO FUERA DE LA VENTANA
                self.blockeA = self.ba.get_rect(center=(600, 600))
                # --------------------------------------------
                # genera puntaje por blockes destruidos
                self.contador += 5
            if self.blockeB.colliderect(self.ballrect):
                self.speed[1] = -self.speed[1]
                self.Mcblock.play()
                self.bb_activo = 0
                self.blockeB = self.bb.get_rect(center=(600, 600))
                self.contador += 10
            if self.blockeC.colliderect(self.ballrect):
                self.speed[1] = -self.speed[1]
                self.Mcblock.play()
                self.bc_activo = 0
                self.blockeC = self.bc.get_rect(center=(600, 600))
                self.contador += 15
            if self.blockeD.colliderect(self.ballrect):
                self.speed[1] = -self.speed[1]
                self.Mcblock.play()
                self.bd_activo = 0
                self.blockeD = self.bd.get_rect(center=(600, 600))
                self.contador += 20
            if self.blockeE.colliderect(self.ballrect):
                self.speed[1] = -self.speed[1]
                self.Mcblock.play()
                self.be_activo = 0
                self.blockeE = self.be.get_rect(center=(600, 600))
                self.contador += 25
            if self.blockeAA.colliderect(self.ballrect):
                self.speed[1] = -self.speed[1]
                self.Mcblock.play()
                self.baa_activo = 0
                self.blockeAA = self.baa.get_rect(center=(600, 600))
                self.contador += 5
            if self.blockeBB.colliderect(self.ballrect):
                self.speed[1] = -self.speed[1]
                self.Mcblock.play()
                self.bbb_activo = 0
                self.blockeBB = self.bbb.get_rect(center=(600, 600))
                self.contador += 10
            if self.blockeCC.colliderect(self.ballrect):
                self.speed[1] = -self.speed[1]
                self.Mcblock.play()
                self.bcc_activo = 0
                self.blockeCC = self.bcc.get_rect(center=(600, 600))
                self.contador += 15
            if self.blockeDD.colliderect(self.ballrect):
                self.speed[1] = -self.speed[1]
                self.Mcblock.play()
                self.bdd_activo = 0
                self.blockeDD = self.bdd.get_rect(center=(600, 600))
                self.contador += 20
            if self.blockeEE.colliderect(self.ballrect):
                self.speed[1] = -self.speed[1]
                self.Mcblock.play()
                self.bee_activo = 0
                self.blockeEE = self.bee.get_rect(center=(600, 600))
                self.contador += 25
            if self.ba_activo == 0 and self.bb_activo == 0 and self.bc_activo == 0 and self.bd_activo == 0 and self.be_activo == 0 and self.baa_activo == 0 and self.bbb_activo == 0 and self.bcc_activo == 0 and self.bdd_activo == 0 and self.bee_activo == 0:
                # Llenamos los bloques
                theGame.LlenarBloques()
            if self.vidas <= 0:
                inicio = 1
                # pygame.time.wait(3000)
                self.pantalla = 0
                self.vidas = 3
                self.primeroNombre = self.hgScore.get("primero", "nombre")
                self.primeroScore = self.hgScore.get("primero", "score")
                self.segundoNombre = self.hgScore.get("segundo", "nombre")
                self.segundoScore = self.hgScore.get("segundo", "score")
                self.terceroNombre = self.hgScore.get("tercero", "nombre")
                self.terceroScore = self.hgScore.get("tercero", "score")
                if int(self.primeroScore.translate(self.scoreTablaVie)) < self.contador:
                    self.hgScore.set("tercero", "score", self.segundoScore)
                    self.hgScore.set("segundo", "score", self.primeroScore)
                    self.hgScore.set("primero", "score", str(self.contador).translate(self.scoreTablaVa))
                    self.lugar = 1
                    self.contador = 0
                    theGame.highScore()
                elif int(self.primeroScore.translate(self.scoreTablaVie)) == self.contador:
                    self.hgScore.set("tercero", "score", self.segundoScore)
                    self.hgScore.set("segundo", "score", self.primeroScore)
                    self.hgScore.set("primero", "score", str(self.contador).translate(self.scoreTablaVa))
                    self.lugar = 1
                    self.contador = 0
                    theGame.highScore()
                elif int(self.segundoScore.translate(self.scoreTablaVie)) < self.contador:
                    self.hgScore.set("tercero", "score", self.segundoScore)
                    self.hgScore.set("segundo", "score", str(self.contador).translate(self.scoreTablaVa))
                    self.lugar = 2
                    self.contador = 0
                    theGame.highScore()
                elif int(self.segundoScore.translate(self.scoreTablaVie)) == self.contador:
                    self.hgScore.set("tercero", "score", self.segundoScore)
                    self.hgScore.set("segundo", "score", str(self.contador).translate(self.scoreTablaVa))
                    self.lugar = 2
                    self.contador = 0
                    theGame.highScore()
                elif int(self.terceroScore.translate(self.scoreTablaVie)) < self.contador:
                    self.hgScore.set("tercero", "score", str(self.contador).translate(self.scoreTablaVa))
                    self.lugar = 3
                    self.contador = 0
                    theGame.highScore()
                elif int(self.terceroScore.translate(self.scoreTablaVie)) == self.contador:
                    self.hgScore.set("tercero", "score", str(self.contador).translate(self.scoreTablaVa))
                    self.lugar = 3
                    self.contador = 0
                    theGame.highScore()

                f = open(".arkathon.scr", "w")
                self.hgScore.write(f)
                f.close()

                self.contador = 0

                theGame.gameOver()
            pygame.display.flip()

    def LlenarBloques(self):
        # Vuelve la pelota a la barra
        self.ballrect.centerx = self.barrarect.centerx - 3
        self.ballrect.centery = self.barrarect.centery - 16

        self.pantalla = self.pantalla + 1
        # leemos el archivo de la carpeta ventana
        try:
            Apantalla = open('data/pantallas/' + str(self.pantalla), 'r')
            # inicializamos con 1 para ke los blockes vuelvan a activarse
            self.ba_activo = self.bb_activo = self.bc_activo = self.bd_activo = self.be_activo = 1
            self.baa_activo = self.bbb_activo = self.bcc_activo = self.bdd_activo = self.bee_activo = 1

            # le damos la posicion a los blockes
            # Lellendo de los archivos de pantallas
            a = Apantalla.read(3)
            basura = Apantalla.read(1)
            b = Apantalla.read(3)
            basura = Apantalla.read(1)
            self.blockeA = self.ba.get_rect(center=(int(a), int(b)))
            a = Apantalla.read(3)
            basura = Apantalla.read(1)
            b = Apantalla.read(3)
            basura = Apantalla.read(1)
            self.blockeB = self.bb.get_rect(center=(int(a), int(b)))
            a = Apantalla.read(3)
            basura = Apantalla.read(1)
            b = Apantalla.read(3)
            basura = Apantalla.read(1)
            self.blockeC = self.bc.get_rect(center=(int(a), int(b)))
            a = Apantalla.read(3)
            basura = Apantalla.read(1)
            b = Apantalla.read(3)
            basura = Apantalla.read(1)
            self.blockeD = self.bd.get_rect(center=(int(a), int(b)))
            a = Apantalla.read(3)
            basura = Apantalla.read(1)
            b = Apantalla.read(3)
            basura = Apantalla.read(1)
            self.blockeE = self.be.get_rect(center=(int(a), int(b)))
            a = Apantalla.read(3)
            basura = Apantalla.read(1)
            b = Apantalla.read(3)
            basura = Apantalla.read(1)
            self.blockeAA = self.baa.get_rect(center=(int(a), int(b)))
            a = Apantalla.read(3)
            basura = Apantalla.read(1)
            b = Apantalla.read(3)
            basura = Apantalla.read(1)
            self.blockeBB = self.bbb.get_rect(center=(int(a), int(b)))
            a = Apantalla.read(3)
            basura = Apantalla.read(1)
            b = Apantalla.read(3)
            basura = Apantalla.read(1)
            self.blockeCC = self.bcc.get_rect(center=(int(a), int(b)))
            a = Apantalla.read(3)
            basura = Apantalla.read(1)
            b = Apantalla.read(3)
            basura = Apantalla.read(1)
            self.blockeDD = self.bdd.get_rect(center=(int(a), int(b)))
            a = Apantalla.read(3)
            basura = Apantalla.read(1)
            b = Apantalla.read(3)
            basura = Apantalla.read(1)
            self.blockeEE = self.bee.get_rect(center=(int(a), int(b)))
            # si esta bX_activo activo lo dibujamos
            self.screen.blit(self.ba, self.blockeA)
            self.screen.blit(self.bb, self.blockeB)
            self.screen.blit(self.bc, self.blockeC)
            self.screen.blit(self.bd, self.blockeD)
            self.screen.blit(self.be, self.blockeE)
            self.screen.blit(self.baa, self.blockeAA)
            self.screen.blit(self.bbb, self.blockeBB)
            self.screen.blit(self.bcc, self.blockeCC)
            self.screen.blit(self.bdd, self.blockeDD)
            self.screen.blit(self.bee, self.blockeEE)
        except IOError:
            self.pantalla = 0

    def Menu(self):
        # bgsound = 0
        while 1:
            self.screen.blit(self.menu, self.menu.get_rect())
            self.screen.blit(self.Mnuevo, self.Mnuevo.get_rect(center=(224, 270)))
            self.screen.blit(self.Mopciones, self.Mopciones.get_rect(center=(224, 300)))
            self.screen.blit(self.Msalir, self.Msalir.get_rect(center=(224, 330)))
            mousepos = pygame.mouse.get_pos()
            if self.bgsound == 0:
                self.Mintro.set_volume(0.7)
                self.Mintro.play(-1)
                self.bgsound = 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.Mnuevo.get_rect(center=(224, 270)).collidepoint(x, y):
                        self.Mintro.stop()
                        theGame.Jugar()
                    elif self.Mopciones.get_rect(center=(224, 300)).collidepoint(x, y):
                        theGame.Opciones()
                    elif self.Msalir.get_rect(center=(224, 330)).collidepoint(x, y):
                        sys.exit()
            ''' permite simular el mouse over del menu '''
            if self.Mnuevo.get_rect(center=(224, 270)).collidepoint(mousepos):
                self.screen.blit(self.MnuevoB, self.MnuevoB.get_rect(center=(224, 270)))
            elif self.Mopciones.get_rect(center=(224, 300)).collidepoint(mousepos):
                self.screen.blit(self.MopcionesB, self.MopcionesB.get_rect(center=(224, 300)))
            elif self.Msalir.get_rect(center=(224, 330)).collidepoint(mousepos):
                self.screen.blit(self.MsalirB, self.MsalirB.get_rect(center=(224, 330)))

            pygame.display.flip()

    def Opciones(self):
        bgsound = 0
        # self.Mintro.stop()
        self.tvida = pygame.font.Font("data/font/arc.ttf", 40)
        while 1:
            self.screen.blit(self.BGOpciones, self.BGOpciones.get_rect())
            self.screen.blit(self.Ovolver, self.Ovolver.get_rect(center=(224, 400)))
            self.screen.blit(self.Omas, self.Omas.get_rect(center=(300, 302)))
            self.screen.blit(self.Omenos, self.Omenos.get_rect(center=(340, 302)))
            self.txtvidas = self.tvida.render(str(self.vidas), 0, (255, 0, 0))
            self.screen.blit(self.txtvidas, (230, 283))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.Ovolver.get_rect(center=(224, 400)).collidepoint(x, y):
                        theGame.Menu()
                    elif self.Omas.get_rect(center=(300, 302)).collidepoint(x, y):
                        if self.vidas < 9:
                            self.vidas = self.vidas + 1
                    elif self.Omenos.get_rect(center=(340, 302)).collidepoint(x, y):
                        if self.vidas == 1:
                            continue
                        else:
                            self.vidas = self.vidas - 1

            pygame.display.flip()

    def highScore(self):
        bgsound = 0
        lista = []
        borrar = pygame.image.load("data/abc/borrar.png")
        self.Mgameplay.stop()

        # self.screen.blit(self.hs, self.hs.get_rect())
        self.screen.blit(self.menu, self.menu.get_rect())

        while 1:
            if bgsound == 0:
                self.Mend.set_volume(0.4)
                self.Mhs.play(-1)
                bgsound = 1
            if pygame.font:
                mensaje = pygame.font.Font("data/font/arc.ttf", 40)
                n1 = pygame.font.Font("data/font/arc.ttf", 60)
                n2 = pygame.font.Font("data/font/arc.ttf", 60)
                n3 = pygame.font.Font("data/font/arc.ttf", 60)
                mmensaje = mensaje.render('new  record!', 0, (255, 0, 0))
                self.screen.blit(mmensaje, (110, 190))

                if len(lista) == 0:
                    self.screen.blit(borrar, (130, 430))
                if len(lista) == 1:
                    mn1 = n1.render(lista[0], 0, (255, 0, 0))
                    self.screen.blit(mn1, (130, 430))
                    self.screen.blit(borrar, (200, 430))
                    self.screen.blit(borrar, (270, 430))
                if len(lista) == 2:
                    mn2 = n2.render(lista[1], 0, (255, 0, 0))
                    self.screen.blit(mn2, (200, 430))
                    self.screen.blit(borrar, (270, 430))
                if len(lista) == 3:
                    mn3 = n3.render(lista[2], 0, (255, 0, 0))
                    self.screen.blit(mn3, (270, 430))

            m0 = pygame.image.load("data/abc/0.png")
            m1 = pygame.image.load("data/abc/1.png")
            m2 = pygame.image.load("data/abc/2.png")
            m3 = pygame.image.load("data/abc/3.png")
            m4 = pygame.image.load("data/abc/4.png")
            m5 = pygame.image.load("data/abc/5.png")
            m6 = pygame.image.load("data/abc/6.png")
            m7 = pygame.image.load("data/abc/7.png")
            m8 = pygame.image.load("data/abc/8.png")
            m9 = pygame.image.load("data/abc/9.png")
            mq = pygame.image.load("data/abc/q.png")
            mw = pygame.image.load("data/abc/w.png")
            me = pygame.image.load("data/abc/e.png")
            mr = pygame.image.load("data/abc/r.png")
            mt = pygame.image.load("data/abc/t.png")
            my = pygame.image.load("data/abc/y.png")
            mu = pygame.image.load("data/abc/u.png")
            mi = pygame.image.load("data/abc/i.png")
            mo = pygame.image.load("data/abc/o.png")
            mp = pygame.image.load("data/abc/p.png")
            ma = pygame.image.load("data/abc/a.png")
            ms = pygame.image.load("data/abc/s.png")
            md = pygame.image.load("data/abc/d.png")
            mf = pygame.image.load("data/abc/f.png")
            mg = pygame.image.load("data/abc/g.png")
            mh = pygame.image.load("data/abc/h.png")
            mj = pygame.image.load("data/abc/j.png")
            mk = pygame.image.load("data/abc/k.png")
            ml = pygame.image.load("data/abc/l.png")
            mz = pygame.image.load("data/abc/z.png")
            mx = pygame.image.load("data/abc/x.png")
            mc = pygame.image.load("data/abc/c.png")
            mv = pygame.image.load("data/abc/v.png")
            mb = pygame.image.load("data/abc/b.png")
            mn = pygame.image.load("data/abc/n.png")
            mm = pygame.image.load("data/abc/m.png")
            mok = pygame.image.load("data/abc/ok.png")
            mpto = pygame.image.load("data/abc/pto.png")
            mexc = pygame.image.load("data/abc/exc.png")
            merrase = pygame.image.load("data/abc/errase.png")

            mmq = mq.get_rect(center=(90, 260))
            mmw = mw.get_rect(center=(120, 260))
            mme = me.get_rect(center=(150, 260))
            mmr = mr.get_rect(center=(180, 260))
            mmt = mt.get_rect(center=(210, 260))
            mmy = my.get_rect(center=(240, 260))
            mmu = mu.get_rect(center=(270, 260))
            mmi = mi.get_rect(center=(300, 260))
            mmo = mo.get_rect(center=(330, 260))
            mmp = mp.get_rect(center=(360, 260))
            mma = ma.get_rect(center=(90, 300))
            mms = ms.get_rect(center=(120, 300))
            mmd = md.get_rect(center=(150, 300))
            mmf = mf.get_rect(center=(180, 300))
            mmg = mg.get_rect(center=(210, 300))
            mmh = mh.get_rect(center=(240, 300))
            mmj = mj.get_rect(center=(270, 300))
            mmk = mk.get_rect(center=(300, 300))
            mml = ml.get_rect(center=(330, 300))
            mmz = mz.get_rect(center=(360, 300))
            mmx = mx.get_rect(center=(90, 340))
            mmc = mc.get_rect(center=(120, 340))
            mmv = mv.get_rect(center=(150, 340))
            mmb = mb.get_rect(center=(180, 340))
            mmn = mn.get_rect(center=(210, 340))
            mmm = mm.get_rect(center=(240, 340))
            mmpto = mpto.get_rect(center=(270, 340))
            mmexc = mexc.get_rect(center=(300, 340))
            mmok = mok.get_rect(center=(330, 340))
            mmerrase = merrase.get_rect(center=(360, 340))
            mm0 = m0.get_rect(center=(90, 380))
            mm1 = m1.get_rect(center=(120, 380))
            mm2 = m2.get_rect(center=(150, 380))
            mm3 = m3.get_rect(center=(180, 380))
            mm4 = m4.get_rect(center=(210, 380))
            mm5 = m5.get_rect(center=(240, 380))
            mm6 = m6.get_rect(center=(270, 380))
            mm7 = m7.get_rect(center=(300, 380))
            mm8 = m8.get_rect(center=(330, 380))
            mm9 = m9.get_rect(center=(360, 380))

            self.screen.blit(mq, mmq)
            self.screen.blit(mw, mmw)
            self.screen.blit(me, mme)
            self.screen.blit(mr, mmr)
            self.screen.blit(mt, mmt)
            self.screen.blit(my, mmy)
            self.screen.blit(mu, mmu)
            self.screen.blit(mi, mmi)
            self.screen.blit(mo, mmo)
            self.screen.blit(mp, mmp)
            self.screen.blit(ma, mma)
            self.screen.blit(ms, mms)
            self.screen.blit(md, mmd)
            self.screen.blit(mf, mmf)
            self.screen.blit(mg, mmg)
            self.screen.blit(mh, mmh)
            self.screen.blit(mj, mmj)
            self.screen.blit(mk, mmk)
            self.screen.blit(ml, mml)
            self.screen.blit(mz, mmz)
            self.screen.blit(mx, mmx)
            self.screen.blit(mc, mmc)
            self.screen.blit(mv, mmv)
            self.screen.blit(mb, mmb)
            self.screen.blit(mn, mmn)
            self.screen.blit(mm, mmm)
            self.screen.blit(mpto, mmpto)
            self.screen.blit(mexc, mmexc)
            self.screen.blit(mok, mmok)
            self.screen.blit(merrase, mmerrase)
            self.screen.blit(m0, mm0)
            self.screen.blit(m1, mm1)
            self.screen.blit(m2, mm2)
            self.screen.blit(m3, mm3)
            self.screen.blit(m4, mm4)
            self.screen.blit(m5, mm5)
            self.screen.blit(m6, mm6)
            self.screen.blit(m7, mm7)
            self.screen.blit(m8, mm8)
            self.screen.blit(m9, mm9)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if mmq.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("q")
                    elif mmw.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("w")
                    elif mme.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("e")
                    elif mmr.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("r")
                    elif mmt.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("t")
                    elif mmy.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("y")
                    elif mmu.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("u")
                    elif mmi.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("i")
                    elif mmo.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("o")
                    elif mmp.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("p")
                    elif mma.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("a")
                    elif mms.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("s")
                    elif mmd.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("d")
                    elif mmf.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("f")
                    elif mmg.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("g")
                    elif mmh.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("h")
                    elif mmj.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("j")
                    elif mmk.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("k")
                    elif mml.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("l")
                    elif mmz.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("z")
                    elif mmx.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("x")
                    elif mmc.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("c")
                    elif mmv.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("v")
                    elif mmb.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("b")
                    elif mmn.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("n")
                    elif mmm.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("m")
                    elif mm0.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("0")
                    elif mm1.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("1")
                    elif mm2.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("2")
                    elif mm3.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("3")
                    elif mm4.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("4")
                    elif mm5.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("5")
                    elif mm6.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("6")
                    elif mm7.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("7")
                    elif mm8.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("8")
                    elif mm9.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("9")
                    elif mmpto.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append(".")
                    elif mmexc.collidepoint(x, y):
                        if len(lista) < 3:
                            lista.append("!")
                    elif mmerrase.collidepoint(x, y):
                        if len(lista) > 0:
                            lista.pop()
                    elif mmok.collidepoint(x, y):
                        if self.lugar == 1:
                            if len(lista) == 0:
                                self.hgScore.set("tercero", "nombre", self.segundoNombre)
                                self.hgScore.set("segundo", "nombre", self.primeroNombre)
                                self.hgScore.set("primero", "nombre", "   ".translate(self.nombreTablaVa))
                            elif len(lista) == 1:
                                name = str(lista[0]) + "  "
                                self.hgScore.set("tercero", "nombre", self.segundoNombre)
                                self.hgScore.set("segundo", "nombre", self.primeroNombre)
                                self.hgScore.set("primero", "nombre", name.translate(self.nombreTablaVa))
                            elif len(lista) == 2:
                                name = str(lista[0]) + str(lista[1]) + " "
                                self.hgScore.set("tercero", "nombre", self.segundoNombre)
                                self.hgScore.set("segundo", "nombre", self.primeroNombre)
                                self.hgScore.set("primero", "nombre", name.translate(self.nombreTablaVa))
                            elif len(lista) == 3:
                                name = str(lista[0]) + str(lista[1]) + str(lista[2])
                                self.hgScore.set("tercero", "nombre", self.segundoNombre)
                                self.hgScore.set("segundo", "nombre", self.primeroNombre)
                                self.hgScore.set("primero", "nombre", name.translate(self.nombreTablaVa))
                        elif self.lugar == 2:
                            if len(lista) == 0:
                                self.hgScore.set("tercero", "nombre", self.segundoNombre)
                                self.hgScore.set("segundo", "nombre", "   ".translate(self.nombreTablaVa))
                            elif len(lista) == 1:
                                name = str(lista[0]) + "  "
                                self.hgScore.set("tercero", "nombre", self.segundoNombre)
                                self.hgScore.set("segundo", "nombre", name.translate(self.nombreTablaVa))
                            elif len(lista) == 2:
                                name = str(lista[0]) + str(lista[1]) + " "
                                self.hgScore.set("tercero", "nombre", self.segundoNombre)
                                self.hgScore.set("segundo", "nombre", name.translate(self.nombreTablaVa))
                            elif len(lista) == 3:
                                name = str(lista[0]) + str(lista[1]) + str(lista[2])
                                self.hgScore.set("tercero", "nombre", self.segundoNombre)
                                self.hgScore.set("segundo", "nombre", name.translate(self.nombreTablaVa))
                        elif self.lugar == 3:
                            if len(lista) == 0:
                                self.hgScore.set("tercero", "nombre", "   ".translate(self.nombreTablaVa))
                            elif len(lista) == 1:
                                name = str(lista[0]) + "  "
                                self.hgScore.set("tercero", "nombre", name.translate(self.nombreTablaVa))
                            elif len(lista) == 2:
                                name = str(lista[0]) + str(lista[1]) + " "
                                self.hgScore.set("tercero", "nombre", name.translate(self.nombreTablaVa))
                            elif len(lista) == 3:
                                name = str(lista[0]) + str(lista[1]) + str(lista[2])
                                self.hgScore.set("tercero", "nombre", name.translate(self.nombreTablaVa))
                        f = open(".arkathon.scr", "w")
                        self.hgScore.write(f)
                        f.close()
                        theGame.mostrarHighScore()

            pygame.display.flip()

    def gameOver(self):
        bgsound = 0
        self.Mgameplay.stop()
        self.Mhs.stop()
        self.screen.blit(self.gameover, self.gameover.get_rect())
        while 1:
            if bgsound == 0:
                self.Mend.set_volume(0.4)
                self.Mend.play(-1)
                bgsound == 1
            for event in pygame.event.get():
                if pygame.mouse.get_pressed()[0] == 1:
                    bgsound = 0
                    self.bgsound = 0
                    self.Mend.stop()
                    theGame.Menu()
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

    def mostrarHighScore(self):
        self.screen.blit(self.menu, self.menu.get_rect())
        while 1:
            if pygame.font:
                n1 = pygame.font.Font("data/font/arc.ttf", 40)
                n2 = pygame.font.Font("data/font/arc.ttf", 40)
                n3 = pygame.font.Font("data/font/arc.ttf", 40)
                n1score = pygame.font.Font("data/font/arc.ttf", 40)
                n2score = pygame.font.Font("data/font/arc.ttf", 40)
                n3score = pygame.font.Font("data/font/arc.ttf", 40)
                n1 = n1.render('1. ' + str(self.hgScore.get("primero", "nombre")).translate(self.nombreTablaVie), 0,
                               (255, 0, 0))
                n2 = n2.render('2. ' + str(self.hgScore.get("segundo", "nombre")).translate(self.nombreTablaVie), 0,
                               (255, 0, 0))
                n3 = n3.render('3. ' + str(self.hgScore.get("tercero", "nombre")).translate(self.nombreTablaVie), 0,
                               (255, 0, 0))
                n1score = n1score.render(str(self.hgScore.get("primero", "score")).translate(self.scoreTablaVie), 0,
                                         (255, 255, 255))
                n2score = n2score.render(str(self.hgScore.get("segundo", "score")).translate(self.scoreTablaVie), 0,
                                         (255, 255, 255))
                n3score = n3score.render(str(self.hgScore.get("tercero", "score")).translate(self.scoreTablaVie), 0,
                                         (255, 255, 255))
                self.screen.blit(n1, (110, 270))
                self.screen.blit(n2, (110, 300))
                self.screen.blit(n3, (110, 330))
                self.screen.blit(n1score, (300, 270))
                self.screen.blit(n2score, (300, 300))
                self.screen.blit(n3score, (300, 330))

            for event in pygame.event.get():
                # if pygame.mouse.get_pressed()[0] == 1:
                # bgsound = 0
                # self.bgsound = 0
                # self.Mend.stop()
                # theGame.gameOver()
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()
            time.sleep(10)
            self.bgsound = 0
            theGame.gameOver()


theGame = Arkathon()
theGame.Menu()
