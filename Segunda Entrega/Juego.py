import pygame
import configparser

ALTO=500
ANCHO=700
class Interfaz():
	def __init__(self, pantalla,  nivel, interprete):
		for i in interprete.items(nivel):
			#print(i)
			if i[0] == 'imagen':
				self.imagen = pygame.image.load(i[1]).convert_alpha()
			else:
				corte = self.imagen.subsurface(eval(interprete.get('cortes',i[0])))
				for pos in eval(i[1]):
					pantalla.blit(corte,pos)
		pygame.display.flip()

class Arbol(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('Arboles2.png').convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self):
		pass


class Casa(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imagen = pygame.image.load('pokemon2.png').convert_alpha()
		self.image = self.imagen.subsurface((1555,1744, 106, 82))
		self.rect=self.image.get_rect()

class Agua(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imagen = pygame.image.load('pokemon2.png').convert_alpha()
		self.image = self.imagen.subsurface((1555,1744, 106, 82))
		self.rect=self.image.get_rect()

class Bloque(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imagen = pygame.image.load('pokemon2.png').convert_alpha()
		self.image = self.imagen.subsurface((1555,1744, 106, 82))
		self.rect=self.image.get_rect()


class Jugador(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.imagen = pygame.image.load('pokemon2.png').convert_alpha()
		self.jugador = self.imagen.subsurface((1555,1744, 106, 82))
		self.dir = 0
		self.x = 0
		self.var_x = 0
		self.var_y = 0
		self.m = []
		for i in range(4):
			aux = []
			for j in range(3):
				aux.append(self.jugador.subsurface((i*30, j*30, 16, 22)))
			self.m.append(aux)
		self.image = self.m[self.dir][self.x]
		self.rect=self.image.get_rect()

	def update(self):
		self.rect.x+=self.var_x
		self.rect.y+=self.var_y
		if self.rect.x>=ANCHO-self.rect[2]:
			self.var_x=ANCHO-self.rect[2]
		if self.rect.x<=0:
			self.rect.x=0
			self.var_x=0
		if self.rect.y>=ALTO-self.rect[3]:
			self.var_y=ALTO-self.rect[3]
		if self.rect.y<=0:
			self.var_y=0
		self.image=self.m[self.dir][self.x]

if __name__=='__main__':
	pygame.init()
	pantalla=pygame.display.set_mode([ANCHO,ALTO])
	interprete=configparser.ConfigParser()
	interprete.read('Mapa.map')
	pantalla.fill((0,160,0))
	jp = Jugador()
	# V = Interfaz(pantalla, 'nivel1', interprete)

	general=pygame.sprite.Group()
	general.add(jp)
	objetos = pygame.sprite.Group()
	ar = Arbol(0,0)
	ar1 = Arbol(490,0)
	objetos.add(ar)
	general.add(ar)
	objetos.add(ar1)
	general.add(ar1)
	reloj=pygame.time.Clock()
	val = True
	while val:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				val=False
		pygame.display.flip()
		reloj.tick(60)
		general.draw(pantalla)
		pygame.display.flip()
