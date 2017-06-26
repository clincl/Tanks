####MAKE SURE TO CHANGE FOLDERNAME
import pygame as pg
import os

TITLE = 'Tanks'
GROUND = 250
BLACK = (0,0,0)
WHITE = (255, 255, 255)
PURPLE = (216, 191, 216)
YELLOW = (255, 255, 51)
INVALID_INPUTS = [pg.K_4, pg.K_h, pg.K_i, pg.K_SEMICOLON, pg.K_MINUS, pg.K_LEFTBRACKET, pg.K_QUESTION, pg.K_HASH, pg.K_v, pg.K_KP4]

def loadImage(image):
    filename = os.path.join("images", image)
    image = pg.image.load(filename).convert()
    return image, image.get_rect()
    
#def Terrain():

def testMove(functionality, Window, Tank):
	functionality
	Window.screen.blit(Tank.tankImage, (Tank.tankRect.x,Tank.tankRect.y))
	Window.screen.blit(Tank.shootyThingImage, (Tank.shootyThingRect.x,Tank.shootyThingRect.y))		
	pg.display.update()

def testAngle(functionality, init_angle, Window, Tank):	
	angle = init_angle	
	angle = functionality
	Window.screen.blit(Tank.tankImage, (Tank.tankRect.x,Tank.tankRect.y))
	Window.screen.blit(Tank.shootyThingImage, (Tank.shootyThingRect.x,Tank.shootyThingRect.y))
	pg.display.update()
	return angle
