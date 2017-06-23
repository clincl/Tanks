####MAKE SURE TO CHANGE FOLDERNAME
import pygame
import os

GROUND = 5
BLACK = (0,0,0)
WHITE = (255, 255, 255)

def loadImage(image):
    filename = os.path.join("foldername", image)
    image = pygame.image.load(filename).convert()
    return image, image.get_rect()
    
#def Terrain():

#def 
