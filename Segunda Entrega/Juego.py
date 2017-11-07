import pygame
import configparser

ALTO=500
ANCHO=700
class Interfaz():
	def __init__(self, pantalla,  nivel, interprete):
		for i in interprete.items(nivel):
			print(i)
			if i[0] == 'imagen':
				self.imagen = pygame.image.load(i[1]).convert_alpha()
			else:
				corte = self.imagen.subsurface(eval(interprete.get('cortes',i[0])))
				for pos in eval(i[1]):
					pantalla.blit(corte,pos)		
		pygame.display.flip()


if __name__=='__main__':
	pygame.init()
	pantalla=pygame.display.set_mode([ANCHO,ALTO])
	interprete=configparser.ConfigParser()
	interprete.read('Mapa.map')
	pantalla.fill((0,160,0))
	V = Interfaz(pantalla, 'nivel2', interprete)
	reloj=pygame.time.Clock()
	val = True
	while val:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				val=False
		pygame.display.flip()
		reloj.tick(5)