import pygame as pg
import utility as u
import tank
import bullet

class Window:
	def __init__(self, width=800, height=450):
		pg.init()
		self.width = width
		self.height = height
		self.screen = pg.display.set_mode((self.width, self.height))
		pg.display.set_caption('Tanks')#Nia	
		self.background = pg.Surface(self.screen.get_size()).convert()
		self.screen.blit(u.loadImage("myBackground.png")[0], (0,0))
		pg.display.flip()


def test():
	'''
	#This function contains the test code for the classes
	Arguments: None
	Returns: None
	'''
	x = Window()
	
	#This tests object (tank) creation
	tank1 = tank.Tank(10, 10, "myTank.png", "myShootyThing.png")
	pg.display.update() #Nia
	#This tests the class to ensure that the stats are assigned properly

	#This tests proper movement in the positive x direction
	#print(tank1.tankRect())
	for i in range(50):
		u.testMove(tank1.move(pg.K_RIGHT), x, tank1) 
	#print("The new x-pos of the tank is ", tank1.tankRect.left())
	a = input("Ready to move to the next test?")

	#This tests proper movement in the negative x direction
	#print("The old x-pos of the tank is ", tank1.tankRect.x())
	for i in range(50):
		u.testMove(tank1.move(pg.K_LEFT), x, tank1) 
	#print("The new x-pos of the tank is ", tank1.tankRect.x())
	a = input("Ready to move to the next test?")

	#This tests the upward angular movement of the shootything
	#print("The old x-pos and y-pos of the tank is:", tank1.shootyThingRect.x(), "and", tank1.shootyThingRect.y())
	angle = 0	
	for i in range(50):
		new_angle = u.testAngle(tank1.angle(pg.K_UP, angle), angle, x, tank1)
		angle = new_angle
	#print("The new x-pos and y-pos of the tank is:", tank1.shootyThingRect.x(), "and", tank1.shootyThingRect.y())
	a = input("Ready to move to the next test?")

	#This tests the downward angular movement of the shootything
	#print("The old x-pos and y-pos of the tank is:", tank1.shootyThingRect.x(), "and", tank1.shootyThingRect.y())
	for i in range(50):
		new_angle = u.testAngle(tank1.angle(pg.K_UP, angle), angle, x, tank1)
		angle = new_angle
	#print("The new x-pos and y-pos of the tank is:", tank1.shootyThingRect.x(), "and", tank1.shootyThingRect.y())
	a = input("Ready to move to the next test?")

	#This tests to see if the tank will move if non-essential keys are pressed
	for i in u.INVALID_INPUTS:
		u.testMove(tank1.move(i), x, tank1) 

	#This tests to see if the shootything moves if non-essential keys are pressed
	for i in u.INVALID_INPUTS:
		u.testMove(tank1.move(i), x, tank1) 

	#This tests to see if the bullet is created when teh tank should shoot
	shot = tank1.shoot(pg.K_SPACE)
	x.screen.blit(tank1.tankImage, (tank1.tankRect.x,tank1.tankRect.y))
	x.screen.blit(tank1.shootyThingImage, (tank1.shootyThingRect.x,tank1.shootyThingRect.y))
	x.screen.blit(shot.bulletImage, (shot.bulletRect.x,shot.bulletRect.y))
	pg.display.update()

	a = input("Ready to move to the next test?")

	#This tests to see if the bullet moves properly
	for i in range(5):
		shot_coor = shot.update()
		print("The x-pos and y-pos of the bullet is", shot_coor)
	#This tests

	#More power== key held down
	#Transform - rotating objects


test()

'''
#This is the updated main code for reference
import pygame
import tank
import bullet
import utility
import time

class Window:
	def __init__(self, width=800, height=450):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption('Tanks')#Nia	
		self.background = pygame.Surface(self.screen.get_size()).convert()
		self.screen.blit(utility.loadImage("myBackground.png")[0], (0,0))
		pygame.display.flip()


def test():
	#''
	#This function contains the test code for the classes
	#Arguments: None
	#Returns: None
	#''
	x = Window()
	
	#This tests object (tank) creation
	tank1 = tank.Tank(10, 10, "myTank.png", "myShootyThing.png")
	pygame.display.update() #Nia
	#This tests the class to ensure that the stats are assigned properly

	#This tests proper movement in the positive x direction
	pos = utility.testMove(20, pygame.K_RIGHT, x, tank1)
	print("Changing input from right to d!")
	pos = utility.testMove(20, pygame.K_d, x, tank1)
	a = input("Ready to move to the next test?")

	#This tests proper movement in the negative x direction
	print("The initial x-pos of the tank is ", tank1.tankRect.x)
	pos = utility.testMove(20, pygame.K_LEFT, x, tank1)
	print("Changing input from left to a!")
	pos = utility.testMove(20, pygame.K_a, x, tank1)
	print("The final x-pos of the tank is ", tank1.tankRect.x)
	a = input("Ready to move to the next test?")

	#''	
	#This tests the upward angular movement of the shootything
	print("The initial x-pos and y-pos of the shootyThing is:", tank1.shootyThingRect.x, "and", tank1.shootyThingRect.y)	
	angle = 0	
	new_angle = utility.testAngle(15, pygame.K_UP, angle, x, tank1)
	new_angle = utility.testAngle(15, pygame.K_w, angle, x, tank1)
	print("The final x-pos and y-pos of the tank is:", tank1.shootyThingRect.x, "and", tank1.shootyThingRect.y)
	a = input("Ready to move to the next test?")

	#This tests the downward angular movement of the shootything
	#print("The old x-pos and y-pos of the tank is:", tank1.shootyThingRect.x(), "and", tank1.shootyThingRect.y())
	new_angle = utility.testAngle(15, pygame.K_DOWN, new_angle, x, tank1)
	new_angle = utility.testAngle(15, pygame.K_s, new_angle, x, tank1)	
	angle = new_angle
	#print("The new x-pos and y-pos of the tank is:", tank1.shootyThingRect.x(), "and", tank1.shootyThingRect.y())
	a = input("Ready to move to the next test?")
	#''
	#This tests to see if the tank will move if non-essential keys are pressed
	for i in utility.INVALID_INPUTS:
		pos = utility.testMove(1, i, x, tank1) 
		print("The new position of the tank is ", pos) 
	a = input("Ready to move to the next test?")

	#This tests to see if the shootything moves if non-essential keys are pressed
	for i in utility.INVALID_INPUTS:
		pos = utility.testAngle(1, i, x, tank1) 
		print("The new position of the tank is ", pos) 
	a = input("Ready to move to the next test?")

	#This tests to see if the bullet is created when teh tank should shoot
	shot = tank1.shoot(pygame.K_SPACE)
	x.screen.blit(tank1.tankImage, (tank1.tankRect.x,tank1.tankRect.y))
	x.screen.blit(tank1.shootyThingImage, (tank1.shootyThingRect.x,tank1.shootyThingRect.y))
	x.screen.blit(shot.bulletImage, (shot.bulletRect.x,shot.bulletRect.y))
	pygame.display.update()

	a = input("Ready to move to the next test?")

	#This tests to see if the bullet moves properly
	for i in range(50):
		shot_coor = shot.update()
		x.screen.blit(shot.bulletImage, (shot.bulletRect.x,shot.bulletRect.y))
		pygame.display.flip()
		time.sleep(0.25)
		print("The x-pos and y-pos of the bullet is", shot_coor)
	a = input("Ready to move to the next test?")
	
	#This tests
'''
