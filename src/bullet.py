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
		#self.bulletMaxY = 150
		self.angle = angle
        
	def update(self):
		self.bulletRect.x += self.bulletXSpeed * cos(self.angle)
		t = 0
		while self.bulletYSpeed > 0:
			t +=1
			self.bulletYSpeed += u.GRAVITY * t #as t increases speed drops
			self.bulletRect.y += ((self.bulletYSpeed * sin(self.angle)) * t) + ((u.GRAVITY/2) * t**2)
		if self.bulletYSpeed <= 0:
			while self.bulletRect.y > u.GROUND:
				t -= 1
				self.bulletYSpeed -= u.GRAVITY * t #as t increases speed increases
				self.bulletRect.y += ((self.bulletYSpeed * sin(self.angle)) * t) + ((u.GRAVITY/2) * t**2)

				
		#if self.bulletY == self.bulletMaxY:
		#	self.bulletYSpeed *= -1
		return self.bulletRect.x, self.bulletRect.y
