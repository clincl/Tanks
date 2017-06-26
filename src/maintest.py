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
	
	#This tests the class to ensure that the init values of the tank and shootything are assigned properly
	print("Health =", tank1.health)
	print("Speed =", tank1.tankSpeed)
	print("Tank X-pos =", tank1.tankRect.x)
	print("Tank Y-pos =", tank1.tankRect.y)
	print("ShootyThing X-pos =", tank1.shootyThingRect.x)
	print("ShootyThing Y-pos =", tank1.shootyThingRect.y)
	
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
	new_angle = utility.testAngle(15, pygame.K_w, new_angle, x, tank1)
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
		pos = utility.testAngle(1, i, angle, x, tank1) 
		print("The new position of the tank is ", pos) 
	a = input("Ready to move to the next test?")

	#This tests to see if the bullet is created when teh tank should shoot
	shot = tank1.shoot(pygame.K_SPACE)
	x.screen.blit(tank1.tankImage, (tank1.tankRect.x,tank1.tankRect.y))
	x.screen.blit(tank1.shootyThingImage, (tank1.shootyThingRect.x,tank1.shootyThingRect.y))
	x.screen.blit(shot.bulletImage, (shot.bulletRect.x,shot.bulletRect.y))
	pygame.display.update()
	a = input("Ready to move to the next test?")
	
	#This tests the class to ensure that the init values of the bullet are assigned properly
	print("ShootyThing X-pos =", tank1.shootyThingRect.x)
	print("ShootyThing Y-pos =", tank1.shootyThingRect.y)
	print("Bullet X-pos =", tank1.bulletRect.x)
	print("Bullet Y-pos =", tank1.bulletRect.y)

	#This tests to see if the bullet moves properly
	for i in range(50):
		shot_coor = shot.update()
		x.screen.blit(shot.bulletImage, (shot.bulletRect.x,shot.bulletRect.y))
		pygame.display.flip()
		time.sleep(0.25)
		print("The x-pos and y-pos of the bullet is", shot_coor)
	a = input("Ready to move to the next test?")
	
	#This tests to see if the tank moves when essential keys for other methods are pressed
	pos = utility.testMove(1, pygame.K_UP, x, tank1)
	pos = utility.testMove(1, pygame.K_RSHIFT, x, tank1)
	pos = utility.testMove(1, pygame.K_SPACE, x, tank1)
	pos = utility.testMove(1, pygame.K_s, x, tank1)
	pos = utility.testMove(1, pygame.K_w, x, tank1)
	pos = utility.testMove(1, pygame.K_DOWN, x, tank1)
	
	a = input("Ready to move to the next test?")

	#This tests to see if the shootyThing moves when essential keys for other methods are pressed
	pos = utility.testAngle(1, pygame.K_LEFT, x, tank1)
	pos = utility.testAngle(1, pygame.K_RSHIFT, x, tank1)
	pos = utility.testAngle(1, pygame.K_SPACE, x, tank1)
	pos = utility.testAngle(1, pygame.K_a, x, tank1)
	pos = utility.testAngle(1, pygame.K_d, x, tank1)
	pos = utility.testAngle(1, pygame.K_right, x, tank1)
	
	a = input("Ready to move to the next test?")
	
	#This tests to see if the bullet shoots when essential keys for other methods are pressed
	pos = tank1.shoot(1, pygame.K_UP, x, tank1)
	print(type(pos))
	pos = tank1.shoot(1, pygame.K_LEFT, x, tank1)
	print(type(pos))
	pos = tank1.shoot(1, pygame.K_RIGHT, x, tank1)
	print(type(pos))
	pos = tank1.shoot(1, pygame.K_s, x, tank1)
	print(type(pos))
	pos = tank1.shoot(1, pygame.K_w, x, tank1)
	print(type(pos))
	pos = tank1.shoot(1, pygame.K_DOWN, x, tank1)
	print(type(pos))
	pos = tank1.shoot(1, pygame.K_a, x, tank1)
	print(type(pos))
	pos = tank1.shoot(1, pygame.K_d, x, tank1)
	print(type(pos))
	
test()	
