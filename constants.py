
#general constants
SIZE = 400
GRID_LEN = 4
GRID_PADDING = 10


#basic colour scheme for the game
BACKGROUND_COLOR_GAME = "#92877d"  
BACKGROUND_COLOR_GAME_SECONDARY = "#9e948a"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"
BACKGROUND_COLOUR_BEHIND_FRAME = "#92877d" 

#background colour of the cell corresponding to the number
BACKGROUND_COLOR_DICT = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
                         16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
                         128: "#edcf72", 256: "#edcc61", 512: "#edc850",
                         1024: "#edc53f", 2048: "#edc22e",

                         4096: "#eee4da", 8192: "#edc22e", 16384: "#f2b179",
                         32768: "#f59563", 65536: "#f67c5f", }

#background of the cell of the number
CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
                   32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2",
                   256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2",
                   2048: "#f9f6f2",

                   4096: "#776e65", 8192: "#f9f6f2", 16384: "#776e65",
                   32768: "#776e65", 65536: "#f9f6f2", }


#standardised font and style defined
FONT = ("Clear Sans", 20,"bold")# you can also use verdana, 40 bold
FONT_SECONDARY = ("Clear Sans", 10,"bold")
CELL_NUMBER_FONTS = ("verdana", 10,"bold")

WINNER_BG = "#ffcc00"
LOSER_BG = "#a39489"
GAME_OVER_FONT_COLOUR = "#776e65"

#key strokes and functionality
KEY_UP_ALT = "\'\\uf700\'"
KEY_DOWN_ALT = "\'\\uf701\'"
KEY_LEFT_ALT = "\'\\uf702\'"
KEY_RIGHT_ALT = "\'\\uf703\'"

# WASD keys are assigned for additional compatibility
KEY_UP = "'w'"
KEY_DOWN = "'s'"
KEY_LEFT = "'a'"
KEY_RIGHT = "'d'"
KEY_BACK = "'b'"

#IJKL keys are assigned for additional compatibility
KEY_J = "'j'"
KEY_K = "'k'"
KEY_L = "'l'"
KEY_H = "'h'"

#seperate colour profiles for self play, intended to be changed quickly
CELL_NUMBER_FONTS = {
    2: ("verdana", 55, "bold"), 4: ("verdana", 55, "bold"), 8: ("verdana", 55, "bold"),
    16: ("verdana", 50, "bold"), 32: ("verdana", 50, "bold"), 64: ("verdana", 50, "bold"),
    128: ("verdana", 45, "bold"), 256: ("verdana", 45,"bold"), 512: ("verdana", 45, "bold"),
    1024: ("verdana", 40, "bold"),2048: ("verdana", 40, "bold")
    }

CELL_COLORS = {2: "#fcefe6", 4: "#f2e8cb", 8: "#f5b682", 16: "#f29446", 32: "#ff775c",
    64: "#e64c2e", 128: "#ede291", 256: "#fce130", 512: "#ffdb4a", 1024: "#fØb922", 2048: "#fad74d",
    }

CELL_NUMBER_COLORS = {2: "#695c57", 4: "#695c57", 8: "#ffffff", 16: "#ffffff", 32: "#ffffff",
    64: "#ffffff", 128: "#ffffff", 256: "#ffffff", 512: "#ffffff", 1024: "#ffffff", 2048: "#ffffff"
    }
