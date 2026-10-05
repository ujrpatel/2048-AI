import tkinter as tk
import mysql.connector
import constants as c
from datetime import datetime
from tkinter import *
# from cryptography.fernet import Fernet
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()


#database connection
mydb = mysql.connector.connect(
    host ="localhost",
    user="root",
    passwd="root",
    database = "2048Logins"
    )

mycursor = mydb.cursor()

# fernet = Fernet(key)

#function to put queries into a list
def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item
        return str

#database is run when called
def loginDatabase(self,verified):
    
    #lables that link to the login page error lables
    self.usernameEntrylbl = tk.Label(self.loginFrame, text = '', fg='red', bg=c.BACKGROUND_COLOR_GAME_SECONDARY)
    self.usernameEntrylbl.grid(row=2,column=0, padx=10, pady=10)

    self.passEntrylbl = tk.Label(self.loginFrame, text = '', fg='red', bg=c.BACKGROUND_COLOR_GAME_SECONDARY)
    self.passEntrylbl.grid(row=5,column=0, padx=10, pady=10)


    #validaiton for Login
    if self.usernameEntry.get() == '' or self.passwordEntry.get() == '' or (len(self.usernameEntry.get())) >= 16 or (len(self.passwordEntry.get())) >16:

        #If username or password is empty
        if self.usernameEntry.get() == '':
            self.usernameEntrylbl.config(text= 'Please enter Username!',)
            verified = False
            print("username field empty")
            pass

        if self.passwordEntry.get() == '':
            self.passEntrylbl.config(text= 'Please enter Password!',)
            verified = False
            print("password field empty")
            pass

        #if username or password exceed length
        if len(self.usernameEntry.get()) >= 16:
            self.usernameEntrylbl.config(text= 'Username length Exceeded',)
            verified = False
            print("Username length Exceeded")
            pass

        if len(self.passwordEntry.get()) >16:
            self.passEntrylbl.config(text= 'Password Length Exceeded',)
            verified = False
            print("Password length Exceeded")
            pass
        
        # #if username or password are too short
        # if len(self.usernameEntry.get()) <= 5:
        #     self.usernameEntrylbl.config(text= 'Username length too short',)
        #     verified = False
        #     print("Username length too short")
        #     pass

        # if len(self.passwordEntry.get()) <=5:
        #     self.passEntrylbl.config(text= 'Password Length too short',)
        #     verified = False
        #     print("Password Length too short")
        #     pass

        return verified
        

    #if validaiton is passed
    else:
        

        #select column username from database then print 
        mycursor.execute("SELECT username FROM userLogin")
        currentUsers = mycursor.fetchall()
        print("existins users",currentUsers)

        #puts the usernames that are queried into a simple string
        usernameInList = []
        for x in currentUsers:
            y = convertTuple(x)
            usernameInList.append(y)
            print(usernameInList)

        
        #check if username is in the list /exists
        if self.usernameEntry.get() in usernameInList:

            usernameSearch = str(self.usernameEntry.get())

            #get the password associcated with the username 
            mycursor.execute("SELECT password FROM userLogin WHERE username = ('%s')" % (usernameSearch))
            passwordSearch = mycursor.fetchall()

            typed = self.passwordEntry.get()
            verified = False
            if passwordSearch and passwordSearch[0][0] is not None:
                stored = passwordSearch[0][0]
                # old accounts: password saved as plain text
                if isinstance(stored, str) and stored == typed:
                    verified = True
                else:
                    token = stored if isinstance(stored, (bytes, bytearray)) else str(stored).encode()
                    try:
                        verified = fernet.decrypt(token).decode() == typed
                    except Exception:
                        verified = False
                verified = True
            
            #if password is not in list
            if verified:
                pass
            else:
                print("password failed")
                self.passEntrylbl.config(text= 'Username or Password incorrect',)
                self.usernameEntrylbl.config(text= 'Username or Password incorrect',)
                verified = False
        
        #if the username is not in the list
        else:
            self.usernameEntrylbl.config(text = '      Username not in list!        ',)
            verified = False
    
    return verified



#// ADMIN PURPOSES



    # mycursor.execute("DELETE FROM UserLogin")
    # mycursor.execute("DESCRIBE UserLogin")
    # mycursor.execute("SELECT * FROM UserLogin")
    # for x in mycursor:
    #     print(x)




#// ADMIN PURPOSE ENDS



