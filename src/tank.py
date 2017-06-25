import pygame
import utility
import bullet

class Tank(pygame.sprite.Sprite):
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
        self.tankImage, self.tankRect = utility.loadImage(tankImg)
        self.shootyThingImage, self.shootyThingRect = utility.loadImage(shootyThingImg)
        self.tankRect.x = 10
        self.tankRect.y = utility.GROUND
        self.shootyThingRect.x = self.tankRect.x + 175
        self.shootyThingRect.y = utility.GROUND + 60
        pygame.sprite.Sprite.__init__(self)
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
        if(direction == pygame.K_LEFT):
            self.tankRect.x -= self.tankSpeed
            self.shootyThingRect.x -= self.tankSpeed
        elif(direction == pygame.K_RIGHT):
            self.tankRect.x += self.tankSpeed
            self.shootyThingRect.x += self.tankSpeed
    
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
        if direction == pygame.K_UP:
            pygame.transform.rotate(self.tankImage, 20.0)
            #self.shootyThingRect.x -= 1
            #self.shootyThingRect.y -= 1
            the_angle 
            return the_angle
        elif direction == pygame.K_DOWN:
            pygame.transform.rotate(self.shootyThingImage, -20.0)
            #self.shootyThingRect.x += 1
            #self.shootyThingRect.y += 1
            the_angle -= 20
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
        if key == pygame.K_SPACE:
            shot = bullet.Bullet(self.shootyThingRect.x, self.shootyThingRect.y)
            return shot
            
