import random
import sys
import numpy as py4
from random import randint
import time
from tkinter import *
from functools import partial
import datetime
import math
from threading import Timer


class dice:
	def __init__(self, master):
		self.master = master
		master.title("Boggle 2.0") #Window header
		self.root = Tk() #Setup for root window
		#self.label = Label(master, , width = 60, height = 60)
		#self.label.pack()
		self.frame1 = Frame(self.root, width = 120, height = 120) #Window size for tkinter window
		self.frame1.grid()
		#establishing the empty bored 
		self.board = [[] for _ in range(4)]
		self.completed_words = []
		self.score=0
		self.start=True
		self.wordnow=''
		self.letters = [['L', 'R', 'E', "V", 'D', "Y"],['R', 'N', 'Z', 'N', 'H', 'L'],['E', 'D', 'L', 'X', 'R', 'I'],['G','A','E','A','E','N'],['Q', 'N', 'M', 'I', 'U', 'H'],
		['D', 'S', 'Y', 'I', 'T', 'T'],['I', 'T', 'S', 'E', 'S', 'O'],['S', 'N', 'E', 'I', 'E', 'U'],['R', 'Y', 'T', 'L', 'T', 'E'],['A', 'S', 'P', 'F', 'K', 'F'],
		['W', 'E', 'G', 'H', 'H', 'E'],['R', 'V', 'T', 'H', 'E', 'W'],['C', 'I', 'U', 'T', 'M', 'O'],['S','C','A','O','P','H'],['B', 'A', 'O', 'B', 'O', 'J'],
		['A', 'O', 'T', 'T', 'W', 'O']]
		self.assign_values()
		self.display() #Creates grid of buttons with mines and numbers
		# self.play()#Calls main function which plays
		self.root.mainloop() #setup window
		

	def display(self): #Setup for GUI window 10x10 window
		#intro = Label(self.root, text="Boggle is just a simple word search game. The player gets three minutes to find as many words on the board that are longer than two letters. Words can only be created by touching tiles (diagonal, vertical, or horizontal) only and you can not use the same tile twice in the same word.")
		msg = Message(self.master, text = "Instructions: Boggle is just a simple word search game. You get unlimited time to find as many words on the board that are longer than two letters. Words can only be created by touching tiles (diagonal, vertical, or horizontal) only and you can not use the same tile twice in the same word.")
		msg.config(bg='lightgreen', font=('times', 24, 'italic'))
		msg.pack()

		button2 = Label(self.frame1, text="Welcome to our Boggle Game!", width = 30, height = 3)
		button2.config(font=('Comic Sans MS', 24, 'italic'))
		button2.grid(row=0, column=0, columnspan = 8)

		enter = Button(self.frame1, text='Enter', width = 6, height = 3, command=self.entercheck)
		enter.grid(row=1, column=5, rowspan=2)


		clear = Button(self.frame1, text='Clear', width = 6, height = 3, command=self.clearword)
		clear.grid(row=1, column=6, rowspan=2)

		currentword1 = Label(self.frame1, text="Word:", width = 4, height = 2)
		currentword1.grid(row=3, column = 5, rowspan=2)
		currentword = Label(self.frame1, text= self.wordnow, width = 20, height = 2)
		currentword.grid(row=3, column=6, rowspan=2)

		
		scoreboard = Label(self.frame1, text='Score:',  width = 6, height = 3)
		scoreboard.grid(row=5, columns=5, rowspan=4)

		start = Button(self.frame1, text='Start', width = 6, height = 3, command=self.twofuncforstart)
		start.grid(row=5, column=6, rowspan=4)

		self.board_createnofunc()

	def twofuncforstart(self):
		self.board_create()
		self.falsefunc()

	def falsefunc(self):
		start = Button(self.frame1, text='End', width = 6, height = 3, command=self.root.destroy)
		start.grid(row=5, column=6, rowspan=4)

	def board_create(self):
		for r in range(4):
			for c in range(4):
				button = Button(self.frame1, text=str(self.board[r][c]), width = 6, height = 3, command=partial(self.greyout, r, c))#This is how you create a button.
				button.grid(row=r+1, column=c+1)
	def board_createnofunc(self):
			for r in range(4):
				for c in range(4):
					button = Button(self.frame1, text=str(self.board[r][c]), width = 6, height = 3)#No function
					button.grid(row=r+1, column=c+1)

	def greyout(self, r, c):
			
			self.wordnow+=self.board[r][c]
			currentword1 = Label(self.frame1, text="Word:", width = 4, height = 2)
			currentword1.grid(row=3, column = 5, rowspan=2)
			currentword = Label(self.frame1, text= self.wordnow, width = 20, height = 2)
			currentword.grid(row=3, column=6, rowspan=2)
			self.check(r,c)
		
	def check(self, r, c):
		self.board_createnofunc()
		if (r==1 and c==1) or (r==1 and c==2) or (r==2 and c==1) or (r==2 and c==2): #central
			r1 = r+1
			c1 = c
			button = Button(self.frame1, text=str(self.board[r1][c1]), width = 6, height = 3, command=partial(self.greyout, r1, c1))
			button.grid(row=r1+1, column=c1+1)

			r2 = r+1
			c2 = c+1
			button = Button(self.frame1, text=str(self.board[r2][c2]), width = 6, height = 3, command=partial(self.greyout, r2, c2))
			button.grid(row=r2+1, column=c2+1)

			r3 = r
			c3 = c+1
			button = Button(self.frame1, text=str(self.board[r3][c3]), width = 6, height = 3, command=partial(self.greyout, r3, c3))
			button.grid(row=r3+1, column=c3+1)

			r4 = r-1
			c4 = c+1
			button = Button(self.frame1, text=str(self.board[r4][c4]), width = 6, height = 3, command=partial(self.greyout, r4, c4))
			button.grid(row=r4+1, column=c4+1)

			r5 = r-1
			c5 = c
			button = Button(self.frame1, text=str(self.board[r5][c5]), width = 6, height = 3, command=partial(self.greyout, r5, c5))
			button.grid(row=r5+1, column=c5+1)

			r6 = r-1
			c6 = c-1
			button = Button(self.frame1, text=str(self.board[r6][c6]), width = 6, height = 3, command=partial(self.greyout, r6, c6))
			button.grid(row=r6+1, column=c6+1)

			r7 = r
			c7 = c-1
			button = Button(self.frame1, text=str(self.board[r7][c7]), width = 6, height = 3, command=partial(self.greyout, r7, c7))
			button.grid(row=r7+1, column=c7+1)

			r8 = r+1
			c8 = c-1
			button = Button(self.frame1, text=str(self.board[r8][c8]), width = 6, height = 3, command=partial(self.greyout, r8, c8))
			button.grid(row=r8+1, column=c8+1)
		

		if (r==1 and c==0) or (r==2 and c==0): # left two middle

			r1 = r+1
			c1 = c
			button = Button(self.frame1, text=str(self.board[r1][c1]), width = 6, height = 3, command=partial(self.greyout, r1, c1))
			button.grid(row=r1+1, column=c1+1)

			r2 = r+1
			c2 = c+1
			button = Button(self.frame1, text=str(self.board[r2][c2]), width = 6, height = 3, command=partial(self.greyout, r2, c2))
			button.grid(row=r2+1, column=c2+1)

			r3 = r
			c3 = c+1
			button = Button(self.frame1, text=str(self.board[r3][c3]), width = 6, height = 3, command=partial(self.greyout, r3, c3))
			button.grid(row=r3+1, column=c3+1)

			r4 = r-1
			c4 = c+1
			button = Button(self.frame1, text=str(self.board[r4][c4]), width = 6, height = 3, command=partial(self.greyout, r4, c4))
			button.grid(row=r4+1, column=c4+1)

			r5 = r-1
			c5 = c
			button = Button(self.frame1, text=str(self.board[r5][c5]), width = 6, height = 3, command=partial(self.greyout, r5, c5))
			button.grid(row=r5+1, column=c5+1)
		

		if (r==3 and c==1) or (r==3 and c==2): #bottom middle

			r3 = r
			c3 = c+1
			button = Button(self.frame1, text=str(self.board[r3][c3]), width = 6, height = 3, command=partial(self.greyout, r3, c3))
			button.grid(row=r3+1, column=c3+1)

			r4 = r-1
			c4 = c+1
			button = Button(self.frame1, text=str(self.board[r4][c4]), width = 6, height = 3, command=partial(self.greyout, r4, c4))
			button.grid(row=r4+1, column=c4+1)

			r5 = r-1
			c5 = c
			button = Button(self.frame1, text=str(self.board[r5][c5]), width = 6, height = 3, command=partial(self.greyout, r5, c5))
			button.grid(row=r5+1, column=c5+1)

			r6 = r-1
			c6 = c-1
			button = Button(self.frame1, text=str(self.board[r6][c6]), width = 6, height = 3, command=partial(self.greyout, r6, c6))
			button.grid(row=r6+1, column=c6+1)

			r7 = r
			c7 = c-1
			button = Button(self.frame1, text=str(self.board[r7][c7]), width = 6, height = 3, command=partial(self.greyout, r7, c7))
			button.grid(row=r7+1, column=c7+1)

		if (r==1 and c==3) or (r==2 and c==3):#right middle

			r1 = r+1
			c1 = c
			button = Button(self.frame1, text=str(self.board[r1][c1]), width = 6, height = 3, command=partial(self.greyout, r1, c1))
			button.grid(row=r1+1, column=c1+1)

			r5 = r-1
			c5 = c
			button = Button(self.frame1, text=str(self.board[r5][c5]), width = 6, height = 3, command=partial(self.greyout, r5, c5))
			button.grid(row=r5+1, column=c5+1)

			r6 = r-1
			c6 = c-1
			button = Button(self.frame1, text=str(self.board[r6][c6]), width = 6, height = 3, command=partial(self.greyout, r6, c6))
			button.grid(row=r6+1, column=c6+1)

			r7 = r
			c7 = c-1
			button = Button(self.frame1, text=str(self.board[r7][c7]), width = 6, height = 3, command=partial(self.greyout, r7, c7))
			button.grid(row=r7+1, column=c7+1)

			r8 = r+1
			c8 = c-1
			button = Button(self.frame1, text=str(self.board[r8][c8]), width = 6, height = 3, command=partial(self.greyout, r8, c8))
			button.grid(row=r8+1, column=c8+1)

		if (r==0 and c==1) or (r==0 and c==2):#top middle
			r1 = r+1
			c1 = c
			button = Button(self.frame1, text=str(self.board[r1][c1]), width = 6, height = 3, command=partial(self.greyout, r1, c1))
			button.grid(row=r1+1, column=c1+1)

			r2 = r+1
			c2 = c+1
			button = Button(self.frame1, text=str(self.board[r2][c2]), width = 6, height = 3, command=partial(self.greyout, r2, c2))
			button.grid(row=r2+1, column=c2+1)

			r3 = r
			c3 = c+1
			button = Button(self.frame1, text=str(self.board[r3][c3]), width = 6, height = 3, command=partial(self.greyout, r3, c3))
			button.grid(row=r3+1, column=c3+1)

			r7 = r
			c7 = c-1
			button = Button(self.frame1, text=str(self.board[r7][c7]), width = 6, height = 3, command=partial(self.greyout, r7, c7))
			button.grid(row=r7+1, column=c7+1)

			r8 = r+1
			c8 = c-1
			button = Button(self.frame1, text=str(self.board[r8][c8]), width = 6, height = 3, command=partial(self.greyout, r8, c8))
			button.grid(row=r8+1, column=c8+1)

		#top left
		if r==0 and c==0:
			r1 = r+1
			c1 = c
			button = Button(self.frame1, text=str(self.board[r1][c1]), width = 6, height = 3, command=partial(self.greyout, r1, c1))
			button.grid(row=r1+1, column=c1+1)

			r2 = r+1
			c2 = c+1
			button = Button(self.frame1, text=str(self.board[r2][c2]), width = 6, height = 3, command=partial(self.greyout, r2, c2))
			button.grid(row=r2+1, column=c2+1)

			r3 = r
			c3 = c+1
			button = Button(self.frame1, text=str(self.board[r3][c3]), width = 6, height = 3, command=partial(self.greyout, r3, c3))
			button.grid(row=r3+1, column=c3+1)

		#bottom left
		if r==3 and c==0:
			r3 = r
			c3 = c+1
			button = Button(self.frame1, text=str(self.board[r3][c3]), width = 6, height = 3, command=partial(self.greyout, r3, c3))
			button.grid(row=r3+1, column=c3+1)

			r4 = r-1
			c4 = c+1
			button = Button(self.frame1, text=str(self.board[r4][c4]), width = 6, height = 3, command=partial(self.greyout, r4, c4))
			button.grid(row=r4+1, column=c4+1)

			r5 = r-1
			c5 = c
			button = Button(self.frame1, text=str(self.board[r5][c5]), width = 6, height = 3, command=partial(self.greyout, r5, c5))
			button.grid(row=r5+1, column=c5+1)

			
		#bottom right
		if r==3 and c==3:


			r5 = r-1
			c5 = c
			button = Button(self.frame1, text=str(self.board[r5][c5]), width = 6, height = 3, command=partial(self.greyout, r5, c5))
			button.grid(row=r5+1, column=c5+1)

			r6 = r-1
			c6 = c-1
			button = Button(self.frame1, text=str(self.board[r6][c6]), width = 6, height = 3, command=partial(self.greyout, r6, c6))
			button.grid(row=r6+1, column=c6+1)

			r7 = r
			c7 = c-1
			button = Button(self.frame1, text=str(self.board[r7][c7]), width = 6, height = 3, command=partial(self.greyout, r7, c7))
			button.grid(row=r7+1, column=c7+1)

		#top left
		if r==0 and c==3:
	
			r1 = r+1
			c1 = c
			button = Button(self.frame1, text=str(self.board[r1][c1]), width = 6, height = 3, command=partial(self.greyout, r1, c1))
			button.grid(row=r1+1, column=c1+1)

			r7 = r
			c7 = c-1
			button = Button(self.frame1, text=str(self.board[r7][c7]), width = 6, height = 3, command=partial(self.greyout, r7, c7))
			button.grid(row=r7+1, column=c7+1)

			r8 = r+1
			c8 = c-1
			button = Button(self.frame1, text=str(self.board[r8][c8]), width = 6, height = 3, command=partial(self.greyout, r8, c8))
			button.grid(row=r8+1, column=c8+1)
		


	def clearword(self):
		self.wordnow=''
		currentword1 = Label(self.frame1, text="Word:", width = 4, height = 2)
		currentword1.grid(row=3, column = 5, rowspan=2)
		currentword = Label(self.frame1, text= self.wordnow, width = 20, height = 2)
		currentword.grid(row=3, column=6, rowspan=2)
		self.board_create()
		
	def entercheck(self):
		if self.wordnow in self.completed_words:
			self.clearword()
		else:
			if len(self.wordnow) <= 4 and len(self.wordnow) > 2:
				self.score+=1
			elif len(self.wordnow) <= 5 and len(self.wordnow) > 2:
				self.score+=2
			elif len(self.wordnow) <= 6 and len(self.wordnow) > 2:
				self.score+=3
			elif len(self.wordnow) <= 7 and len(self.wordnow) > 2:
				self.score+=5
			elif len(self.wordnow) >= 8:
				self.score+=11
			scoreboard = Label(self.frame1, text='Score: '+ str(self.score),  width = 6, height = 3)
			scoreboard.grid(row=5, columns=5, rowspan=4)
		self.completed_words.append(self.wordnow)
		self.clearword()

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
	def destroy(self):
		root.destroy()




