
# Boggle
### Plan

#### description:
Revant and Will's Boggle class is a project with the objective of practicing classes and functions in a functioning game. 

helpful links: 
[Boggle Rules!](http://www.fun-with-words.com/play_boggle.html)
[classes in python!](https://docs.python.org/3/tutorial/classes.html) 
[dice class help!](https://stackoverflow.com/questions/14409661/dice-generator-using-class-in-python)
[tk help!](https://docs.python.org/2/library/tk.html) 

### classes:

1. make a graphic interface class
2. make dice class 
3. main runner 
4. point score class 

#### class graphic interface:

def __init__(self,master):

self.master = master – creates a user window

master.title – a simple GUI (game user interface)

self.root = Tk() - setup for root window

self.board_rowcol=4 - Creates a 10x10 Minesweeper board

self.label = Label(master, text="Welcome to Boggle") – simple greeting interface that also establishes a place for text

self.label.pack()

self.frame1 = Frame(self.root, width = 30, height = 30) -Window size for tkinter window

self.frame1.grid() – makes the grid

self.makecoord() - Calls on function to make letter coordinates on board. 

self.display() -Creates grid of letters  

self.root.mainloop() – main function for the display of everything 
    
#### class point_score:
def _init_(self, word_count)

self.word_count = word_count

lettercount() – counts the number of letters in the word responses and assures that the words are more than two letters

pointreward() – depending on length of the word points are assigned with this function

wordcheck() – make sure that the word is able to be made on the board 

Checkcoord() -Check up down right left etc. to make sure letters are next to eachother 

Nodoubles() - Make sure the same letter isn’t used twice

#### class dice():  
def init (self, sides):
sides will be defined by 6 letters in the alphabet (using a 2d array for every die). 

Dice.placement() – assign random placements on the 4x4 board of all the dice

Dice.values() – randomized (or somewhat randomized for each dice (6 values for each dice) 


Main runner will call the classes and set the variables

_________________________________________________________________________________________________________________________

#### Who is working on what?
will:

* plan 
* readme 
* point score
* check 

Revant: 

* dice class 
* User interface class 
* main runner