#the function is run when called
def SignupDatabase(self,verified):

    #lables that link to the Signup page
    userlbl = tk.Label(self.signupFrame, text = '', fg='red',bg=c.BACKGROUND_COLOR_GAME_SECONDARY)
    userlbl.grid(row=5,column=0, padx=10, pady=10)

    Passlbl = tk.Label(self.signupFrame, text = '', fg='red',bg=c.BACKGROUND_COLOR_GAME_SECONDARY)
    Passlbl.grid(row=8,column=0, padx=10, pady=10)

    ReenterPasslbl = tk.Label(self.signupFrame, text = '', fg='red',bg=c.BACKGROUND_COLOR_GAME_SECONDARY)
    ReenterPasslbl.grid(row=11,column=0, padx=10, pady=10)

    #validation for the password, this is the same as login
    if self.usernameEntry.get() == '' or self.passwordEntry.get() == '' or self.passwordCheckEntry.get() == '' or (len(self.usernameEntry.get())) >= 16 or (len(self.passwordEntry.get())) >16 or len(self.passwordCheckEntry.get()) >16 or (self.passwordEntry.get() != self.passwordCheckEntry.get()):
        
        #if the username field is empty
        if self.usernameEntry.get() == '':
            userlbl.config(text= 'Please enter Username!',)
            print("username field empty")
            verified = False
            pass

        #if the password password field is empty
        if self.passwordEntry.get() == '':
            Passlbl.config(text= 'Please enter Password!',)
            print("password field empty")
            verified = False
            pass
        
        #if the reenter password field is empty
        if self.passwordCheckEntry.get() == '':
            ReenterPasslbl.config(text= 'Please re-enter Password!',)
            print("re enter password field empty")

        #check to see if the both passwords match
        if self.passwordEntry.get() != self.passwordCheckEntry.get():
            Passlbl.config(text= 'Passwords Do Not Match',)
            ReenterPasslbl.config(text= 'Passwords Do Not Match',)
            print("passwords dont match")
        else:
            
            #if the passwords match, username/password/reenter password are checked to see if they excced limits
            if len(self.usernameEntry.get()) >= 16:
                userlbl.config(text= 'Username length Exceeded',)
                print("username length exceeded")
                verified = False
                pass    
            
            #checks password entry length
            if len(self.passwordEntry.get()) >16:
                Passlbl.config(text= 'Password Length Exceeded',)
                print(" password length exceeded")
                verified = False
                pass
            
            #checks password check entry length
            if len(self.passwordCheckEntry.get()) >16:
                ReenterPasslbl.config(text= 'Password Length Exceeded',)
                print("re enter password length exceeded")
                verified = False
                pass
            
            #checks username length too see if its too short
            if len(self.usernameEntry.get()) <= 5:
                userlbl.config(text= 'Username length too short',)
                verified = False
                print("Username length too short")
                pass
            
            #checks password length if it is too short
            if len(self.passwordEntry.get()) <=5:
                Passlbl.config(text= 'Password Length too short',)
                verified = False
                print("Password Length too short")

            return verified
        

    else:
        
        if self.passwordEntry.get() != self.passwordCheckEntry.get():
            Passlbl.config(text='Check Passwords')
            ReenterPasslbl.config(text='Check Passwords')
            verified = False
            return verified

        else:
            
            #queris for all usernames in the list currently
            mycursor.execute("SELECT username FROM userLogin")
            currentUsers = mycursor.fetchall()

            #gets the usernames into an organised list
            userExists = [row[0] for row in currentUsers]

            #this checks to see if the username already exists in the database
            if self.usernameEntry.get() in userExists:
                print(currentUsers,"\n#########")
                print(userExists)
                userlbl.config(text= 'Username Exists!')
                print("username exists in database")
                verified = False

                return verified
            
            #if the username is valid and does not exist
            else:

                #the username is put into the database, with the password and the current time

                mycursor.execute("INSERT INTO UserLogin (username, password, timeCreated) VALUES (%s,%s,%s)",(self.usernameEntry.get(),self.passwordEntry.get(),datetime.now()))
                mydb.commit()
                print("done")

                #this is what lets the checkinput() function know if signup has finished
                verified = True
                return verified







#______________________________________________________________




# mycursor.execute("CREATE DATABASE 2048Logins")

# mycursor.execute("CREATE TABLE UserLogin ( userID int PRIMARY KEY AUTO_INCREMENT, username VARCHAR(20), password VARCHAR(20) , timeCreated datetime NOT NULL)")

# mycursor.execute("DESCRIBE UserLogin")

# mycursor.execute("INSERT INTO UserLogin (username, password, timeCreated) VALUES (%s,%s,%s)",("Uday","a",datetime.now()))

# mydb.commit()

# mycursor.execute("SELECT * FROM UserLogin")

# mycursor.execute("SELCT * FROM UserLogin WHERE username = '' ORDER BY userID ASC")

# for x in mycursor:
#     print(x)










# def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)

# def loginDatabase(self,verified):
#     if self.usernameEntry.get() == '':
        
#         lbl = tk.Label(self.loginFrame, text = 'That is not a real username!', fg='red')
#         lbl.grid(row=2,column=0, padx=10, pady=10)
    
#     if self.passwordEntry.get() == '':

#         lbl = tk.Label(self.loginFrame, text = 'That is not a real Password!', fg='red')
#         lbl.grid(row=5,column=0, padx=10, pady=10)

#     else:

#         print(self.usernameEntry.get())
#         print(self.passwordEntry.get())
#         verified = True

#     return verified







# print(self.usernameEntry.get())
# print(self.passwordEntry.get())













# mycursor.execute("CREATE TABLE UserLogin ( username VARCHAR(20), password VARCHAR(20))")
# mydb.commit()

