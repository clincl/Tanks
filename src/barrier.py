import pygame
import tank

class Barrier(pg.sprite.Sprite):
	def __init__(self,x ,y,width =100,height=300 ):
		pygame.sprite.Sprite.__init__(self)
		self.barrier = pg.draw.rect(gameDisplay, black, [x,y,width,height])
		self.barrierRect.x = x - width/2
        	self.barrierRect.y = y
		
main()
