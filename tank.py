import pygame
black = (0,0,0)
white = (255,255,255)
class Tank:
    def __init__(self, x, y, img_file):
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
        self.rect.x = 100
        self.rect.y = 100
        pygame.sprite.Sprite.__init__(self)
        self.tankSpeed = 10.0

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
            self.rect.x -= self.speed
        elif(direction == pygame.K_RIGHT):
            self.rect.x += self.speed

    def shoot(self):
        """
            Produces a projectile and fires it. WIP.
        args:
            param list: (self) States the variable.
        return:
                        (self) Returns the variable.
        """
