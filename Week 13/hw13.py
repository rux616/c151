#!/usr/bin/python

# Name:	Dan Cassidy
# HW:	13

from random import *
from sys import *
from string import *


#A constant defining the maximum quantity of numbers that will be written to a
#single line.
NUMBERS_PER_LINE = 20


################################################################################
# Action:		Writes a file to the hard drive that has a number of random
#				numbers written to it, based on the inputs given.
#
# PARAMETERS
# In:			filename, holds the file name of the file to be written
# In:			size, holds the quantity of numbers that will be generated
# In:			limit, holds the highest value that a random number should be
# Out:			None
#
# Returns:		Nothing
#
# Restrictions:	User must have permissions to write to filename, size must be a
#				positive ingteger, and limit must be a non-negative integer
################################################################################
def generateNumbers(filename, size, limit):
	fout = open(filename, "w")
	fout.writelines("%d\n" %(size))
	
	strOut = ""
	
	for i in range(size):
		n = randint(0, limit)
		if strOut == "":
			strOut = "%d" %(n)
		else:
			strOut = "%s %d" %(strOut, n)
		if (i + 1) % NUMBERS_PER_LINE == 0:
			fout.writelines("%s\n" %(strOut))
			strOut = ""
	
	fout.writelines("%s\n" %(strOut))
	
	fout.close()


################################################################################
# Action:		Reads a file from the hard drive that has a number of random
#				numbers written to it.
#
# PARAMETERS
# In:			filename, holds the file name of the file to be read
# Out:			None
#
# Returns:		result, an array holding the numbers read from the file
#
# Restrictions:	filename must exist and the user must have read permissions
################################################################################
def readFile(filename):
	fin = open(filename, "r")
	line = fin.readline()
	size = int(line)
	result = []
	
	while len(result) < size:
		line = fin.readline()
		numbers = split(line, " ")
		for n in numbers:
			result.append(int(n))
	
	return result


if __name__ == '__main__':
	if len(argv) < 4:
		print "Usage: hw13.py <FILE> <QUANTITY> <MAXIMUM>"
		print "Generates a FILE with a QUANTITY of random numbers between 0 and MAXIMUM."
	else:
		FileName = argv[1]
		QuantityOfNumbers = int(argv[2])
		UpperLimit = int(argv[3])
		
		generateNumbers(FileName, QuantityOfNumbers, UpperLimit)
		
		print readFile(FileName)

