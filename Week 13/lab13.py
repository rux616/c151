#!/usr/bin/python

# Name:	Dan Cassidy
# Lab:	13

from sys import *
from os import *


################################################################################
# Action:		Convert the
#
# PARAMETERS
# In:			text, an array containing strings of integers
# Out:			None
#
# Returns:		result, an array containing integers converted from text
#
# Restrictions:	text must be a non-empty array and must contain only string-ified integers
################################################################################
def strs2int(text):
	result = []
	for i in text:
		result.append(int(i))
		
	return result


################################################################################
# Action:		Prints some system information to the output screen.
#
# PARAMETERS
# In:			None
# Out:			None
#
# Returns:		Nothing
#
# Restrictions:	None
################################################################################
def sysInfo():
	print "\nsys.executable: Gives the absolute path of the executable binary for the Python interpreter."
	print executable #sys.executable
	print "\nsys.maxint: The largest positive integer supported by Python's regular integer type."
	print maxint #sys.maxint
	print "\nsys.path: A list of strings that specifies the search path for modules."
	print path #sys.path
	print "\nsys.platform: A string containing a platform identifier."
	print platform #sys.platform
	print "\nsys.version: A string containing the version number of the Python interpreter plus additional information on the build number and compiler used."
	print version #sys.version
	
	print "\nUser name:", environ['USER']
	print "Home directory:", environ['HOME']
	
	u = uname()
	print "Operating System:", u[0]
	print "Computer Name:", u[1]


if __name__ == '__main__':
	print "Command line arguments:", argv
	
	size = len(argv)
	
	if size > 1:
		numbers = strs2int(argv[1:size])
	
	print "Numbers extracted from command line arguments:", numbers
	print "Max number:", max(numbers)
	
	sysInfo()
	
	system("ls")
	
	filelist = listdir(".")
	for files in filelist:
		print files,

