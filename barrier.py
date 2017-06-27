import pygame
import tank

class Barrier(pg.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.barrier = pg.draw.rect(gameDisplay, black, [400,300,barrier_width,1000])
		self.barrierRect.x = x + 600 - #half of the wall
        	self.barrierRect.y = y + 600
		
main()
