
import tkinter as tk

import constants as c
import random
import gameSelector

#this section of code is expaned in previous sections, simply it communicates withe main file and makes the basics for the game
#   to connect with the rest of the application
class Page(tk.Frame):

    #this initilaised the page and the class, as done in all preivous 
    #   pages and frames
    def __init__(self, parent, controller ):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid()
        self.main_grid =  tk.Frame(
            self, bg=c.BACKGROUND_COLOUR_BEHIND_FRAME, bd=3, width=600, height=600,
        )

# #''   #sets the background of the frame and makes the frame able to maximise
        #   and center properly
        self.background = tk.Frame(self.main_grid)
        self.background.grid(row=1, column=0,sticky="nsew")
        self.background.configure(bg=c.BACKGROUND_COLOUR_BEHIND_FRAME)

        gameSlectorFrame = tk.Frame(self.background)
        gameSlectorFrame.grid(row=0, column=0)
        gameSlectorFrame.configure(bg=c.BACKGROUND_COLOUR_BEHIND_FRAME)
        self.configure(bg=c.BACKGROUND_COLOUR_BEHIND_FRAME)

        backbtn = tk.Button(self, text='Back to selector', command=lambda: [self.controller.show_frame(gameSelector.Page)])
        backbtn.grid(row=0, column=0)

