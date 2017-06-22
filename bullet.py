import pygame
import utility

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, location, image):
        pygame.sprite.Sprite.__init__(self)
        self.bulletX, self.bulletY = location
        self.bulletImage, self.bulletRect = utility.loadImage("myBullet.jpeg")
        self.bulletXSpeed = 5
        self.bulletYSpeed = 5
        self.bulletMaxY = 150
        
    def update(self):
        self.bulletX += self.bulletXSpeed
        self.bulletY += self.bulletYSpeed
        if self.bulletY == self.bulletMaxY:
            self.bulletYSpeed *= -1
