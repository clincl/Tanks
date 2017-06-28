import pygame as pg
import math as *
import utility as u

class Bullet(pg.sprite.Sprite):

	def __init__(self, x, y, direction, angle, bulletImg):
		pg.sprite.Sprite.__init__(self)
		self.bulletImage, self.bulletRect = u.loadImage(bulletImg)
		self.bulletRect.x = x + 75
		self.bulletRect.y = y
		self.bulletXSpeed = 5 * direction
		self.bulletYSpeed = 5
		self.bulletMaxY = 150
		self.angle = angle
        
	def update(self):
		self.bulletRect.x += self.bulletXSpeed * cos(self.angle)
		self.bulletRect.y += (self.bulletYSpeed * sin(self.angle)) - u.GRAVITY
		if self.bulletY == self.bulletMaxY:
			self.bulletYSpeed *= -1
		return self.bulletRect.x, self.bulletRect.y
