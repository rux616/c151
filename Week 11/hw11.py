#!/usr/bin/python
#
# Name: Dan Cassidy

###############################################################################
# Action:     Determine the largest element in the passed array.
#
# Parameters:
# IN:         Array, array which will be scanned
# OUT:        None
#
# Returns:    Max, the largest element found in the passed array
#
# Limits:     Array must be an array
###############################################################################
def MaxArray(Array):
	Max = Array[0]
	for Element in Array:
		if Element > Max:
			Max = Element
	return Max

###############################################################################
# Action:     Reverse the elements in the passed array.
#
# Parameters:
# IN:         Array, array whose elements will be reversed
# OUT:        None
#
# Returns:    Array, the newly reversed version of the original array
#
# Limits:     Array must be an array
###############################################################################
def ReverseArray(Array):
	N = len(Array) - 1
	for i in range(N/2):
		Temp = Array[i]
		Array[i] = Array[N - i]
		Array[N - i] = Temp
	return Array

if __name__ == '__main__':
	TestArray = [3, 1, 6, 2, 4, 9, 0]
	print MaxArray(TestArray)
	print ReverseArray(TestArray)

