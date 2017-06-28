import pygame as pg
import utility as u

class Bullet(pg.sprite.Sprite):
    
    def __init__(self, x, y, direction, bulletImg):
        pg.sprite.Sprite.__init__(self)
        self.bulletImage, self.rect = u.loadImage(bulletImg)
        self.rect.x = x + 75
        self.rect.y = y
        self.bulletXSpeed = 5 * direction
        self.bulletYSpeed = -5
        self.bulletMaxY = 0
        
    def update(self):
        self.rect.x += self.bulletXSpeed
        self.rect.y += self.bulletYSpeed
        if self.rect.y == self.bulletMaxY:
            self.bulletYSpeed *= -1
        return (self.bulletImage, self.rect.x, self.rect.y)
