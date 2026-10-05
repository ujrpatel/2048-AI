import tkinter as tk
from tkinter import *

import login
import signUp
import selfPlay
import accountSelector
import gameSelector
import gameGui

# a class allows functions to run simultaneously
class App(tk.Tk):
 
    def __init__(self, *args, **kwargs):        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, '2048')
        
        #this sets characteristics for each and every frame, allowing each of them to fill the screen when expanded
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        #each frame that is displayed is to be added here, this allows us to swich between them
        for F in (login.Page, accountSelector.Page, signUp.Page,gameSelector.Page, gameGui.Page, selfPlay.Page ):

            frame = F(container, self)

            self.frames[F] = frame
            
            
            frame.grid(row = 0, column = 0, sticky = "nsew")

        #this is the first page that is shown everytime the code is run
        self.show_frame(accountSelector.Page)

    #this code brings the selected frame to the front of the stack, meaning we can view it.
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



app = App()
#app.resizable(False, False)

#adds a .ico image at the top of the window, visual feature


#this sets the minimum size of the application
app.minsize(670,795)
app.mainloop()