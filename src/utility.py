####MAKE SURE TO CHANGE FOLDERNAME
import pygame
import os

TITLE = 'Tanks'
GROUND = 250
BLACK = (0,0,0)
WHITE = (255, 255, 255)
PURPLE = (216, 191, 216)
YELLOW = (255, 255, 51)
INVALID_INPUTS = [pygame.K_4, pygame.K_h, pygame.K_i, pygame.K_SEMICOLON, pygame.K_MINUS, pygame.K_LEFTBRACKET, pygame.K_QUESTION, pygame.K_HASH, pygame.K_v, pygame.K_KP4]

def loadImage(image):
    filename = os.path.join("images", image)
    image = pygame.image.load(filename).convert()
    return image, image.get_rect()
    
#def Terrain():

def testMove(functionality, Window, Tank):
	functionality
	Window.screen.blit(Tank.tankImage, (Tank.tankRect.x,Tank.tankRect.y))
	Window.screen.blit(Tank.shootyThingImage, (Tank.shootyThingRect.x,Tank.shootyThingRect.y))		
	pygame.display.update()

def testAngle(functionality, init_angle, Window, Tank):	
	angle = init_angle	
	angle = functionality
	Window.screen.blit(Tank.tankImage, (Tank.tankRect.x,Tank.tankRect.y))
	Window.screen.blit(Tank.shootyThingImage, (Tank.shootyThingRect.x,Tank.shootyThingRect.y))
	pygame.display.update()
	return angle
