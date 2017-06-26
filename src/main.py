import pygame
import tank
import utilities

class Controller:
    def __init__(self, width=800, height=450):
    """
Initializes the screen and sets its dimensions.

    args:
        param list: (self) States the variable.
                    (width) The width.
                    (height) The height.
    return:
                    (self) Returns the variable.
                    (width)
                    (height)
    """
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen = pygame.set_caption(TITLE)#Nia
        self.screen = pygame.display.update() #Nia
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.screen.blit(utility.loadImage("myBackground.jpg")[0], (0,0))
        self.tank1 = tank.Tank(100, utility.GROUND, "myTank.jpg","myShootyThing.jpg")
        self.screen.blit(self.tank1.tankImage, (0,0))
        self.screen.blit(self.tank1.shootyThingImage, (0,0))
        self.tank2 = tank.Tank(-100,utility.GROUND,"myTank2.jpg","myShootyThing2.jpg")
        self.screen.blit(self.tank2.tankImage,(0,0))
        self.screen.blit(self.tank2.shootyThingImage, (0,0))
        
    def mainLoop(self):
    """
    Sets the background white and allows you to hold directional keys to move.

    args:
        param list: (self) States the variable.
                    (direction) The direction you want the tank to go.
    return:
                    (self) Returns the variable.
                    (direction) Returns the tank going in that direction
    """
        pygame.key.set_repeat(1,50)
        while True:
            self.background.fill(white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #Print(event) #Nia lets you see where your mouse is
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.tank.move(event.key)
       
        self.tank.draw(self.screen)
   

def main():
    Controller()
    Controller.mainLoop()

main()