#''     
        #this binds the Up, Down, Left and Right commands to their respective keys
        self.main_grid.bind("<Up>", self.up)
        self.main_grid.bind("<Down>", self.down)
        self.main_grid.bind("<Left>", self.left)
        self.main_grid.bind("<Right>", self.right)
        self.main_grid.focus_set()

        #this places the grid using .place() so that other elements can be added with
        #   respect to the screen
        self.main_grid.place(relx=0, rely = 0.2)

        #start functions that run the game
        self.make_GUI()
        self.start_game()

        #buttons on screen are defined here, it is a way of playing the game on a
        #   touchscreen or if you do not have a set of arrow keys on your keyboard
        btn = tk.Button(self, text='UP', command=lambda: self.up(None))
        btn.place(relx=0.3,rely=0)

        btn = tk.Button(self, text='DOWN', command=lambda: self.down(None))
        btn.place(relx=0.3,rely=0.1)

        btn = tk.Button(self, text='LEFT', command=lambda: self.left(None))
        btn.place(relx=0.2,rely=0.1)

        btn = tk.Button(self, text='RIGHT', command=lambda: self.right(None))
        btn.place(relx=0.4,rely=0.1)


    # this function is run at the start, defines the grid and its characteristics
    def make_GUI(self):

        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                    width=150,
                    height=150
                )
                #each cell has the same spacing, width and height. they are also all coordinated in colour
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                cell_number.grid(row=i, column=j)
                cell_data = {"frame": cell_frame , "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)

        # make score header
        score_frame = tk.Frame(self)
        score_frame.place(relx=0.5,rely=0)
        tk.Label(
            score_frame,
            text="Score",
            font=c.FONT_SECONDARY
        ).grid(row=0)

        #score label set to "0" at the start
        self.scorelabel = tk.Label(score_frame, text="0", font=c.FONT_SECONDARY,)
        self.scorelabel.grid(row=1)



    def start_game (self):
        # create matrix of zeroes
        self.matrix = [[0] * 4 for _ in range(4)]
        # fill 2 random cells with 2s
        #starts the game with either a 2 or a 4 tile
        #randomizing the cell value
        row = random.randint (0, 3)
        col = random.randint(0, 3)
        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg=c.CELL_COLORS[2])
        self.cells[row][col]["number"].configure(
            bg=c.CELL_COLORS[2],
            fg=c.CELL_NUMBER_COLORS[2],
            font=c.CELL_NUMBER_FONTS[2],
            text="2"
        )
        #starts the game with either a 2 or a 4 tile
        while(self.matrix[row][col] != 0):
            #randomizing the cell value
            col =random.randint(0, 3)
            row =random.randint(0, 3)
        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg=c.CELL_COLORS[2])
        self.cells[row][col]["number"].configure(
            bg=c.CELL_COLORS[2],
            fg=c.CELL_NUMBER_COLORS[2],
            font=c.CELL_NUMBER_FONTS[2],
            text="2"
        )
        self.score =0
                           



    #these functions define how the grid is manipulated in order
    #    to merge sucessfully

    #most basic merge for left
    def stack(self):
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            fill_position = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position += 1
        self.matrix = new_matrix

    #merge of the tiles
    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]

    # flips the grid left to right for right merges
    def reverse(self):
        new_matrix = []
        for i in range (4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3 - j])
        self.matrix = new_matrix

    #vertically flips the grid 
    def transpose(self):
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]
        self.matrix = new_matrix





    #function that adds a new tile
    def add_new_tile(self):
        empty = [(i, j) for i in range(4) for j in range(4) if self.matrix[i][j] == 0]
        if not empty:
            return
        row, col = random.choice(empty)
        self.matrix[row][col] = random.choice([2, 4])

    #updates the GUI after merges take place
    def update_GUI(self):
        #cycle through every cell by using a for loop
        for i in range (4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.cells[i][j]["number"].configure(bg=c.BACKGROUND_COLOR_CELL_EMPTY, text="")
                #update the cells with their value
                else:
                    self.cells[i][j]["frame"].configure(bg=c.BACKGROUND_COLOR_DICT[cell_value])
                    self.cells[i][j]["number"].configure(
                        bg=c.BACKGROUND_COLOR_DICT[cell_value],
                        fg=c.CELL_COLOR_DICT[cell_value],
                        font=c.CELL_NUMBER_FONTS[cell_value],
                        text=str(cell_value)
                    )
        #updating the score
        self.scorelabel.configure(text=self.score)
        self.update_idletasks()

# these functions define the order in which functions are run
#   when initated, they run in the reverse order they are called 
#   so they go back to their original form

    #left is the most simple merge
    def left(self, event):
        self.stack()
        self.combine()
        self.stack()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    #you reverse the grid from right to left
    #   and then you follow the same procedure
    #   as left merge
    def right(self, event):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    #you vertically flip the grid and then
    #   follow the left merger
    def up(self, event):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    #this is the most complicated merge, you
    #   flip the grid vertically and then you
    #   reverse it, then you can follow the left
    #   merge.
    def down(self, event):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    #checks to see if horizonatal moves exist, determines if the game ends
    def horizontal_move_exists(self):
        for i in range (4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j + 1]:
                    return True
        return False

    #checks to see if vertical moves exist, determines if the game ends
    def vertical_move_exists(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i + 1][j]:
                    return True
        return False

    #what happens when the game is finished, win or loss 
    def game_over(self):
        if any(2048 in row for row in self.matrix):
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(    
                game_over_frame,
                text="You win!",
                bg=c.WINNER_BG,
                fg=c.GAME_OVER_FONT_COLOUR,
                font=c.FONT_SECONDARY
            ).pack()
            #opens a file that stores the highscores under their username
            try:
                name = getattr(self.controller, "username", "Player")
                with open("Highscore.txt", "a") as highscore:
                    highscore.write(f"\nName: {name}\nScore: {int(self.score)}\n")
            except OSError:
                pass
        
        #if the user does not get the 2048 tile then this code is run
        #checking if any moves exist
        elif not any (0 in row for row in self.matrix) and not self.horizontal_move_exists() and not self.vertical_move_exists():
            #creating a game over frame
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(    
                game_over_frame,
                text="Game Over",
                bg=c.LOSER_BG,
                fg=c.GAME_OVER_FONT_COLOUR,
                font=c.FONT_SECONDARY
            ).pack()
            #opens a file that stores the highscores under their username
            try:
                name = getattr(self.controller, "username", "Player")
                with open("Highscore.txt", "a") as highscore:
                    highscore.write(f"\nName: {name}\nScore: {int(self.score)}\n")
            except OSError:
                pass