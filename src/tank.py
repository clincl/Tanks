import pygame as pg
import utility as u
import bullet

class Tank(pg.sprite.Sprite):
	def __init__(self, x, y, tankImg, shootyThingImg):
		self.tankImage, self.tankRect = u.loadImage(tankImg)
		self.shootyThingImage, self.shootyThingRect = u.loadImage(shootyThingImg)
		self.tankRect.x = 10
		self.tankRect.y = u.GROUND
		self.shootyThingRect.x = self.tankRect.x + 175
		self.shootyThingRect.y = u.GROUND + 60
		pg.sprite.Sprite.__init__(self)
		self.tankSpeed = 10.0
		self.health = 50

	def move(self, direction):
		if(direction == pg.K_LEFT or direction == pg.K_a):
			self.tankRect.x -= self.tankSpeed
			self.shootyThingRect.x -= self.tankSpeed
		elif(direction == pg.K_RIGHT or direction == pg.K_d):
			self.tankRect.x += self.tankSpeed
			self.shootyThingRect.x += self.tankSpeed
		return self.tankRect.x, self.tankRect.y
	    
	def angle(self, direction, the_angle):      
		if direction == pg.K_UP:
			the_angle += 1
			for i in utility.ANGLE_DICTIONARY_2.keys():
				diff = the_angle - i
				if i == the_angle or (diff <= 4 and diff > 0):
					self.shootyThingImage = utility.loadImage(utility.ANGLE_DICTIONARY_2.get(i))
			return the_angle
		if direction == pg.K_w:
			the_angle += 1
			for i in utility.ANGLE_DICTIONARY.keys():
				diff = the_angle - i
				if i == the_angle or (diff <= 4 and diff > 0):
					self.shootyThingImage = utility.loadImage(utility.ANGLE_DICTIONARY.get(i))
			return the_angle
		if direction == pg.K_DOWN:
			the_angle += 1
			for i in utility.ANGLE_DICTIONARY_2.keys():
				diff = the_angle - i
				if i == the_angle or (diff <= 4 and diff > 0):
					self.shootyThingImage = utility.loadImage(utility.ANGLE_DICTIONARY_2.get(i))
			return the_angle
		if direction == pg.K_s:
			the_angle += 1
			for i in utility.ANGLE_DICTIONARY.keys():
				diff = the_angle - i
				if i == the_angle or (diff <= 4 and diff > 0):
					self.shootyThingImage = utility.loadImage(utility.ANGLE_DICTIONARY.get(i))
			return the_angle
		return the_angle

	def shoot(self, key):
		if key == pg.K_SPACE:
			direction = 1
			shot = bullet.Bullet(self.shootyThingRect.x, self.shootyThingRect.y, direction, "MyBullet.png")
		if key == pg.K_RSHIFT: #elif doesn't work what?
			direction = -1
			shot = bullet.Bullet(self.shootyThingRect.x, self.shootyThingRect.y, direction, "MyBullet2.png")
		return shot
