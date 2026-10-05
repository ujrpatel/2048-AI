import tkinter as tk
import constants as c
import gameGui
import selfPlay

#backend,  a class allows functions to run simultaneously
#        all the code is explained in design throughly 
class Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.window = tk.Frame(self,bg = c.BACKGROUND_COLOR_GAME_SECONDARY)
        self.window.pack()

#sets the backgrond and centers the frame
#//
        self.selectorFrame = tk.Frame(self.window)
        self.selectorFrame.grid(row=1, column=0,sticky="nsew")
        self.selectorFrame.configure(bg=c.BACKGROUND_COLOR_CELL_EMPTY)

        selection_frame = tk.Frame(self.selectorFrame)
        selection_frame.grid(row=0, column=0)
        selection_frame.configure(bg=c.BACKGROUND_COLOR_GAME)
        self.configure(bg=c.BACKGROUND_COLOR_GAME)
#//
         #crestes a frame within a frame
        self.selectorFrame = tk.Frame(self.window)
        self.selectorFrame.grid(row=1, column=0,sticky="nsew")
        self.selectorFrame.configure(bg=c.BACKGROUND_COLOR_GAME_SECONDARY)

        #defining the Instruction
        Title_label = tk.Label(self.window, text = 'Please select one of the options from below!', bg = c.BACKGROUND_COLOR_GAME)
        Title_label.grid(row=0, column=0)

        #buttons that redirect the user to selected page
        Login_button = tk.Button(self.window, text='AI', command=lambda:self.controller.show_frame(gameGui.Page))
        Login_button.grid(row=4, column=0, padx=10, pady=10,)

        Signup_button = tk.Button(self.window, text='Self play', command=lambda:self.controller.show_frame(selfPlay.Page))
        Signup_button.grid(row=6, column=0, padx=10, pady=10,)