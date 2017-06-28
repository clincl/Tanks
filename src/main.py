import pygame as pg
import utility as u
import tank
import barrier


class Controller():
	def __init__(self, width=1200, height=675):

		pg.init()
		self.width = width
		self.height = height
		self.screen = pg.display.set_mode((self.width, self.height))
		pg.display.set_caption("Tanks")
		pg.display.update() 
		self.background = u.loadImage("myBackground.png")[0]#pg.Surface(self.screen.get_size()).convert()
		self.screen.blit(self.background, (0, 0))
		self.wall = barrier.Barrier(600,375)		
		self.screen.blit(self.wall,(self.wall.x,self.wall.y))
		self.tank1 = tank.Tank(10, u.GROUND, "myTank.png", "myShootyThing.png")
		self.screen.blit(self.tank1.tankImage, (0, 0))
		self.screen.blit(self.tank1.shootyThingImage, (0, 0))
		self.tank2 = tank.Tank(-10, u.GROUND, "myTank2.png", "myShootyThing2.png")
		self.screen.blit(self.tank2.tankImage, (0, 0))
		self.screen.blit(self.tank2.shootyThingImage, (0, 0))
		self.spritegroup = pg.sprite.Sprite()
		self.smallfont = pg.font.SysFont("comicsansms",25)
		self.medfont = pg.font.SysFont("comicsansms",50)
		self.largefont = pg.font.SysFont("comicsansms",80)
		self.icon = pg.image.load('myTank.png')
		pg.sprite.RenderPlain()
		pg.display.flip()
		pg.display.set_icon(self.icon)#best size is 32*32
		self.clock = pg.time.Clock()

	def text_objects(self,text,color,size):
		if size == "small":
			textSurface = self.smallfont.render(text,True,color)
		elif size == "medium":
			textSurface = self.medfont.render(text,True,color)
		elif size == "large":
			textSurface = self.largefont.render(text,True,color)
		return textSurface, textSurface.get_rect()

	def message_to_screen(self,msg, color,y_displace = 0, size="small"):
		textSurf,textRect = text_objects(msg,color)
		textRect.center = (self.width/2,self.height/2) + y_displace
		self.screen.blit(textSurf,textRect)
	def game_intro(): #make sure you call it before the game loop 
		intro = True
		while intro:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					quit()
				if event.type == pg.KEYDOWN
					if event.key == pg.K_c:
						intro = False
					if event.key == pg.K_q:
						pg.QUIT
						quit()
			self.screen.fill(white)
			message_to_screen("Welcome to Tanks",purple,-100,size="large")
			message_to_screen("The Object of the game is to:",black,-30,size="small")
			message_to_screen("More Stuff Here",black,-40,size="small")
			message_to_screen("More Stuff Here",black,-40,size="small")
		pg.display.update()
		#clock.tick(15)

	def gameLoop(self):

		while not gameExit:
			while gameOver == True:
				self.screen.fill(white)  #ExitScreen
				message_to_screen("Game Over press C to play again or Q to Quit", red,y_displace=-50,size = "large")
				pg.display.update()

				for event in pg.event.get():
					if event.type == pg.KEYDOWN:
						if event.key == pg.K_q:
							gameExit = True
							gameOver = False
						if event.key == pg.K_c:
							gameLoop()

		pg.key.set_repeat(1,50)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				gameExit = True
			if event.type == pg.KEYDOWN:
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
					self.spritegroup.add(shot)
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
					self.spritegroup.add(shot)				
		collisionCheck(self.tank1, self.spritegroup)
		collisionCheck(self.tank2, self.spritegroup)
		collisionCheck(u.GROUND, self.spritegroup)
		collisionCheck(self.wall, self.spritegroup)
		pg.display.flip()
		gameOver = True


def main():

	Controller()
	

main()
