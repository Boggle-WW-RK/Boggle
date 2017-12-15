import random
import sys
import numpy as py4
from random import randint
class gui_board:
	def __init__(self, master): 
		self.master = master
		self.array
		self.letters =
		[['L', 'R', 'E', "V", 'D', "Y"]['R', 'N', 'Z', 'N', 'H', 'L']['E', 'D', 'L', 'X', 'R', 'I']['G','A','E','A','E','N']['QU', 'N', 'M', 'I', 'U', 'H']
		['D', 'S', 'Y', 'I', 'T', 'T']['I', 'T', 'S', 'E', 'S', 'O']['S', 'N', 'E', 'I', 'E', 'U']['R', 'Y', 'T', 'L', 'T', 'E']['A', 'S', 'P', 'F'. 'K', 'F']
		['W', 'E', 'G', 'H', 'H', 'E']['R', 'V', 'T', 'H', 'E', 'W']['C', 'I', 'U', 'T', 'M', 'O']['S','C','A','O','P','H']['B', 'A', 'O', 'B', 'O', 'J']
		['A', 'O', 'T', 'T', 'W', 'O']]
		self.board = [[][][][]]
	def setup():#Setup for board

class dice:
	def __init__():

	def assign_values(self): #Assigns a letter from the dictionary for each of the 16 cubes
		counter = 0
		for i in range(15):
			counter+=1
			if counter < 4:
				self.board[0][0].append(random(self.letters[randint(0,15)]))  #Pick random array, pick random element, delete element while keeping order
			if counter < 8 && counter > 3:
				self.board[0][1].append(random(self.letters[randint(0,15)]))
			if counter > 7 && counter < 12:
				self.board[0][2].append(random(self.letters[randint(0,15)]))
			if counter > 11 && counter < 16:
				self.board[0][3].append(random(self.letters[randint(0,15)]))
		for i in range(3)
			print(self.board[0][i])
	def random_pos(self): #Gives position board for each cube

class points: 
	def __init__(self, word): #Needs word for input
		self.word = word
		self.score = 0

	def point_assign(self): #Takes word and takes length of it
		if len(self.word) <= 4:
			self.score+=1
		elif len(self.word) <= 5:
			self.score+=2
		elif len(self.word) <= 6:
			self.score+=3
		elif len(self.word) <= 7:
			self.score+=5
		elif len(self.word) >= 8:
			self.score+=11


class timer:
	def __init__(self, time): #User can input time at beginning of the game
		self.time = time

	def duration(self, time): #Sets up a timer which'll send off a siren mp3


class check(): 
	def __init__(self):

	def checking(): #Makes sure word is continuous

	#Returns true or false statment for fucntions in points class to run