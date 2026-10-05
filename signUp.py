
import tkinter as tk
import accountSelector
import constants as c
import mySQL
import login
#!########################################################################

LargeFont = ('Verdana', 12)

class Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.window = tk.Frame(self,bg= c.BACKGROUND_COLOR_GAME)
        self.window.pack()
        #fill = "both", expand = True

        #//responsible for filling the backdrop of the frame
        self.signupFrame = tk.Frame(self.window)
        self.signupFrame.grid(row=1, column=0,sticky="nsew")
        self.signupFrame.configure(bg=c.BACKGROUND_COLOUR_BEHIND_FRAME)

        signup_frame = tk.Frame(self.signupFrame)
        signup_frame.grid(row=0, column=0)
        signup_frame.configure(bg=c.BACKGROUND_COLOUR_BEHIND_FRAME)
        self.configure(bg=c.BACKGROUND_COLOUR_BEHIND_FRAME)
        #//

        signupLabel = tk.Label(self.window, text = 'Sign-Up Page', bg = c.BACKGROUND_COLOR_GAME)
        signupLabel.grid(row=0,column=1)

        accountSelectorButton = tk.Button(self.window, text='Back', command=lambda:self.controller.show_frame(accountSelector.Page))
        accountSelectorButton.grid(row=0, column=0, padx=10, pady=10)
       
       #//1. creating the frame for the buttons 
        self.signupFrame = tk.Frame(self.window, bg=c.BACKGROUND_COLOR_CELL_EMPTY)
        self.signupFrame.grid(row=2, column=0, columnspan = 4, padx=20, pady=20)

        #<username button is created and addressed here> row 3
        usernameLabel = tk.Label(self.signupFrame, text = 'Username')
        usernameLabel.grid(row=3,column=0, sticky = 'W' , padx=10, pady=10)

        self.usernameEntry = tk.Entry(self.signupFrame)
        self.usernameEntry.grid(row=4,column=0, padx=10, pady=10)

        #<password entry button is created and addressed here>
        passwordLabel = tk.Label(self.signupFrame, text = 'Password')
        passwordLabel.grid(row=6,column=0, sticky = 'W' , padx=10, pady=10)

        self.passwordEntry = tk.Entry(self.signupFrame)
        self.passwordEntry.grid(row=7,column=0, padx=10, pady=10)

        #<password Re-entry button is created and addressed here>
        passwordCheckLabel = tk.Label(self.signupFrame, text = 'Re-enter Password')
        passwordCheckLabel.grid(row=9,column=0, sticky = 'W' , padx=10, pady=10)

        self.passwordCheckEntry = tk.Entry(self.signupFrame)
        self.passwordCheckEntry.grid(row=10,column=0, padx=10, pady=10)

        #<continue button is created and adderessed here>
        btn = tk.Button(self.signupFrame, text='Continue', command=lambda:[self.checkInputs(),])
        btn.grid(row=12, column=0, padx=10, pady=10)
        #// 1




    

    
    #checks the inputs against the database and displays login if correct
    def checkInputs(self):
        verified = False
        verified = mySQL.SignupDatabase(self, verified)
        if verified == True:
            self.controller.show_frame(login.Page)










        # self.passwordEntry = tk.Entry(self.signupFrame)
        # self.passwordEntry.grid(row=7,column=0, padx=10, pady=10)

        # passwordCheckLabel = tk.Label(self.signupFrame, text = 'Re-enter Password')
        # passwordCheckLabel.grid(row=9,column=0, sticky = 'W' , padx=10, pady=10)

        # self.passwordCheckEntry = tk.Entry(self.signupFrame)
        # self.passwordCheckEntry.grid(row=10,column=0, padx=10, pady=10)





    # def checkInputs(self):
    #     if self.usernameeEntry.get() == 'uday':
    #         self.controller.show_frame(game.Page)
    #     else:
    #         lbl = tk.Label(self.loginFrame, text = 'That is not a real username!', fg='red')
    #         lbl.grid(row=3,column=0, padx=10, pady=10)