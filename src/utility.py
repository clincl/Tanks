####MAKE SURE TO CHANGE FOLDERNAME
import pygame as pg
import os
import time
import math

TITLE = 'Tanks'
GROUND = 250
BLACK = (0,0,0)
WHITE = (255, 255, 255)
PURPLE = (216, 191, 216)
YELLOW = (255, 255, 51)
INVALID_INPUTS = [pg.K_4, pg.K_h, pg.K_i, pg.K_SEMICOLON, pg.K_MINUS, pg.K_LEFTBRACKET, pg.K_QUESTION, pg.K_HASH, pg.K_v, pg.K_KP4]
TANK_INPUTS = [pg.K_UP, pg.K_DOWN, pg.K_w, pg.K_s, pg.K_SPACE, pg.K_RHSIFT]
SHOOTYTHING_INPUTS = [pg.K_LEFT, pg.K_RIGHT, pg.K_a, pg.K_d, pg.K_SPACE, pg.K_RHSIFT]
BULLET_INPUTS = [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_w, pg.K_s, pg.K_a, pg.K_d]

def loadImage(image):
	filename = os.path.join("images", image)
	image = pg.image.load(filename).convert()
	return image, image.get_rect()

def testMove(iters, direction, Window, Tank):
	for i in range(iters):
		pos = Tank.move(direction)
		Window.screen.blit(Tank.tankImage, (Tank.tankRect.x,Tank.tankRect.y))
		Window.screen.blit(Tank.shootyThingImage, (Tank.shootyThingRect.x,Tank.shootyThingRect.y))		
		pg.display.update()
		print("The new position of the tank is ", pos)
	return pos 

def testAngle(iters, direction, init_angle, Window, Tank):
	for i in range(iters):		
		angle = Tank.angle(direction, init_angle)
		init_angle = angle
		#Window.screen.blit(Tank.tankImage, (Tank.tankRect.x,Tank.tankRect.y))
		Window.screen.blit(Tank.shootyThingImage, (Tank.shootyThingRect.x,Tank.shootyThingRect.y))
		pg.display.update()
		time.sleep(1)
		print("The angle of the shootyThing is ", init_angle)
	return init_angle

def collisionCheck(MainObject, SpriteGroup):
	col = pygame.sprite.collide(MainObject, SpriteGroup)
	if col == True:
		pygame.sprite.SpriteGroup.remove()
