import pygame
import configparser
import random
import sys

ALTO=500
ANCHO=700

class Arbol(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('Arboles2.png').convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self):
		pass

class Maquina(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.imagen = pygame.image.load('pokemon2.png').convert_alpha()
		self.image = self.imagen.subsurface((850,710, 20, 33))
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		def update(self):
			pass

class Casa(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.imagen = pygame.image.load('pokemon2.png').convert_alpha()
		self.image = self.imagen.subsurface((5,5, 180, 50))
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		def update(self):
			pass

class Tienda(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.imagen = pygame.image.load('pokemon2.png').convert_alpha()
		self.image = self.imagen.subsurface((675,522, 230, 65))
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		def update(self):
			pass

class Gym(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.imagen = pygame.image.load('pokemon2.png').convert_alpha()
		self.image = self.imagen.subsurface((420,90, 120, 83))
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		def update(self):
			pass

class RioI(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('RioI2.png').convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self):
		pass

class RioD(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('RioD2.png').convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self):
		pass

class bloque(pygame.sprite.Sprite):
	def __init__(self,imagen,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = imagen.subsurface((288,288,32,32))
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Suelo(pygame.sprite.Sprite):
	def __init__(self,imagen,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('terrenogen.png').convert_alpha().subsurface((672,288,32,32))
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Disparo(pygame.sprite.Sprite):
	def __init__(self,x,y,var_x, grados):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.rotate(pygame.image.load('Goku1.png').convert_alpha().subsurface((388,130, 18, 18)),grados)
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.var_x = var_x

	def update(self):
		self.rect.x += self.var_x

class Barrera(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50, 500))
		self.image.fill((0,0,255))
		self.rect = self.image.get_rect()
		self.rect.x = -50
		self.rect.y = 0

class Jugador(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imagen = pygame.image.load('pokemon2.png').convert_alpha()
		self.jugador = self.imagen.subsurface((1555,1744, 106, 82))
		self.dir = 0
		self.x =0
		self.var_x = 0
		self.var_y = 0
		self.m = []
		self.aux = 0 
		for i in range(4):
			aux = []
			for j in range(3):
				aux.append(self.jugador.subsurface((i*30, j*30, 16, 22)))
			self.m.append(aux)
		self.image = self.m[self.dir][self.x]
		self.rect=self.image.get_rect()
		self.rect.y = 478

	def update(self):
		self.rect.x+=self.var_x
		self.rect.y+=self.var_y
		if pygame.sprite.spritecollide(jp, objetos, False) != []:
			self.rect.x -= self.var_x
			self.rect.y -= self.var_y
			self.var_x = 0
			self.var_y = 0
		self.aux += 1
		if self.aux == 5:
			self.aux = 0
		if (self.var_x != 0 or self.var_y != 0) and self.aux == 0:
			self.x += 1
		if self.rect.x>ANCHO-self.rect[2]:
			self.rect.x = ANCHO-self.rect[2]
			self.var_x = 0
		if self.rect.x<0:
			self.rect.x=0
			self.var_x=0
		if self.rect.y>ALTO-self.rect[3]:
			self.rect.y = ALTO-self.rect[3]
			self.var_y = 0
		if self.rect.y<0:
			self.rect.y=0
			self.var_y = 0
		if self.x > 2:
			self.x = 0
		self.image=self.m[self.dir][self.x]

class Goku(pygame.sprite.Sprite):
	corre = True
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.Vida = 156
		self.jugador = pygame.image.load('Goku1.png').convert_alpha()
		self.dir = 1
		self.x = 2
		self.var_x = 0
		self.var_y = 0
		self.m = []
		self.aux = 0 
		for i in range(3):
			aux = []
			for j in range(5):
				aux.append(pygame.transform.scale(self.jugador.subsurface((j*28+3, i*36+6+i, 25, 31)),(25,31)))
			self.m.append(aux)
		aux = []
		for i in self.m[1]:
			aux.append(pygame.transform.flip(i, True, False))
		self.m.append(aux)
		self.m.append([self.jugador.subsurface((356,120, 25, 31))])
		self.m.append([self.jugador.subsurface((305,156, 25, 31))])
		self.image = self.m[self.dir][self.x]
		self.rect=self.image.get_rect()
		self.rect.y = 469

	def update(self):
		self.rect.x+=self.var_x
		self.rect.y+=self.var_y
		if pygame.sprite.spritecollide(jp, objetos, False) != []:
			self.rect.x -= self.var_x
			self.rect.y -= self.var_y
			self.var_x = 0
			self.var_y = 0
		self.aux += 1
		if self.aux == 5:
			self.aux = 0
		if (self.var_x != 0 or self.var_y != 0) and self.aux == 0 and self.corre:
			self.x += 1
		if self.rect.x>ANCHO-self.rect[2]:
			self.rect.x = ANCHO-self.rect[2]
			self.var_x = 0
		if self.rect.x<0:
			self.rect.x=0
			self.var_x=0
		if self.rect.y>ALTO-self.rect[3]:
			self.rect.y = ALTO-self.rect[3]
			self.var_y = 0
		if self.rect.y<0:
			self.rect.y=0
			self.var_y = 0
		if self.x > 2:
			self.x = 0
		self.image=self.m[self.dir][self.x]

class Gotens(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.Vida = 156
		self.jugador = pygame.image.load('Gotens1.png').convert_alpha()
		self.dir = 0
		self.var_x = 0
		self.var_y = 0
		self.m = []
		# self.aux = 0 
		self.m.append(pygame.transform.flip(self.jugador.subsurface((38, 35, 23, 32)),True,False))
		self.m.append(self.jugador.subsurface((116, 105, 23, 32)))
		self.m.append(self.jugador.subsurface((40, 1, 23, 32)))
		self.m.append(pygame.transform.flip(self.jugador.subsurface((57, 285, 23, 32)),True,False))
		self.image = self.m[self.dir]
		self.rect=self.image.get_rect()
		self.rect.y = 0
		self.rect.x = 675

	def update(self):
		self.rect.y+=self.var_y
		# if self.rect.y>ALTO-self.rect[3]:
		# 	self.rect.y = ALTO-self.rect[3]
		# 	self.var_y = 0
		# if self.rect.y<0:
		# 	self.rect.y=0
		# 	self.var_y = 0
		# if self.x > 2:
		# 	self.x = 0
		self.image=self.m[self.dir]

class Gohan(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.Vida = 156
		self.jugador = pygame.image.load('Gohan1.png').convert_alpha()
		self.dir = 0
		self.var_x = 0
		self.var_y = 0
		self.m = []
		# self.aux = 0 
		self.m.append(self.jugador.subsurface((61, 72, 20, 32)))
		self.m.append(self.jugador.subsurface((180, 115, 23, 32)))
		self.m.append(self.jugador.subsurface((5, 259, 23, 32)))
		self.m.append(pygame.transform.flip(self.jugador.subsurface((65, 335, 23, 32)),True,False))
		self.image = self.m[self.dir]
		self.rect=self.image.get_rect()
		self.rect.y = 0
		self.rect.x = 675

	def update(self):
		self.rect.y+=self.var_y
		# if self.rect.y>ALTO-self.rect[3]:
		# 	self.rect.y = ALTO-self.rect[3]
		# 	self.var_y = 0
		# if self.rect.y<0:
		# 	self.rect.y=0
		# 	self.var_y = 0
		# if self.x > 2:
		# 	self.x = 0
		self.image=self.m[self.dir]

if __name__=='__main__':
	pygame.init()
	pantalla=pygame.display.set_mode([ANCHO,ALTO])
	nivel = 1
	#        1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2
	mapa = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
			[1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,0,0,1,0],
			[0,0,0,0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,0],
			[0,0,0,0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,0],
			[0,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,0,1,0],
			[0,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,0,1,0],
			[0,0,0,0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,0],
			[0,0,0,0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,1,1,0],
			[0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0],
			[0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0],
			[0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,0],
			[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0],
			[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
	Fuente = pygame.font.Font('Fuentes/A.C.M.E. Secret Agent.ttf', 25)
	pygame.mixer.music.load('pokemon.mp3')
	pygame.mixer.music.play(1)
	# todo el pedazo de aqui carga todos los jugadores, puente, agua, casas,
	jp = Jugador()
	puente = pygame.image.load('Puente2.png').convert_alpha()
	general = pygame.sprite.Group()
	Maquinas = pygame.sprite.Group()
	objetos = pygame.sprite.Group()
	disparos = pygame.sprite.Group()
	ar = Arbol(0,0)
	ar1 = Arbol(490,0)
	agua1 = RioI(0,228)
	agua2 = RioD(358,230)
	tienda = Tienda(210, 0)
	gym = Gym(500, 270)
	maquina1 = Maquina(445, 10)
	maquina2 = Maquina(465, 10)
	Imagen1 = pygame.transform.flip(pygame.image.load('CasaGoku1.jpg').convert_alpha(), True, False)
	BarraVida = pygame.transform.scale(pygame.image.load('BarraVida.png').convert_alpha(),(172,30))
	general.add(jp)
	objetos.add(ar)
	objetos.add(ar1)
	objetos.add(agua1)
	objetos.add(agua2)
	objetos.add(tienda)
	objetos.add(gym)
	Maquinas.add(maquina1)
	Maquinas.add(maquina2)
	for i in ((0, 400), (0, 300), (450, 400)):
		Casas = Casa(i[0],i[1])
		objetos.add(Casas)
	reloj=pygame.time.Clock()
	while True:
		while nivel == 1:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						sys.exit()
					if event.key == pygame.K_DOWN or event.key == pygame.K_s:
						jp.dir = 0
						jp.var_y = 1 
					if event.key == pygame.K_LEFT or event.key == pygame.K_a:
						jp.dir = 1
						jp.var_x = -1
					if event.key == pygame.K_UP or event.key == pygame.K_w:
						jp.dir = 2
						jp.var_y = -1 
					if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
						jp.dir = 3
						jp.var_x = 1 
				if event.type == pygame.KEYUP:
					jp.var_x = 0
					jp.var_y = 0
			jp.update()
			pantalla.fill((0,160,0))
			pantalla.blit(puente, (328,216))
			objetos.draw(pantalla)
			Maquinas.draw(pantalla)
			general.draw(pantalla)
			pygame.display.flip()
			reloj.tick(60)
		if nivel == 2:	
			Gk = Goku()
			general1 = pygame.sprite.Group()
			barreras = pygame.sprite.Group()
			general1.add(Gk)
			oponente = Gohan()
			general1.add(oponente)
			NumOponente = False
			barreras.add(Barrera())
			barre = Barrera()
			barre.rect.x = 700
			barreras.add(barre)
			segundos = int(pygame.time.get_ticks()/1000) + 120
			aux = 0
			aux1 = 0
		while nivel == 2:
			aux += 1
			aux1 += 1
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						sys.exit()
					if event.key == pygame.K_UP:
						Gk.var_y = -1
						Gk.dir = 4
						Gk.x = 0
						Gk.corre = False
					if event.key == pygame.K_DOWN:
						Gk.var_y = 1
						Gk.dir = 0
						Gk.x = 2
						Gk.corre = False
					if event.key == pygame.K_v:
						Gk.var_y = 0
						Gk.dir = 5
						Gk.x = 0
						Gk.corre = False
						disparos.add(Disparo(25, Gk.rect.y+8, 3, 90))
				if event.type == pygame.KEYUP:
					Gk.var_y = 0
					Gk.dir = 1
					Gk.x = 2
			Gk.update()
			if aux >= 50:
				if Gk.rect.y - oponente.rect.y > 0:
					oponente.var_y = 1
					oponente.dir = 2
				if Gk.rect.y - oponente.rect.y < 0:
					oponente.var_y = -1
					oponente.dir = 1
				if Gk.rect.y - oponente.rect.y == 0:
					oponente.var_y = 0
					# oponente.dir = 0
				aux = 0
			if abs(Gk.rect.y - oponente.rect.y) <= 30 and aux1 >= 20:
				oponente.dir = 3
				disparos.add(Disparo(657, oponente.rect.y+8, -5, 270))
				aux1 = 0
			if oponente.Vida <= 0 and not NumOponente:
				general1.remove(oponente)
				oponente = Gotens()
				general1.add(oponente)
			if pygame.sprite.spritecollide(Gk, disparos, True) != []:
				Gk.Vida -= 10
			if pygame.sprite.spritecollide(oponente, disparos, True) != []:
				oponente.Vida -= 10
			pygame.sprite.groupcollide(disparos, barreras, True, False)
			Texto1 = Fuente.render(str(segundos - int(pygame.time.get_ticks()/1000)), 0, (0, 0, 0))
			oponente.update()
			disparos.update()
			pantalla.blit(Imagen1, (0,0))
			barreras.draw(pantalla)
			pygame.draw.rect(pantalla,(255,0,0),(8, 9, Gk.Vida, 11))
			pantalla.blit(BarraVida, (0,0))
			pygame.draw.rect(pantalla,(255,0,0),(536, 9, oponente.Vida, 11))
			pantalla.blit(BarraVida, (528,0))
			general1.draw(pantalla)
			disparos.draw(pantalla)
			pantalla.blit(Texto1, (330,0))
			pygame.display.flip()
			reloj.tick(60)
		if nivel == 3:
			terreno = pygame.image.load('terrenogen.png').convert_alpha()
			Gk = Goku()
			Gk.rect.y = 32
			jug = pygame.sprite.Group()
			suelos = pygame.sprite.Group()
			bloques = pygame.sprite.Group()
			jug.add(Gk)
			for i in range(16):
				for j in range(22):
					if mapa[i][j]==0:
						bloques.add(bloque(terreno,j*32,i*32))
					if mapa[i][j]==1:
						suelos.add(Suelo(terreno,j*32,i*32))
		while nivel == 3:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						sys.exit()
					if event.key == pygame.K_DOWN or event.key == pygame.K_s:
						Gk.dir = 0
						Gk.var_y = 1 
					if event.key == pygame.K_LEFT or event.key == pygame.K_a:
						Gk.dir = 3
						Gk.var_x = -1
					if event.key == pygame.K_UP or event.key == pygame.K_w:
						Gk.dir = 2
						Gk.var_y = -1 
					if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
						Gk.dir = 1
						Gk.var_x = 1 
				if event.type == pygame.KEYUP:
					Gk.var_x = 0
					Gk.var_y = 0
			if pygame.sprite.spritecollide(Gk, bloques, False) != []:
				Gk.rect.x -= Gk.var_x
				Gk.rect.y -= Gk.var_y
				Gk.var_x = 0
				Gk.var_y = 0
			Gk.update()
			suelos.draw(pantalla)
			bloques.draw(pantalla)
			jug.draw(pantalla)
			pygame.display.flip()
			reloj.tick(60)