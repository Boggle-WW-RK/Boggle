
from main import dice

dice_roll = dice(Tk())
=======
from boggleclass import gui_board, dice, timer, scoring, end_game, check
import random
import sys
import numpy as py4
import time
from tkinter import *


#simple class calls. Nothing too complicated at all about the runner calss just runs the differnt classes in sequence
  x.gui_board() #set up the board originally set up display and titles 
  x.dice() #set up the dice on the board
  x.timer() #start the timer
  x.check() #check to make sure that the inputs are actually playable - this is done by restricting the letters you can click
  x.scoring() #score the inputs by using the len function
  x.end_game() #the end 

