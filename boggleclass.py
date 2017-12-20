import random
import sys
import numpy as py4
from random import randint
import time
from tkinter import *

#A class for GUI (Graphical User Interface) - this class will establish basic functions and an open list that can be appended to eventually to make the actual board in Tkinter. 
<<<<<<< HEAD

=======
>>>>>>> d7be0b3e24e9b060c98216a8ce7cf785587d9f68
#add new grid, while loop if this block is not hit don't run, keep adding during while 
#empty array vairable for user input
#clear button if user doesn't want to do word
# this class is a dice class and includes a list for each the 6 posibilities of the 16 different dice and will assign random values to these dice and random locations on the bored
<<<<<<< HEAD
'''
class gui_board:
	#constructor

=======

class gui_board:
	#constructor
>>>>>>> d7be0b3e24e9b060c98216a8ce7cf785587d9f68
	def __init__(self, master):
		self.master = master
		master.title("Boggle 2.0") #Window header
		self.root = Tk() #Setup for root window
		self.label = Label(master, text="Welcome to Boggle")
		self.label.pack()
		self.frame1 = Frame(self.root, width = 120, height = 120) #Window size for tkinter window
		self.frame1.grid()
		#self.array and self.master and self.letters are functions and values used later in the Tkinter that will need to be edited and modified later
'''
# this class is a dice class and includes a list for each the 6 posibilities of the 16 different dice and will assign random values to these dice and random locations on the bored
class dice:
<<<<<<< HEAD
	def __init__(self, master):
		self.master = master
		master.title("Boggle 2.0") #Window header
		self.root = Tk() #Setup for root window
		self.label = Label(master, text="Welcome to Boggle")
		self.label.pack()
		self.frame1 = Frame(self.root, width = 120, height = 120) #Window size for tkinter window
		self.frame1.grid()
=======
	def __init__():
		self.letters =
		#list of dice outputs
		[['L', 'R', 'E', "V", 'D', "Y"]['R', 'N', 'Z', 'N', 'H', 'L']['E', 'D', 'L', 'X', 'R', 'I']['G','A','E','A','E','N']['QU', 'N', 'M', 'I', 'U', 'H']
		['D', 'S', 'Y', 'I', 'T', 'T']['I', 'T', 'S', 'E', 'S', 'O']['S', 'N', 'E', 'I', 'E', 'U']['R', 'Y', 'T', 'L', 'T', 'E']['A', 'S', 'P', 'F'. 'K', 'F']
		['W', 'E', 'G', 'H', 'H', 'E']['R', 'V', 'T', 'H', 'E', 'W']['C', 'I', 'U', 'T', 'M', 'O']['S','C','A','O','P','H']['B', 'A', 'O', 'B', 'O', 'J']
		['A', 'O', 'T', 'T', 'W', 'O']]
>>>>>>> d7be0b3e24e9b060c98216a8ce7cf785587d9f68
		#establishing the empty bored 
		self.board = [[] for _ in range(4)]
		self.l = []

		#Label(master, text="Word Input:").grid(row=0)
		#Label(master, text="Last Name").grid(row=1)
		#e1 = Entry(master)
		#e1.grid(row=0, column=1)


		self.letters = [['L', 'R', 'E', "V", 'D', "Y"],['R', 'N', 'Z', 'N', 'H', 'L'],['E', 'D', 'L', 'X', 'R', 'I'],['G','A','E','A','E','N'],['Qu', 'N', 'M', 'I', 'U', 'H'],
		['D', 'S', 'Y', 'I', 'T', 'T'],['I', 'T', 'S', 'E', 'S', 'O'],['S', 'N', 'E', 'I', 'E', 'U'],['R', 'Y', 'T', 'L', 'T', 'E'],['A', 'S', 'P', 'F', 'K', 'F'],
		['W', 'E', 'G', 'H', 'H', 'E'],['R', 'V', 'T', 'H', 'E', 'W'],['C', 'I', 'U', 'T', 'M', 'O'],['S','C','A','O','P','H'],['B', 'A', 'O', 'B', 'O', 'J'],
		['A', 'O', 'T', 'T', 'W', 'O']]
		self.assign_values()
		self.display() #Creates grid of buttons with dice values 
		# self.play()#Calls main function which plays
		self.root.mainloop() #setup window
	
	def display(self): #Setup for GUI window 10x10 window
		for r in range(4):
			for c in range(4):
				button = Button(self.frame1, text=str(self.board[r][c]), width = 2, height = 2, padx = 20, pady = 5)#This is how you create a button.
				#button = Button(self.frame1, text=str(self.board[r][c]), width = 2, height = 2, padx = 20, pady = 5, command =partial(self.play, r, c))#This is how you create a button.
				## the label is in the top row so add one to each row
				button.grid(row=r, column=c)
		

	def assign_values(self): #Assigns a letter from the dictionary for each of the 16 cubes
		counter = -1
		dice = 15
		for i in range(16):
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
		for i in range(4):
			print(self.board[i])


	#def intro():
<<<<<<< HEAD


	
=======
	#def random_pos(self, board): #Gives position board for each cube: If we have time, we can do a shuffle where we reoganize all the letters on the board
>>>>>>> d7be0b3e24e9b060c98216a8ce7cf785587d9f68

class timer():
    def __init__(self):
        self.initial = 180

    def start_time():
        # timeit.timeit(howlong)
        for i in range(180):
            if i > 0: 
                i -= 1
                current = i
                time.sleep(1)

	
class scoring(self):
    def __init__(self, userword): 
        self.word = userword
        self.score = 0

    def pointawarding(self): 
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

class end_game:
	def __init__(self, time, score):
		self.time = time
		self.score = score
	def display():
		self.label = Label(text="Great Job!")
        self.label.pack()

<<<<<<< HEAD
=======

>>>>>>> d7be0b3e24e9b060c98216a8ce7cf785587d9f68
#this class is complicated and will be used to check to make sure that the words found on the bored can actually be found on the bored 
class check(): 
	def __init__(self, word, coord):

	def checkcord(): #checks to make sure letters are adjacent to eachother on the gameboard 
		a1 = []
		for char in self.word:
			al.append(char)
		for char in a1:
			if [r+1, c] in self.mines:  #0
			if a[char]
      		if [r+1, c+1] in self.mines:
         	
      		if [r, c+1] in self.mines:
         			self.near+=1
      		if [r-1, c+1] in self.mines:
         			self.near+=1
      		if [r-1, c] in self.mines:
         			self.near+=1
      		if [r-1, c-1] in self.mines:
         			self.near+=1
      		if [r, c-1] in self.mines:
         			self.near+=1
      		if [r+1, c-1] in self.mines:
         			self.near+=1

		else:
			return False
<<<<<<< HEAD

=======
>>>>>>> d7be0b3e24e9b060c98216a8ce7cf785587d9f68
	def checkcord(): #checks to make sure letters are adjacent to eachother on the gameboard 
		
	def nodoubles(): #makes sure there are no doubles on the game bored

	#Returns true or false statment for fucntions in points class to run

<<<<<<< HEAD




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

=======
>>>>>>> d7be0b3e24e9b060c98216a8ce7cf785587d9f68















