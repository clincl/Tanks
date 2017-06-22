import pygame
import utility
import bullet

class Tank:
    def __init__(self, x, y):
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
        self.tankImage, self.tankRect = utility.loadImage("myTank.jpeg")
        self.shootyThingImage, self.shootyThingRect = utility.loadImage("myShootyThing.jpeg")
        self.tankRect.x = 100
        self.tankRect.y = utility.GROUND
        self.shootyThingRect.x = 100
        self.shootyThingRect.y = utility.GROUND
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
            self.tankRect.x -= self.speed
        elif(direction == pygame.K_RIGHT):
            self.tankRect.x += self.speed
    
    def angle(self, direction, angle):
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
            self.shootyThingRect.transform.rotate(self.shootyThingImage, 1)
            self.shootyThingRect.x -= 1
            self.shootyThingRect.y -= 1
            angle += 1
        elif direction == pygame.K_DOWN:
            self.shootyThingRect.transform.rotate(self.shootyThingImage, -1)
            self.shootyThingRect.x -= 1
            self.shootyThingRect.y -= 1
            angle -= 1
        return angle

    def shoot(self, key):
        """
            Produces a projectile and fires it. WIP.
        args:
            param list: (self) States the variable.
        return:
                        (self) Returns the variable.
        """
        if key == pygame.K_SPACE:
            bulletShot = Bullet()
            return bulletShot
