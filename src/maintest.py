import pygame
import tank
import bullet
import utility

class Controller:
	def __init__(self, width=800, height=450):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption('Tanks')#Nia	
		self.background = pygame.Surface(self.screen.get_size()).convert()
		self.screen.blit(utility.loadImage("myBackground.jpg")[0], (0,0))
		pygame.display.flip()


def test():
	'''
	This function contains the test code for the classes
	Arguments: None
	Returns: None
	'''
	x = Controller()
	
	#This tests object (tank) creation
	tank1 = tank.Tank(10, 10, "myTank.jpg", "myShootyThing.jpg")
	x.screen.blit(tank1.tankImage, (0,0))
	pygame.display.update() #Nia
	#This tests the class to ensure that the stats are assigned properly

	#This tests proper movement in the positive x direction
	#print(tank1.tankRect())
	for i in range(250):	
		tank1.move(pygame.K_RIGHT)
		x.screen.blit(tank1.tankImage, (0,0))
		pygame.display.update()
	#print("The new x-pos of the tank is ", tank1.tankRect.left())
	pygame.display.update()
	a = input("Ready to move to the next test?")

	#This tests proper movement in the negative x direction
	#print("The old x-pos of the tank is ", tank1.tankRect.x())
	tank1.move(pygame.K_LEFT)
	#print("The new x-pos of the tank is ", tank1.tankRect.x())
	a = input("Ready to move to the next test?")

	#This tests the upward angular movement of the shootything
	print("The old x-pos and y-pos of the tank is:", tank1.shootyThingRect.x(), "and", tank1.shootyThingRect.y())
	tank1.angle(pygame.K_UP)
	print("The new x-pos and y-pos of the tank is:", tank1.shootyThingRect.x(), "and", tank1.shootyThingRect.y())

	#This tests the downward angular movement of the shootything
	print("The old x-pos and y-pos of the tank is:", tank1.shootyThingRect.x(), "and", tank1.shootyThingRect.y())
	tank1.angle(pygame.K_DOWN)
	print("The new x-pos and y-pos of the tank is:", tank1.shootyThingRect.x(), "and", tank1.shootyThingRect.y())

	#This tests to see if the tank will move if non-essential keys are pressed
	print("The old x-pos of the tank is ", tank1.tankRect.x())
	tank1.move(pygame.K_V)
	print("The new x-pos of the tank is ", tank1.tankRect.x())

	print("The old x-pos of the tank is ", tank1.tankRect.x())
	tank1.move(pygame.K_4)
	print("The new x-pos of the tank is ", tank1.tankRect.x())

	print("The old x-pos of the tank is ", tank1.tankRect.x())
	tank1.move(pygame.K_BACKSLASH)
	print("The new x-pos of the tank is ", tank1.tankRect.x())

	#This tests to see if the shootything moves if non-essential keys are pressed
	print("The old x-pos and y-pos of the tank is:", tank1.shootyThingRect.x(), "and", tank1.shootyThingRect.y())
	tank1.angle(pygame.K_V)
	print("The new x-pos and y-pos of the tank is:", tank1.shootyThingRect.x(), "and", tank1.shootyThingRect.y())

	print("The old x-pos and y-pos of the tank is:", tank1.shootyThingRect.x(), "and", tank1.shootyThingRect.y())
	tank1.angle(pygame.K_4)
	print("The new x-pos and y-pos of the tank is:", tank1.shootyThingRect.x(), "and", tank1.shootyThingRect.y())

	print("The old x-pos and y-pos of the tank is:", tank1.shootyThingRect.x(), "and", tank1.shootyThingRect.y())
	tank1.angle(pygame.K_BACKSLASH)
	print("The new x-pos and y-pos of the tank is:", tank1.shootyThingRect.x(), "and", tank1.shootyThingRect.y())

	#This tests to see if the bullet is created when teh tank should shoot
	shot = tank1.shoot(pygame.K_SPACE)
	print(type(shot))
	print("The x-pos and y-pos of the bullet is", shot.bulletRect.x(), "and", shot.bulletRect.y())

	#This tests to see if the bullet moves properly
	for i in range(5):
		shot_coor = shot.update()
		print("The x-pos and y-pos of the bullet is", shot_coor)
	#This tests

	#More power== key held down
	#Transform - rotating objects


test()
