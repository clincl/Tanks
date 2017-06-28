import pygame as pg
import tank
import main

class Barrier(pg.sprite.Sprite):
	def __init__(self,x ,y,width =100,height=300 ):
		pg.sprite.Sprite.__init__(self)
		self.barrier = pg.draw.rect(self.screen, black, [x,y,width,height])
		self.barrierRect.x = x - width/2
        	self.barrierRect.y = y
		
