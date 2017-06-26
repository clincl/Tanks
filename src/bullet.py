import pygame as pg
import utility as u

class Bullet(pg.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.bulletImage, self.bulletRect = u.loadImage("myBullet.png")
        self.bulletRect.x = x + 75
        self.bulletRect.y = y
        self.bulletXSpeed = 5
        self.bulletYSpeed = 5
        self.bulletMaxY = 150
        
    def update(self):
        self.bulletX += self.bulletXSpeed
        self.bulletY += self.bulletYSpeed
        if self.bulletY == self.bulletMaxY:
            self.bulletYSpeed *= -1
