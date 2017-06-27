import pygame as pg
import utility as u
import tank


class Controller:
    def __init__(self, width=800, height=450):

        pg.init()
		self.width = width
		self.height = height
		self.screen = pg.display.set_mode((self.width, self.height))
		self.screen = pg.set_caption(u.TITLE)  # Nia
		self.screen = pg.display.update()  # Nia
		self.background = pg.Surface(self.screen.get_size()).convert()
		self.screen.blit(u.loadImage("myBackground.png")[0], (0, 0))
		self.tank1 = tank.Tank(100, u.GROUND, "myTank.png", "myShootyThing.png")
		self.screen.blit(self.tank1.tankImage, (0, 0))
		self.screen.blit(self.tank1.shootyThingImage, (0, 0))
		self.tank2 = tank.Tank(-100, u.GROUND, "myTank2.png", "myShootyThing2.png")
		self.screen.blit(self.tank2.tankImage, (0, 0))
		self.screen.blit(self.tank2.shootyThingImage, (0, 0))
        self.font = pg.font.Sysfont(None,25)
		pygame.sprite.RenderPlain()

	def text_objects(self,text,color):
	    textSurface = self.font.render(text,True,color)
            return textSurface, textSurface.get_rect()

	def message_to_screen(self,msg, color,y_displace = 0, size="small"):
		textSurf,textRect = text_objects(msg,red)
        textRect.center = (self.width/2,self.height/2) + y_displace
		self.screen.blit(textSurf,textRect)


	def gameLoop(self):
		"""
		Sets the background white and allows you to hold directional keys to move.

		args:
			param list: (self) States the variable.
						(direction) The direction you want the tank to go.
		return:
						(self) Returns the variable.
						(direction) Returns the tank going in that direction
		"""

		while not gameExit:
			while gameOver == True:
				self.screen.fill(white)
				message_to_screen("Game Over press C to play again or Q to Quit", red,-50)
				pygame.display.update()

				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_q:
							gameExit = True
							gameOver = False
						if event.key == pygame.K_c:
							gameLoop()

						# pg.key.set_repeat(1,50)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				# Print(event) #Nia lets you see where your mouse is
				GameExit = True
			if event.type == pygame.KEYDOWN
				if event == pg.K_UP:
					self.tank1.angle(event)
				elif event == pg.K_DOWN:
					self.tank1.angle(event)
				if event == pg.K_LEFT:
					self.tank1.move(event)
				elif event == pg.K_RIGHT:
					self.tank1.move(event)
				if event == pg.K_RSHIFT:
					shot = self.tank1.shoot(event)
				if event == pg.K_w:
					self.tank2.angle(event)
				elif event == pg.K_s:
					self.tank2.angle(event)
				if event == pg.K_a:
					self.tank2.move(event)
				elif event == pg.K_d:
					self.tank2.move(event)
				if event == pg.K_SPACE:
					shot = self.tank2.shoot(event)
				# check for all collisions
				# respond appropriately
		self.tank.draw(self.screen)
        gameOver = True


def main():
    Controller()
    Controller.gameLoop()


main()
