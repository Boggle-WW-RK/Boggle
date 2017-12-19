import random
import sys
import numpy as py4
from random import randint
import time

#A class for GUI (Graphical User Interface) - this class will establish basic functions and an open list that can be appended to eventually to make the actual board in Tkinter. 
class gui_board:
	#constructor
	def __init__(self, master):

		self.master = master
		#self.array and self.master and self.letters are functions and values used later in the Tkinter that will need to be edited and modified later
		self.array

	def setup():#Setup for board
<<<<<<< HEAD

class board_creator: #Done
	def __init__(self):
=======
# this class is a dice class and includes a list for each the 6 posibilities of the 16 different dice and will assign random values to these dice and random locations on the bored
class dice:
	def __init__():
		self.letters =
		#list of dice outputs
		[['L', 'R', 'E', "V", 'D', "Y"]['R', 'N', 'Z', 'N', 'H', 'L']['E', 'D', 'L', 'X', 'R', 'I']['G','A','E','A','E','N']['QU', 'N', 'M', 'I', 'U', 'H']
		['D', 'S', 'Y', 'I', 'T', 'T']['I', 'T', 'S', 'E', 'S', 'O']['S', 'N', 'E', 'I', 'E', 'U']['R', 'Y', 'T', 'L', 'T', 'E']['A', 'S', 'P', 'F'. 'K', 'F']
		['W', 'E', 'G', 'H', 'H', 'E']['R', 'V', 'T', 'H', 'E', 'W']['C', 'I', 'U', 'T', 'M', 'O']['S','C','A','O','P','H']['B', 'A', 'O', 'B', 'O', 'J']
		['A', 'O', 'T', 'T', 'W', 'O']]
>>>>>>> 4988f5952bb910a5608acda81a1c0b80aced3c07
		#establishing the empty bored 
		self.board = [[] for _ in range(4)]
		self.l = []
		self.letters = [['L', 'R', 'E', "V", 'D', "Y"],['R', 'N', 'Z', 'N', 'H', 'L'],['E', 'D', 'L', 'X', 'R', 'I'],['G','A','E','A','E','N'],['Qu', 'N', 'M', 'I', 'U', 'H'],
		['D', 'S', 'Y', 'I', 'T', 'T'],['I', 'T', 'S', 'E', 'S', 'O'],['S', 'N', 'E', 'I', 'E', 'U'],['R', 'Y', 'T', 'L', 'T', 'E'],['A', 'S', 'P', 'F', 'K', 'F'],
		['W', 'E', 'G', 'H', 'H', 'E'],['R', 'V', 'T', 'H', 'E', 'W'],['C', 'I', 'U', 'T', 'M', 'O'],['S','C','A','O','P','H'],['B', 'A', 'O', 'B', 'O', 'J'],
		['A', 'O', 'T', 'T', 'W', 'O']]
		
		

	def assign_values(self): #Assigns a letter from the dictionary for each of the 16 cubes
		counter = -1
		dice = 15
		for i in range(15):
			counter+=1
			if counter < 4:
				a = randint(0, dice)
				self.board[0].append(random.choice(self.letters[a]))  
				del self.letters[a]
				dice-=1
			if counter < 8 and counter > 3:
				b = randint(0, dice)
				self.board[1].append(random.choice(self.letters[b]))
				del self.letters[b]
				dice-=1
			if counter > 7 and counter < 12:
				c = randint(0, dice)
				self.board[2].append(random.choice(self.letters[c]))
				del self.letters[c]
				dice-=1
			if counter > 11 and counter < 16:
				d = randint(0, dice)
				self.board[3].append(random.choice(self.letters[d]))
				del self.letters[d]
				dice-=1
		for i in range(3):
			print(self.board[i])

		return self.board 


	#def random_pos(self, board): #Gives position board for each cube: If we have time, we can do a shuffle where we reoganize all the letters on the board


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

	def countdown(t): #https://stackoverflow.com/questions/25189554/countdown-clock-0105
    	while t:
        	mins, secs = divmod(t, 60)
        	timeformat = '{:02d}:{:02d}'.format(mins, secs)
        	print(timeformat, end='\r')
        	time.sleep(1)
        	t -= 1
    	print('Time is UP!\n\n\n\n\n')
		#countdown(180)

class end_game:
	def __init__(self, time, score):
		self.time = time
		self.score = score
	def display():


#this class is complicated and will be used to check to make sure that the words found on the bored can actually be found on the bored 
class check(): 
	def __init__(self):

	def checkcord(): #checks to make sure letters are adjacent to eachother on the gameboard 
		
	def nodoubles(): #makes sure there are no doubles on the game bored

	#Returns true or false statment for fucntions in points class to run

dice_roll = dice()
dice_roll.assign_values()



''' #Example
class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

mustang = Car('Ford', 'Mustang')
print mustang.wheels
# 4
print Car.wheels
# 4
'''
















