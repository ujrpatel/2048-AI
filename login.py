# from cgi import test
import tkinter as tk
import gameGui
import accountSelector
import gameSelector
import constants as c
import mySQL
#!########################################################################



# a class allows functions to run simultaneously
class Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.window = tk.Frame(self,bg= c.BACKGROUND_COLOR_GAME)
        self.window.pack()
        #fill = "both", expand = True

        #//responsible for filling the backdrop of the frame
        self.loginFrame = tk.Frame(self.window)
        self.loginFrame.grid(row=1, column=0,sticky="nsew")
        self.loginFrame.configure(bg=c.BACKGROUND_COLOUR_BEHIND_FRAME)

        login_frame = tk.Frame(self.loginFrame)
        login_frame.grid(row=0, column=0)
        login_frame.configure(bg=c.BACKGROUND_COLOUR_BEHIND_FRAME)
        self.configure(bg=c.BACKGROUND_COLOUR_BEHIND_FRAME)
        #//

        lbl = tk.Label(self.window, text = 'Login Page', bg = c.BACKGROUND_COLOR_GAME)
        lbl.grid(row=0,column=1, padx=10, pady=10)

        btn = tk.Button(self.window, text='Back', command=lambda:self.controller.show_frame(accountSelector.Page))
        btn.grid(row=0, column=0, padx=10, pady=10)

       
       #//1. creating the frame for the buttons
        self.loginFrame = tk.Frame(self.window, bg=c.BACKGROUND_COLOR_CELL_EMPTY)
        self.loginFrame.grid(row=1, column=0, columnspan = 4, padx=20, pady=20)

        #<username button is created and addressed here>
        usernameLabel = tk.Label(self.loginFrame, text = 'Username')
        usernameLabel.grid(row=0,column=0, sticky = 'W' , padx=10, pady=10)

        self.usernameEntry = tk.Entry(self.loginFrame)
        self.usernameEntry.grid(row=1,column=0, padx=10, pady=10)

        #<password Re-entry button is created and addressed here>
        passwordLabel = tk.Label(self.loginFrame, text = 'Password')
        passwordLabel.grid(row=3,column=0, sticky = 'W' , padx=10, pady=10)

        self.passwordEntry = tk.Entry(self.loginFrame)
        self.passwordEntry.grid(row=4,column=0, padx=10, pady=10)

        #<continue button is created and adderessed here>
        btn = tk.Button(self.loginFrame, text='Continue', command=lambda:[self.checkInputs(),])
        btn.grid(row=9, column=0, padx=10, pady=10)
        #// 1

    
    def checkInputs(self):
        
        verified = False
        verified = mySQL.loginDatabase(self,verified)
        if verified == True:
            self.controller.username = self.usernameEntry.get()
            self.controller.show_frame(gameSelector.Page)
            print("login sucessful")
















    # def checkInputs(self):
    #     if self.usernameeEntry.get() == 'uday':
    #         self.controller.show_frame(game.Page)
    #     else:
    #         lbl = tk.Label(self.loginFrame, text = 'That is not a real username!', fg='red')
    #         lbl.grid(row=3,column=0, padx=10, pady=10)