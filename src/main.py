import pygame as pg
import utility as u
import tank
import sys


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
		self.wall = u.loadImage("myWall.jpg")
		self.screen.blit(self.wall[0],(600,375))
		self.tank1 = tank.Tank(10, u.GROUND, "myTank.png", "myShootyThing45.png",1)
		self.screen.blit(self.tank1.image, (100, 577))
		self.screen.blit(self.tank1.shootyThingImage, (0, 0))
		self.tank2 = tank.Tank(-10, u.GROUND, "myTank2.png", "myShootyThing2_45.png",2)
		self.screen.blit(self.tank2.image, (1100, 577))
		self.screen.blit(self.tank2.shootyThingImage, (0, 0))
		self.spritegroup = pg.sprite.Group()
		self.smallfont = pg.font.SysFont("comicsansms",25)
		self.medfont = pg.font.SysFont("comicsansms",50)
		self.largefont = pg.font.SysFont("comicsansms",80)
		self.music = u.loadMusic("IntroMusic.mp3")		
		#self.icon = pg.image.load('myTank.png')
		pg.sprite.RenderPlain()
		pg.display.flip()
		#pg.display.set_icon(self.icon)#best size is 32*32
		self.clock = pg.time.Clock()
		self.buttong = pg.draw.rect(self.screen,u.GREEN,(100,500,100,50))
		self.buttony = pg.draw.rect(self.screen,u.YELLOOW,(300,500,100,50))
		self.buttonr = pg.draw.rect(self.screen,u.RED,(500,500,100,50))
		

	def text_objects(self,text,color,size):
		if size == "small":
			self.textSurface = self.smallfont.render(text,True,color)
		elif size == "medium":
			self.textSurface = self.medfont.render(text,True,color)
		elif size == "large":
			self.textSurface = self.largefont.render(text,True,color)
		return self.textSurface, self.textSurface.get_rect()

	def message_to_screen(self,msg, color,y_displace = 0, size="small"):
		self.textSurf,self.textRect = self.text_objects(msg,color,size)
		self.textRect.center = (self.width/2 + y_displace,self.height/2 + y_displace)
		self.screen.blit(self.textSurf,self.textRect)
		return self.textSurf
	
	def game_intro(self):
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_c:
					self.gameState = "Running"
				if event.key == pg.K_q:
					sys.exit()
		self.screen.fill(u.WHITE)
		self.message_to_screen("Welcome to Tanks",u.PURPLE,100,size="large")
		self.message_to_screen("The Object of the game is to:",u.BLACK,-30,size="small")
		self.message_to_screen("More Stuff Here",u.BLACK,45,size="small")
		#self.message_to_screen("More Stuff Here",u.BLACK,30,size="small")
		#self.screen.blit(self.buttonp,"MESSAGE HERE?!???")
	def text_to_button (self,msg,color,buttonx,buttony,buttonwidth,buttonheight,size= "small")
		self.textSurf,self.textRect = self.text_objects(msg,color,size)
		self.textRect.center = (butttonx + (buttonwidth/2)),(buttony+(buttonheight/2))
		self.screen.blit(self.textSurf,self.textRect)
		return self.textSurf
	
		
		
		
		
	def gameLoop(self):
		self.gameState = "Start"
		self.angle1 = 45
		self.angle2 = 45
		pg.key.set_repeat(1,10)
		while True:
			if self.gameState == "Start":
				self.game_intro()
				print("Start")

			elif self.gameState == "Running":
				#self.music = u.loadMusic("BattleMusic.mp3")
				self.posTup1 = []
				self.posTup2 = []
				for event in pg.event.get():
					if event.type == pg.KEYDOWN:
						if event.key == pg.K_ESCAPE:
							self.gameState = "Over"
						if event.key == pg.K_UP:
							ang = self.tank2.angle(event.key,self.angle2)
							self.angle2 = ang
						elif event.key == pg.K_DOWN:
							ang = self.tank2.angle(event.key, self.angle2)
							self.angle2 = ang
						if event.key == pg.K_LEFT:
							self.posTup2 = self.tank2.move(event.key)
						elif event.key == pg.K_RIGHT:
							self.posTup2 = self.tank2.move(event.key)
						if event.key == pg.K_RSHIFT:
							self.shot = self.tank2.shoot(event.key)
							self.spritegroup.add(self.shot)
						if event.key == pg.K_w:
							ang = self.tank1.angle(event.key, self.angle1)
							self.angle1 = ang
						elif event.key == pg.K_s:
							ang = self.tank1.angle(event.key,self.angle1)
							self.angle1 = ang
						if event.key == pg.K_a:
							self.posTup1 = self.tank1.move(event.key)
						elif event.key == pg.K_d:
							self.posTup1 = self.tank1.move(event.key)
						if event.key == pg.K_SPACE:
							self.shot = self.tank1.shoot(event.key)
							self.spritegroup.add(self.shot)				
				if len(self.posTup1) != 0:
					self.tank1.rect.x = self.posTup1[0]
					self.tank1.rect.y = self.posTup1[1]
					self.tank1.shootyThingRect.x = self.posTup1[2]
					self.tank1.shootyThingRect.y = self.posTup1[3]
				if len(self.posTup2) != 0:
					self.tank2.rect.x = self.posTup2[0]
					self.tank2.rect.y = self.posTup2[1]
					self.tank2.shootyThingRect.x = self.posTup2[2]
					self.tank2.shootyThingRect.y = self.posTup2[3]	
				self.spritegroup.update()
				self.tank1.health = u.collisionCheck(self.tank1, self.spritegroup)
				self.tank2.health = u.collisionCheck(self.tank2, self.spritegroup)
		
				for i in self.spritegroup.sprites():
					if self.wall[0].get_rect().colliderect(i.rect):
						self.spritegroup.remove(i)
				u.groundCheck(self.spritegroup)
				print(self.tank1.rect.x, self.tank2.rect.x)
				if self.tank1.health == 0 or self.tank2.health == 0:
					self.gameState = "Over"
				self.screen.blit(self.background, (0, 0))
				self.screen.blit(self.tank1.image, (self.tank1.rect.x,self.tank1.rect.y))
				self.screen.blit(self.tank1.shootyThingImage, (self.tank1.shootyThingRect.x, self.tank2.shootyThingRect.y))
				self.screen.blit(self.wall[0],(600,375))
				self.screen.blit(self.tank2.image, (self.tank2.rect.x,self.tank2.rect.y ))
				self.screen.blit(self.tank2.shootyThingImage, (self.tank2.shootyThingRect.x, self.tank2.shootyThingRect.y))				
				if len(self.spritegroup) >= 1:
					for i in self.spritegroup:
						self.screen.blit(i.bulletImage, (self.shot.rect.x,self.shot.rect.y))
			elif self.gameState == "Over":
				self.music = u.loadMusic("GameOver.mp3")
				self.screen.fill(u.WHITE)  #ExitScreen
				self.message_to_screen("Game Over press C to play again or Q to Quit", u.RED,y_displace=-50,size = "medium")
				if self.tank1.health == 0:
					self.message_to_screen("Player Two Wins",u.GREEN, y_displace = -45,size = "medium")	
				elif self.tank1.health == 0: 	
					self.message_to_screen("Player One Wins",u.GREEN,y_displace = -45,size = "medium")				
				pg.display.update()
	
				for event in pg.event.get():
					if event.type == pg.KEYDOWN:
						if event.key == pg.K_q:
							sys.exit()
							
						if event.key == pg.K_c:
							self.gameState = "Running"
				print("Over")
			pg.display.update()
		pg.display.quit()		
		pg.quit()
		sys.exit()
		

def main():

	main_window = Controller()
	main_window.gameLoop()

main()
