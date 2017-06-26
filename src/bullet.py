import pygame as pg
import utility as u

class Bullet(pg.sprite.Sprite):
    
    def __init__(self, x, y, direction, bulletImg):
        pg.sprite.Sprite.__init__(self)
        self.bulletImage, self.bulletRect = u.loadImage(bulletImg)
        self.bulletRect.x = x + 75
        self.bulletRect.y = y
        self.bulletXSpeed = 5 * direction
        self.bulletYSpeed = 5
        self.bulletMaxY = 150
        
    def update(self):
        self.bulletRect.x += self.bulletXSpeed
        self.bulletRect.y += self.bulletYSpeed
        if self.bulletY == self.bulletMaxY:
            self.bulletYSpeed *= -1
        return self.bulletRect.x, self.bulletRect.y
