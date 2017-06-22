import pygame
import tank

white = (255,255,255)

class Controller:
    def __init__(self, width=640, height=480):
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
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.tank = tank.Tank(100, 100, "mytank.kpreg")
        #self.sprites = pygame.sprite.RenderPlain((self.hero)+(self.enemy))

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
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.tank.move(event.key)
        #        elif(pygame.sprite.collide_rect(self.hero, self.enemies[i])):
        #needs shoot/tank destruction/collission/enemies
        self.screen.blit(self.background, (0, 0))
        self.tank.draw(self.screen)
        #self.sprites.draw(self.screen)

def main():
    Controller()
    Controller.mainLoop()

main()
