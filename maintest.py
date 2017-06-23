import pygame
import tank
import bullet
import utility
def test():
	'''
	This function contains the test code for the classes
	Arguments: None
	Returns: None
	'''
	#This tests object creation
	tank = Tank()
	print(type(tank))
	
	#This tests the class to ensure that the stats are assigned properly

	#This tests proper movement in the positive x direction
	print("The old x-pos of the tank is ", tank.tankRect.x())
	tank.move(pygame.K_RIGHT)
	print("The new x-pos of the tank is ", tank.tankRect.x())	
	
	#This tests proper movement in the negative x direction
	print("The old x-pos of the tank is ", tank.tankRect.x())
	tank.move(pygame.K_LEFT)
	print("The new x-pos of the tank is ", tank.tankRect.x())	
	
	#This tests the upward angular movement of the shootything
	print("The old x-pos and y-pos of the tank is:", tank.shootyThingRect.x(), "and", tank.shootyThingRect.y())
	tank.angle(pygame.K_UP)
	print("The new x-pos and y-pos of the tank is:", tank.shootyThingRect.x(), "and", tank.shootyThingRect.y())
	
	#This tests the downward angular movement of the shootything
	print("The old x-pos and y-pos of the tank is:", tank.shootyThingRect.x(), "and", tank.shootyThingRect.y())
	tank.angle(pygame.K_DOWN)
	print("The new x-pos and y-pos of the tank is:", tank.shootyThingRect.x(), "and", tank.shootyThingRect.y())
	
	#This tests to see if the tank will move if non-essential keys are pressed
	print("The old x-pos of the tank is ", tank.tankRect.x())
	tank.move(pygame.K_V)
	print("The new x-pos of the tank is ", tank.tankRect.x())

	print("The old x-pos of the tank is ", tank.tankRect.x())
	tank.move(pygame.K_4)
	print("The new x-pos of the tank is ", tank.tankRect.x())

	print("The old x-pos of the tank is ", tank.tankRect.x())
	tank.move(pygame.K_BACKSLASH)
	print("The new x-pos of the tank is ", tank.tankRect.x())

	#This tests to see if the shootything moves if non-essential keys are pressed
	print("The old x-pos and y-pos of the tank is:", tank.shootyThingRect.x(), "and", tank.shootyThingRect.y())
	tank.angle(pygame.K_V)
	print("The new x-pos and y-pos of the tank is:", tank.shootyThingRect.x(), "and", tank.shootyThingRect.y())
	
	print("The old x-pos and y-pos of the tank is:", tank.shootyThingRect.x(), "and", tank.shootyThingRect.y())
	tank.angle(pygame.K_4)
	print("The new x-pos and y-pos of the tank is:", tank.shootyThingRect.x(), "and", tank.shootyThingRect.y())
	
	print("The old x-pos and y-pos of the tank is:", tank.shootyThingRect.x(), "and", tank.shootyThingRect.y())
	tank.angle(pygame.K_BACKSLASH)
	print("The new x-pos and y-pos of the tank is:", tank.shootyThingRect.x(), "and", tank.shootyThingRect.y())
	
	#This tests to see if the tank shoots properly
	tank.shoot(pygame.K_SPACE)

	#This tests to see if the tank takes damage when hit
	
	#This tests
	
	#More power== key held down
	#Transform - rotating objects


test()
