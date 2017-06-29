import pygame as pg
import utility as u

class Bullet(pg.sprite.Sprite):
    
	def __init__(self, x, y, direction, bulletImg):
		pg.sprite.Sprite.__init__(self)
		self.bulletImage, self.rect = u.loadImage(bulletImg)
		self.vel = 50
		self.grav = 10
		self.rect.x = x + 75
		self.rect.y = y
		self.bulletXSpeed = 1 * direction
		self.bulletYSpeed = 1
		self.direct = 1
		self.YIncr = 1


	def update(self):
		if True:
			self.vel += self.grav
			self.rect.x += self.bulletXSpeed
			self.rect.y -= self.bulletYSpeed * self.direct * self.YIncr
			self.YIncr -= 0.005
			if self.rect.y <= 0:
				direction = self.direct * -1
				self.direct = direction
				self.YIncr *= -1
		return (self.bulletImage, self.rect.x, self.rect.y)
