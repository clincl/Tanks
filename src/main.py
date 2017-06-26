import pygame as pg
import utility as u
import tank

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
        
        pg.init()
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((self.width, self.height))
        self.screen = pg.set_caption(u.TITLE)#Nia
        self.screen = pg.display.update() #Nia
        self.background = pg.Surface(self.screen.get_size()).convert()
        self.screen.blit(u.loadImage("myBackground.png")[0], (0,0))
        self.tank1 = tank.Tank(100, u.GROUND, "myTank.png","myShootyThing.png")
        self.screen.blit(self.tank1.tankImage, (0,0))
        self.screen.blit(self.tank1.shootyThingImage, (0,0))
        self.tank2 = tank.Tank(-100,u.GROUND,"myTank2.png","myShootyThing2.png")
        self.screen.blit(self.tank2.tankImage,(0,0))
        self.screen.blit(self.tank2.shootyThingImage, (0,0))
        pygame.sprite.RenderPlain()
        
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
        pg.key.set_repeat(1,50)
        while True:
            self.background.fill(white)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    #Print(event) #Nia lets you see where your mouse is
                    sys.exit()
                if event == pg.K_UP:
                    self.tank1.angle(event)
                elif event == pg.K_DOWN:
                    self.tank1.angle(event)
                if event == pg.K_LEFT:
                    self.tank1.move(event)
                elif event == pg.K_RIGHT:
                    self.tank1.move(event)
                if event == pg.K_RSHIFT:
                    self.tank1.shoot(event)
                if event == pg.K_w:
                    self.tank2.angle(event)
                elif event == pg.K_s:
                    self.tank2.angle(event)
                if event == pg.K_a:
                    self.tank2.move(event)
                elif event == pg.K_d:
                    self.tank2.move(event)
                if event == pg.K_SPACE:
                    self.tank2.shoot(event)
        self.tank.draw(self.screen)
        self.
               
   

def main():
    Controller()
    Controller.mainLoop()

main()
