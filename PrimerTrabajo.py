import pygame
import random 


ALTO=400
ANCHO=600
ROJO=(255,0,0)
BLANCO=(255,255,255)
AZUL=(59,131,189)
VERDE=(0,255,0)
centro=[ANCHO/2,ALTO/2]

class InterfasInicio(pygame.sprite.Sprite):
	pygame.font.init()
	Fuente1 = pygame.font.Font(None, 46)
	Fuente2 = pygame.font.Font(None, 36)
	Texto1 = Fuente1.render("BIENVENIDO", 0, (0, 0, 0))
	Texto2 = Fuente2.render("Comenzar",0, (0, 0, 0))
	Texto3 = Fuente2.render("Ayuda", 0, (0, 0, 0))
	y = 200
	Selector = pygame.Surface((20, 20))
	Selector.fill(ROJO)
	def __init__(self, p):
		self.p = p
		p.fill(BLANCO)
		p.blit(self.Texto1, (210, 100))
		p.blit(self.Texto2, (250, 200))
		p.blit(self.Texto3, (250, 250))
		p.blit(self.Selector, (219,self.y))
		pygame.display.flip()

	def mov(self, y):
		self.y += y
		if(self.y < 200):
			self.y = 250;
		if(self.y > 250):
			self.y = 200;
		self.update()

	def update(self):
		self.p.fill(BLANCO)
		self.p.blit(self.Texto1, (210, 100))
		self.p.blit(self.Texto2, (250, 200))
		self.p.blit(self.Texto3, (250, 250))
		self.p.blit(self.Selector, (219,self.y))
		pygame.display.flip()

class InterfasGameOver(pygame.sprite.Sprite):
	Fuente1 = pygame.font.Font(None, 60)
	Fuente2 = pygame.font.Font(None, 20)
	Texto1 = Fuente1.render("GAME OVER", 0, (0, 0, 225))
	Texto2 = Fuente2.render("APRETAR ENTER PARA CONTINUAR",0, (0, 0, 225))
	def __init__(self, p):
		p.blit(self.Texto1, (170, 200))
		p.blit(self.Texto2, (175, 150))
		pygame.display.flip()

class Jugador(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((80, 10))
		self.image.fill((255,0,0))
		self.rect = self.image.get_rect()
		self.var_x = 0
		self.rect.y = 340
		self.rect.x = 200

	def update(self):
		if self.rect.x + self.var_x >= ANCHO - 80:
			self.var_x = 0
		if self.rect.x + self.var_x <= 0:
			self.var_x = 0
		self.rect.x += self.var_x

class Rival(pygame.sprite.Sprite):
	def __init__(self, an, al):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((an, al))
		self.image.fill(AZUL)
		self.rect = self.image.get_rect()
		self.var_x = 0
		self.var_y = 2
		self.rect.x = random.randrange(10, ANCHO-20)
		self.rect.y = random.randrange(-400, 0)

	def update(self):
		self.rect.y += self.var_y
		self.rect.x += self.var_x
		if self.rect.x >= ANCHO-self.rect[2]:
			self.var_x = -2
		if self.rect.x <= 0:
			self.var_x = 2
		if self.rect.y <= 0:
			self.var_y = 2

class Bala(pygame.sprite.Sprite):
	def __init__(self, an, al, x):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((an, al))
		self.image.fill((255,0,0))
		self.rect = self.image.get_rect()
		self.var_y = -2
		self.rect.x = x + 40
		self.rect.y = 330 
	def update(self):
		self.rect.y += self.var_y

class Barrera(pygame.sprite.Sprite):
	def __init__(self, an, al):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((an, al))
		self.image.fill((0,0,255))
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 350

if __name__ == '__main__':
	pygame.init()
	niveles = 0
	pantalla = pygame.display.set_mode([ANCHO,ALTO])
	reloj=pygame.time.Clock()
	validacion = True

	while validacion:
		if niveles == 0:
			inicio = InterfasInicio(pantalla)
			val = True
			while val:
				reloj.tick(60)
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_UP:
							inicio.mov(-50)
						if event.key == pygame.K_DOWN:
							inicio.mov(50)
						if (event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN):
							if inicio.y == 200:
								niveles = 1
								val = False
						if event.key == pygame.K_ESCAPE:
							validacion = False
							val = False
					if event.type == pygame.QUIT:
						validacion = False
						val = False

		if niveles ==1:
			val = True
			jg = Jugador()
			bar = Barrera(ANCHO,50)
			bar1 = Barrera(ANCHO,10)
			bar1.rect.y = -10
			tiempo = 0
			vida = 3
			puntaje = 0
			general = pygame.sprite.Group()
			rivales = pygame.sprite.Group()
			barreras = pygame.sprite.Group()
			Balas = pygame.sprite.Group()
			general.add(jg)
			general.add(bar)
			barreras.add(bar)
			general.add(bar1)
			barreras.add(bar1)
			while val:
				if tiempo == 50:
					r = Rival(20,20)
					r.var_x = 2
					general.add(r)
					rivales.add(r)
				if tiempo == 0:
					r = Rival(20,20)
					general.add(r)
					rivales.add(r)
					tiempo = 100
				else:
					tiempo -= 1
				reloj.tick(60)
				general.draw(pantalla)
				for i in range(vida):
					pygame.draw.rect(pantalla,(255,0,0), (20 + i*25,365,20,20), 0)
				Fuente2 = pygame.font.Font(None, 25)
				Texto2 = Fuente2.render("PUNTAJE : "+ str(puntaje),0, (0, 0, 0))
				pantalla.blit(Texto2, (400, 365))
				pygame.display.flip()
				pantalla.fill((255,255,255))
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_RIGHT:
							jg.var_x = 5
						if event.key == pygame.K_LEFT:
							jg.var_x = -5
						if event.key == pygame.K_ESCAPE:
							validacion = False
							val = False
						if event.key == pygame.K_SPACE:
							B = Bala(5, 10, jg.rect.x)
							general.add(B)
							Balas.add(B)
					if event.type == pygame.KEYUP:
						if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
							jg.var_x = 0
					if event.type == pygame.QUIT:
						validacion = False
						val = False
				general.update()
				col1 = pygame.sprite.spritecollide(bar, rivales, True)
				col2 = pygame.sprite.spritecollide(jg, rivales, True)
				col3 = pygame.sprite.groupcollide(Balas, rivales, True, True)
				col4 = pygame.sprite.spritecollide(bar1, Balas, True)
				for i in col1: puntaje += 1
				for i in col3: puntaje += 1
				for i in col2: vida -= 1
				if vida == 0:
					niveles = 2
					val = False

		if niveles == 2:
			gameover = InterfasGameOver(pantalla)
			val = True
			while val:
				reloj.tick(60)
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if (event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN):
							niveles = 0
							val = False
						if event.key == pygame.K_ESCAPE:
							validacion = False
							val = False
					if event.type == pygame.QUIT:
						validacion = False
						val = False
