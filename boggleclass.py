import random
import sys
import numpy as py4
from random import randint

#A class for GUI (Graphical User Interface) - this class will establish basic functions and an open list that can be appended to eventually to make the actual board in Tkinter. 
class gui_board:
	#constructor
	def __init__(self, master):

		self.master = master
		#self.array and self.master and self.letters are functions and values used later in the Tkinter that will need to be edited and modified later
		self.array

	def setup():#Setup for board
# this class is a dice class and includes a list for each the 6 posibilities of the 16 different dice and will assign random values to these dice and random locations on the bored
class dice:
	def __init__():
		self.letters =
		#list of dice outputs
		[['L', 'R', 'E', "V", 'D', "Y"]['R', 'N', 'Z', 'N', 'H', 'L']['E', 'D', 'L', 'X', 'R', 'I']['G','A','E','A','E','N']['QU', 'N', 'M', 'I', 'U', 'H']
		['D', 'S', 'Y', 'I', 'T', 'T']['I', 'T', 'S', 'E', 'S', 'O']['S', 'N', 'E', 'I', 'E', 'U']['R', 'Y', 'T', 'L', 'T', 'E']['A', 'S', 'P', 'F'. 'K', 'F']
		['W', 'E', 'G', 'H', 'H', 'E']['R', 'V', 'T', 'H', 'E', 'W']['C', 'I', 'U', 'T', 'M', 'O']['S','C','A','O','P','H']['B', 'A', 'O', 'B', 'O', 'J']
		['A', 'O', 'T', 'T', 'W', 'O']]
		#establishing the empty bored 
		self.board = [[][][][]]

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

#this class is pretty simple and allows us to put a timer on the game that the user can actually choose before they make words
class timer:
	def __init__(self, time): #User can input time at beginning of the game
		self.time = time

	def duration(self, time): #Sets up a timer which'll send off a siren mp3

#this class is complicated and will be used to check to make sure that the words found on the bored can actually be found on the bored 
class check(): 
	def __init__(self):

	def checkcord(): #checks to make sure letters are adjacent to eachother on the gameboard 
		
	def nodoubles(): #makes sure there are no doubles on the game bored

	#Returns true or false statment for fucntions in points class to run
