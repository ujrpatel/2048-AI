import tkinter as tk
from tkinter import *
import constants as c
from tkinter import Frame, Label, CENTER
from random import randint
import time
import gameSelector
import gameboard
from aiAlgorithm import AI


SIZE = 150
GRID_LEN = 4
GRID_PADDING = 8

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOR_DICT = {   2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", \
                            32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", \
                            512:"#edc850", 1024:"#edc53f", 2048:"#edc22e" }
CELL_COLOR_DICT = { 2:"#776e65", 4:"#776e65", 8:"#f9f6f2", 16:"#f9f6f2", \
                    32:"#f9f6f2", 64:"#f9f6f2", 128:"#f9f6f2", 256:"#f9f6f2", \
                    512:"#f9f6f2", 1024:"#f9f6f2", 2048:"#f9f6f2" }
FONT = ("Verdana", 40, "bold")


#this section of code is expaned in previous sections, simply it communicates withe main file and makes the basics for the game
#   to connect with the rest of the application
class Page(tk.Frame):

    #this initilaised the page and the class, as done in all preivous 
    #   pages and frames
    def __init__(self, parent, controller, ):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid_cells = []
        self.window = tk.Frame(self,bg= c.BACKGROUND_COLOR_GAME)
        self.window.pack()
        self.AI = AI()

        #sets the background of the frame and makes the frame able to maximise
        #   and center properly
        #''''
        self.background = tk.Frame(self.window)
        self.background.grid(row=1, column=0,sticky="nsew")
        self.background.configure(bg=c.BACKGROUND_COLOUR_BEHIND_FRAME)

        gameSlectorFrame = tk.Frame(self.background)
        gameSlectorFrame.grid(row=0, column=0)
        gameSlectorFrame.configure(bg=c.BACKGROUND_COLOUR_BEHIND_FRAME)
        self.configure(bg=c.BACKGROUND_COLOUR_BEHIND_FRAME)
        #''''

        #initailses buttons and and their desginated functions
        self.startBtn = True
        self.btn = tk.Button(self.window, text='Start', fg="red", command=lambda: self.startGame())
        self.btn.grid(row=1,column=0)

        #clauses that affect the running of the game
        self.aiRunning = True
        self.endEvent = False
        #back to selector button
        backbtn = tk.Button(self.window, text='Back to selector', command=lambda: [self.controller.show_frame(gameSelector.Page), self.stopGame()])
        backbtn.grid(row=2,column=0)
        #pause button
        Pausebtn = tk.Button(self.window, text='Pause', command=lambda: [self.pause()])
        Pausebtn.grid(row=3,column=0)






        #defining the AI move frame 
        self.logFrame = tk.LabelFrame(self.window, text='AI Moves', font= c.FONT, bg=c.BACKGROUND_COLOR_GAME,)
        self.logFrame.grid(row=1, column=1)
        #creating lavel in the AI move frame
        self.movelabel = tk.Label(self.logFrame, text='', bg=c.BACKGROUND_COLOR_GAME)
        self.movelabel.grid(row=1, column=1, )

        #defining score frame
        self.scoreFrame = tk.LabelFrame(self.window, text='Score', font= c.FONT, bg=c.BACKGROUND_COLOR_GAME,)
        self.scoreFrame.grid(row=1, column=2)
        #creating label in score frame
        self.scorelabel = tk.Label(self.scoreFrame, text='', bg=c.BACKGROUND_COLOR_GAME)
        self.scorelabel.grid(row=1, column=1)

        #defining total move frame
        self.totalmovesframe = tk.LabelFrame(self.window, text='Total moves', font= c.FONT, bg=c.BACKGROUND_COLOR_GAME,)
        self.totalmovesframe.grid(row=2, column=1, columnspan= 3)

        #creating labels inside of the total move frame, for up, down, left, right
        self.totalmovesuplabel = tk.Label(self.totalmovesframe, text='', bg=c.BACKGROUND_COLOR_GAME)
        self.totalmovesuplabel.grid(row=1, column=1)

        self.totalmovesdownlabel = tk.Label(self.totalmovesframe, text='', bg=c.BACKGROUND_COLOR_GAME)
        self.totalmovesdownlabel.grid(row=1, column=2)

        self.totalmovesleftlabel = tk.Label(self.totalmovesframe, text='', bg=c.BACKGROUND_COLOR_GAME)
        self.totalmovesleftlabel.grid(row=1, column=3)

        self.totalmovesrightlabel = tk.Label(self.totalmovesframe, text='', bg=c.BACKGROUND_COLOR_GAME)
        self.totalmovesrightlabel.grid(row=1, column=4)

    #defines what the pause button does
    def pause(self):
        self.aiRunning = False
        self.cont = True

    #defiens what disable button does
    def disableBtn(self):
        self.btn.config(state='disabled')
        self.startBtn=False
    
    #defines what enable button does
    def enableBtn(self):
        self.btn.config(state='active')
        self.startBtn=True
        
    #defines what stopgame does
    def stopGame(self):
        self.aiRunning = False
        self.startBtn = False
        print("ai stopped")
        self.moveup = 0
        self.movedown = 0
        self.moveright = 0
        self.moveleft = 0

    #defiens what start game does
    def startGame(self):
        self.aiRunning = True
        self.grid_cells = []

        if self.startBtn == True:
            self.disableBtn()
            self.init_grid()
            self.init_matrix()
            self.update_grid_cells()

            self.run_game()

        #if start button is false then the game has been exited midgame
        #   the game has to destroy the previous instance of the grid
        #   inorder to make a new game run
        if self.startBtn == False:

            #renables the button so that it can be pressed
            self.enableBtn()

            #destroys the background which holds the grid
            self.background.destroy()
            self.scoreupdate = 0

            #reseting the counters
            self.moveup = 0
            self.movedown = 0
            self.moveright = 0
            self.moveleft = 0

            #updating the labels with new scores
            self.scorelabel.config(text=f'Score : {self.scoreupdate}')

            self.move = ''
            self.movelabel.config( text=f'Move: {self.move}',anchor = "center")



    #this what happens when the start button is pressed and the game is run
    def run_game(self):
        self.scoreupdate = 0
        self.moveup = 0
        self.movedown = 0
        self.moveright = 0
        self.moveleft = 0
        self.totalmoves = 0
        while self.aiRunning == True :

            # gets the available moves from the existing grid and moves it accordingly
            self.move = self.AI.get_move(self.board)
            self.board.move(self.move)
            self.update_grid_cells()

            #adds new tile 
            pos, newvalue = self.add_random_tile()

            #updates the grid 
            self.update_grid_cells()

            #defines what happens if the game runs out of moves, runs game over display
            if len(self.board.get_available_moves()) == 0:
                self.game_over_display()
                break

            #this chnages the score of the game and does AI move and the Tally feature
            if self.move == 0:
                self.move = "UP"
                self.moveup = self.moveup + 1
                self.totalmoves = self.totalmoves + 1
                self.totalmovesuplabel.config(text = f'Up: {self.moveup}', bg=c.BACKGROUND_COLOR_GAME, font= c.FONT_SECONDARY)

            elif self.move == 1:
                self.move = "DOWN"
                self.movedown = self.movedown + 1
                self.totalmoves = self.totalmoves + 1
                self.totalmovesdownlabel.config(text = f'Down: {self.movedown}', bg=c.BACKGROUND_COLOR_GAME, font= c.FONT_SECONDARY)

            elif self.move == 2:
                self.move = "LEFT"
                self.moveleft = self.moveleft + 1
                self.totalmoves = self.totalmoves + 1
                self.totalmovesleftlabel.config(text = f'Left: {self.moveleft}', bg=c.BACKGROUND_COLOR_GAME, font= c.FONT_SECONDARY)

            else:
                self.move = "RIGHT"
                self.moveright = self.moveright + 1
                self.totalmoves = self.totalmoves + 1
                self.totalmovesrightlabel.config(text = f'Right: {self.moveright}', bg=c.BACKGROUND_COLOR_GAME, font= c.FONT_SECONDARY)

            # this is what updats the score
            self.movelabel.config(text = f'Move: {self.move}', bg=c.BACKGROUND_COLOR_GAME, font= c.FONT_SECONDARY)
            self.scoreupdate = int(self.scoreupdate) +  int(newvalue)
            self.scorelabel.config(text = f'Score : {self.scoreupdate}', bg=c.BACKGROUND_COLOR_GAME, font= c.FONT_SECONDARY)
            self.update()

            # self.movelabel.config(text=f'Move: {self.move}',bg=c.BACKGROUND_COLOR_GAME,font= c.FONT_SECONDARY)
            # self.scoreupdate = int(self.scoreupdate) +  int(newvalue)
            # self.scorelabel.config(text=f'Score : {self.scoreupdate}')
    
    # a function that is run when the game has finished
    def game_over_display(self):

        #sets every cell to the default colour
        for i in range(4):
            for j in range(4):
                self.grid_cells[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
        self.startBtn = True
        #this section of the code colours the top tiles as the 2048 tile colour and cethers them
        self.grid_cells[1][1].configure(text="TOP",bg=BACKGROUND_COLOR_CELL_EMPTY)
        self.grid_cells[1][2].configure(text="4 TILES:",bg=BACKGROUND_COLOR_CELL_EMPTY)
        top_4 = list(map(int, reversed(sorted(list(self.board.grid.flatten())))))
        self.grid_cells[2][0].configure(text=str(top_4[0]), bg=BACKGROUND_COLOR_DICT[2048], fg=CELL_COLOR_DICT[2048])
        self.grid_cells[2][1].configure(text=str(top_4[1]), bg=BACKGROUND_COLOR_DICT[2048], fg=CELL_COLOR_DICT[2048])
        self.grid_cells[2][2].configure(text=str(top_4[2]), bg=BACKGROUND_COLOR_DICT[2048], fg=CELL_COLOR_DICT[2048])
        self.grid_cells[2][3].configure(text=str(top_4[3]), bg=BACKGROUND_COLOR_DICT[2048], fg=CELL_COLOR_DICT[2048])
        #one last update so the top tiles can be replaced
        self.update()

    # this function is run at the start, defines the grid and its characteristics
    def init_grid(self):
        self.background = Frame(self.window, bg=BACKGROUND_COLOR_GAME, width=SIZE, height=SIZE)
        self.background.grid(row=5, column=0, columnspan=3)

        #sets the background of the frame and makes the frame able to maximise
        #   and center properly
        #??
        self.background = tk.Frame(self.background)
        self.background.grid(row=1, column=0,sticky="nsew")
        self.background.configure(bg=c.BACKGROUND_COLOUR_BEHIND_FRAME)

        background = tk.Frame(self.background)
        background.grid(row=0, column=0)
        background.configure(bg=c.BACKGROUND_COLOUR_BEHIND_FRAME)
        self.configure(bg=c.BACKGROUND_COLOUR_BEHIND_FRAME)
        #??

        #creates all the cells and their characteristics
        for i in range(GRID_LEN):
            grid_row = []

            for j in range(GRID_LEN):
                #each cell has the same spacing, width and height. they are also all coordinated in colour
                cell = Frame(self.background, bg=BACKGROUND_COLOR_CELL_EMPTY, width=SIZE/GRID_LEN, height=SIZE/GRID_LEN,)
                cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
                t = Label(master=cell, text="", bg=BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=FONT, width=4, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    #genteration of where the new tile can spawn
    def gen(self):
        return randint(0, GRID_LEN - 1)

    # initilaes matrix that contains the gameboard and the grid within it
    def init_matrix(self):
        self.board = gameboard.GameBoard()
        self.add_random_tile()
        self.add_random_tile()

    # updates all the cells in the grid, run after merges take place or new tiles spawn
    def update_grid_cells(self):
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                new_number = int(self.board.grid[i][j])
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    n = new_number
                    if new_number > 2048:
                        c = 2048
                    else:
                        c = new_number

                    self.grid_cells[i][j].configure(text=str(n), bg=BACKGROUND_COLOR_DICT[c], fg=CELL_COLOR_DICT[c])
        self.update_idletasks()
        
        
    # controls what tile spawns and the probality of each
    def add_random_tile(self):
        if randint(0,99) < 100 * 0.9:
            value = 2
        else:
            value = 4

        #gets all avalible cells form thre grid
        cells = self.board.get_available_cells()
        pos = cells[randint(0, len(cells) - 1)] if cells else None

        if pos is None:
            value = 0
            return pos, value
        #inserts the tile
        else:
            self.board.insert_tile(pos, value)
            xvalue= value
            return pos, xvalue
