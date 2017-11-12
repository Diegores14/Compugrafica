import pygame

ALTO=500
ANCHO=700

if __name__=='__main__':
	pygame.init()
	pantalla=pygame.display.set_mode([ANCHO,ALTO])
	imagen=pygame.image.load('Goku1.png').convert_alpha()
	ancho_img,alto_img =imagen.get_size()
	print ("ancho: ",ancho_img,"alto: ",alto_img)
	pantalla.fill((255,0,0))
	cuadro=(24+28*13,6+36*3 + 16, 18, 18)
	recorte=pygame.transform.rotate(imagen.subsurface(cuadro),90)
	reloj=pygame.time.Clock()
	pantalla.blit(recorte,[0,0])
	fin=False
	while not fin:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				fin=True
			if event.type==pygame.KEYDOWN:
			  fin = True
			pygame.display.flip()
			reloj.tick(60)
