import random
import sys
import numpy as py4
from random import randint
import time
from tkinter import *

class dice:
	def __init__(self, master):
		self.master = master
		master.title("Boggle 2.0") #Window header
		self.root = Tk() #Setup for root window
		self.label = Label(master, text="Welcome to Boggle")
		self.label.pack()
		self.frame1 = Frame(self.root, width = 120, height = 120) #Window size for tkinter window
		self.frame1.grid()
		#establishing the empty bored 
		self.board = [[] for _ in range(4)]
		self.l = []
		self.letters = [['L', 'R', 'E', "V", 'D', "Y"],['R', 'N', 'Z', 'N', 'H', 'L'],['E', 'D', 'L', 'X', 'R', 'I'],['G','A','E','A','E','N'],['Qu', 'N', 'M', 'I', 'U', 'H'],
		['D', 'S', 'Y', 'I', 'T', 'T'],['I', 'T', 'S', 'E', 'S', 'O'],['S', 'N', 'E', 'I', 'E', 'U'],['R', 'Y', 'T', 'L', 'T', 'E'],['A', 'S', 'P', 'F', 'K', 'F'],
		['W', 'E', 'G', 'H', 'H', 'E'],['R', 'V', 'T', 'H', 'E', 'W'],['C', 'I', 'U', 'T', 'M', 'O'],['S','C','A','O','P','H'],['B', 'A', 'O', 'B', 'O', 'J'],
		['A', 'O', 'T', 'T', 'W', 'O']]
		self.assign_values()
		self.display() #Creates grid of buttons with mines and numbers
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

		#return self.board 

dice_roll = dice(Tk())
#dice_roll.assign_values()
#dice_roll.display()
