import tkinter as tk
import constants as c
import login
import signUp

# a class allows functions to run simultaneously
class Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.window = tk.Frame(self,bg = c.BACKGROUND_COLOR_GAME_SECONDARY)
        self.window.pack()

#//     this bit of the code fills the background with a colour and makes sure that the window
#               is centered and can expand correctly
#//     Responsible for filling the backdrop of the frame

        self.selectorFrame = tk.Frame(self.window)
        self.selectorFrame.grid(row=1, column=0,sticky="nsew")
        self.selectorFrame.configure(bg=c.BACKGROUND_COLOR_CELL_EMPTY)

        selection_frame = tk.Frame(self.selectorFrame)
        selection_frame.grid(row=0, column=0)
        selection_frame.configure(bg=c.BACKGROUND_COLOR_GAME)
        self.configure(bg=c.BACKGROUND_COLOR_GAME)
#//

        #this is a frame within a frame, lets me add labels inside
        self.selectorFrame = tk.Frame(self.window)
        self.selectorFrame.grid(row=1, column=0,sticky="nsew")
        self.selectorFrame.configure(bg=c.BACKGROUND_COLOR_GAME_SECONDARY)

        # an instruction label
        Title_label = tk.Label(self.window, text = 'Please select one of the options from below!', bg = c.BACKGROUND_COLOR_GAME)
        Title_label.grid(row=0, column=0)

        #the buttons link back to the main applicaiton, which changes the frame
        Login_button = tk.Button(self.window, text='Login', command=lambda:self.controller.show_frame(login.Page))
        Login_button.grid(row=4, column=0, padx=10, pady=10,)

        Signup_button = tk.Button(self.window, text='Sign-up', command=lambda:self.controller.show_frame(signUp.Page))
        Signup_button.grid(row=6, column=0, padx=10, pady=10,)