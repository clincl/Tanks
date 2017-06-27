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
TANK_INPUTS = [pg.K_UP, pg.K_DOWN, pg.K_w, pg.K_s, pg.K_SPACE, pg.K_RSHIFT]
SHOOTYTHING_INPUTS = [pg.K_LEFT, pg.K_RIGHT, pg.K_a, pg.K_d, pg.K_SPACE, pg.K_RSHIFT]
BULLET_INPUTS = [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_w, pg.K_s, pg.K_a, pg.K_d]
ANGLE_DICTIONARY = {75:"myShootyThing75.png", 70:"myShootyThing70.png", 65:"myShootyThing65.png", 60:"myShootyThing60.png", 55:"myShootyThing55.png", 50:"myShootyThing50.png", 45:"myShootyThing45.png", 40:"myShootyThing50.png"}
ANGLE_DICTIONARY_2 = {75:"myShootyThing2_75.png", 70:"myShootyThing2_70.png", 65:"myShootyThing2_65.png", 60:"myShootyThing2_60.png", 55:"myShootyThing2_55.png", 50:"myShootyThing2_50.png", 45:"myShootyThing2_45.png", 40:"myShootyThing2_40.png"}

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

def collisionCheck(MainObject, Group):
	col = pygame.sprite.collide(MainObject, Group)
	for i in col:
		Group.remove(i)
		
def transformShootyThing(Surface, Copy, XDir, YDir, Angle_Dir):
	Surface = pg.transform.rotozoom(Surface, 2 * Angle_Dir, 1)
	SurfaceRect = Surface.get_rect()
	print(SurfaceRect.w, SurfaceRect.h)
	#SurfaceRect.w = Copy.w
	#SurfaceRect.h = Copy.h
	Surface.set_clip(Copy)	
	SurfaceRect.center = Copy.center
	print(SurfaceRect.width, SurfaceRect.height)
	SurfaceRect.x += 1 * XDir
	SurfaceRect.y += 1 * YDir
	return Surface
