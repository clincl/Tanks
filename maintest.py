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
	print("The old x-pos of the tank is ", tank.xpos())
	tank.move(K_LEFT))
	print("The new x-pos of the tank is ", tank.xpos())	
	
	#This tests proper movement in the negative x direction
	print("The old x-pos of the tank is ", tank.xpos())
	tank.move(K_RIGHT))
	print("The new x-pos of the tank is ", tank.xpos())	
	
	#This tests the upward angular movement of the shootything

	#This tests the downward angular movement of the shootything

	#This tests to see if the tank will move if non-essential keys are pressed
 	print("The old x-pos of the tank is ", tank.xpos())
	tank.move(K_V))
	print("The new x-pos of the tank is ", tank.xpos())

	print("The old x-pos of the tank is ", tank.xpos())
	tank.move(K_4))
	print("The new x-pos of the tank is ", tank.xpos())

	print("The old x-pos of the tank is ", tank.xpos())
	tank.move(K_BACKSLASH))
	print("The new x-pos of the tank is ", tank.xpos())

	#This tests to see if the shootything moves if non-essential keys are pressed

	#This tests to see if the tank shoots properly
	tank.shoot(K_SPACE)

	#This tests to see if the tank takes damage when hit
	
	#This tests
	
	#More power== key held down
	#Transform - rotating objects


test()
