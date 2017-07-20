#!/usr/bin/python
#
# Name:			Dan Cassidy
# Homework:		12

from random import *

###############################################################################
# Action:     Create an arbitrarily sized array and fill it with sequential
#             numbers starting at 1.
#
# Parameters:
# IN:         n, number of elements the array is to contain
# OUT:        None
#
# Returns:    Array, the created array
#
# Limits:     n must be a positive integer
###############################################################################
def makeArray(n):
	Array = []
	for i in range(n):
		Array.append(i + 1)
		
	return Array

###############################################################################
# Action:     Shuffles the elements of an array.
#
# Parameters:
# IN:         Array, the array to be shuffled
# OUT:        None
#
# Returns:    ShuffledArray, the shuffled array
#
# Limits:     Array must not be empty
###############################################################################
def shuffleArray(Array):
	#Copy the array to ensure it is not overwritten
	ShuffledArray = Array
	
	for i in range(len(ShuffledArray) - 1):
		Rand = randint(0, len(ShuffledArray) - 1)
		if Rand != i:
			Temp = ShuffledArray[i]
			ShuffledArray[i] = ShuffledArray[Rand]
			ShuffledArray[Rand] = Temp
	
	return ShuffledArray

if __name__ == '__main__':
	#Get user input
	ArraySize = input("Please enter the number of elements: ")
	
	#Create and display array
	UserArray = makeArray(ArraySize)
	print "Default array created:", UserArray
	
	#Randomize and display array
	ShuffledUserArray = shuffleArray(UserArray)
	print "Array after randomization:", ShuffledUserArray

#TEST OUTPUT
#-----------
#Please enter the number of elements: 10
#Default array created: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Array after randomization: [5, 1, 9, 4, 7, 6, 8, 2, 3, 10]

