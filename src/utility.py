####MAKE SURE TO CHANGE FOLDERNAME
import pygame
import os

GROUND = 5
BLACK = (0,0,0)
WHITE = (255, 255, 255)
PURPLE = (216, 191, 216)
YELLOW = (255, 255, 51)

def loadImage(image):
    filename = os.path.join("images", image)
    image = pygame.image.load(filename).convert()
    return image, image.get_rect()
    
#def Terrain():

#def 
