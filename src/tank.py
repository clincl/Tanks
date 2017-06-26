import pygame as pg
import utility as u
import bullet

class Tank(pg.sprite.Sprite):
    def __init__(self, x, y, tankImg, shootyThingImg):
        """
        Creates the tank.
        args:
            param list: (self) States the variable.
                        (x) The x coordinate.
                        (y) The y coordinate.
                        (img_file) The sprite.

        return:
                        (self) Returns the variable.
                        (x) Places the tank at x.
                        (y) Places the tank at y.
                        (img_file) Gives the tank its sprite.
        """
        self.tankImage, self.tankRect = u.loadImage(tankImg)
        self.shootyThingImage, self.shootyThingRect = u.loadImage(shootyThingImg)
        self.tankRect.x = 10
        self.tankRect.y = u.GROUND
        self.shootyThingRect.x = self.tankRect.x + 175
        self.shootyThingRect.y = u.GROUND + 60
        pg.sprite.Sprite.__init__(self)
        self.tankSpeed = 10.0
        self.health = 50

    def move(self, direction):
        """
        Moves the tank when direction is hit.
        args:
            param list: (self) States the variable.
                        (direction) The direction you want the tank to go.
        return:
                        (self) Returns the variable.
                        (direction) Returns the tank going in that direction
        """
        if(direction == pg.K_LEFT or direction == pg.K_a):
            self.tankRect.x -= self.tankSpeed
            self.shootyThingRect.x -= self.tankSpeed
        elif(direction == pg.K_RIGHT or direction == pg.K_d):
            self.tankRect.x += self.tankSpeed
            self.shootyThingRect.x += self.tankSpeed
        return self.tankRect.x, self.tankRect.y
    
    def angle(self, direction, the_angle):
        """
        Moves the shootyThing when direction is hit.
        args:
            param list: (self) States the variable.
                        (direction) The direction you want the tank to go.
        return:
                        (self) Returns the variable.
                        (direction) Returns the tank going in that direction
        """        
        if direction == pg.K_UP or direction == pg.K_w:
            old = self.shootyThingRect.copy()
            self.shootyThingImage = pg.transform.rotozoom(self.shootyThingImage, 2, 1)
            self.shootyThingRect = self.shootyThingImage.get_rect()
            self.shootyThingRect.w = old.w
            self.shootyThingRect.h = old.h
            self.shootyThingRect.center = old.center
            print(self.shootyThingRect.width, self.shootyThingRect.height)
            #self.shootyThingRect.x -= 1
            #self.shootyThingRect.y -= 1
            the_angle += 2
            return the_angle
        elif direction == pg.K_DOWN or direction == pg.K_s:
            self.shootyThingImage = pg.transform.rotate(self.shootyThingImage, -1)
            self.shootyThingRect = self.shootyThingImage.get_rect()
            self.shootyThingRect.center = origin
            #self.shootyThingRect.x += 1
            #self.shootyThingRect.y += 1
            the_angle -= 1
            return the_angle
        return the_angle

    def shoot(self, key):
        """
            Produces a projectile and fires it. WIP.
        args:
            param list: (self) States the variable.
        return:
                        (self) Returns the variable.
        """
        if key == pg.K_SPACE:
            direction = 1
            shot = bullet.Bullet(self.shootyThingRect.x, self.shootyThingRect.y, direction, "MyBullet.png")
	    elif key == pg.K_RSHIFT:
            direction = -1
            shot = bullet.Bullet(self.shootyThingRect.x, self.shootyThingRect.y, direction, "MyBullet2.png")
        return shot
