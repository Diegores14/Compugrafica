import pygame
import ConfigParser

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

class Jugador():
	def __init__(self):
		self.imagen = pygame.image.load('pokemon2.png').convert_alpha()
		self.jugador = imagen.subsurface((1555,1744, 106, 82))



if __name__=='__main__':
	pygame.init()
	pantalla=pygame.display.set_mode([ANCHO,ALTO])
	interprete=ConfigParser.ConfigParser()
	interprete.read('Mapa.map')
	pantalla.fill((0,160,0))
	j = Jugador()
	V = Interfaz(pantalla, 'nivel1', interprete)
	#pantalla.blit(jugador.subsurface((90, 30, 16, 22)), (0,0))
	reloj=pygame.time.Clock()
	val = True
	while val:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				val=False
		pygame.display.flip()
		reloj.tick(60)
