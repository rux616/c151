#!/usr/bin/python
#
# Name: Dan Cassidy
# Lab Number: 12

from string import *
from random import *


def words():
	word1 = "Stapler before dawn"
	word2 = "Waiting in perfect silence"
	word3 = "Dreams of loose paper"
	poem = word1 + "\n" + word2 + "\n" + word3
	
	print poem


def wordsArray():
	word1 = "This my lab 12 file."
	word2 = "There are many like it."
	word3 = "But this one is mine."
	poem = word1 + "\n" + word2 + "\n" + word3
	
	sentence = split(poem, "\n")
	print sentence
	
	for w in sentence:
		print w
	
	print join(sentence, "\n\n")
	pos = find(poem, word2)
	print "the second line starts at position", pos, "in the string"
	

def wordsRandom():
	word1 = "Stapler before dawn"
	word2 = "Waiting in perfect silence"
	word3 = "Dreams of loose paper"
	poem = word1 + " " + word2 + " " + word3
	
	sentence = split(poem, " ")
	
	for i in range(len(sentence)):
		sentence[i] = lower(sentence[i])
	
	print poem
	
	L = len(sentence)
	for i in range(L):
		#sentence[i] = lower(sentence[i])
		j = randint(0, L - 1)
		if i == 0:
			print capitalize(sentence[j]),
		else:
			print sentence[j],
	

if __name__ == '__main__':
	wordsRandom()
	
