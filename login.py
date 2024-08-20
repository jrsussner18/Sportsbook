from tkinter import *
import csv
import gui

with open("loginInfo.csv", "r", encoding="utf-8") as file:
        read = csv.reader(file)
        usernames=next(read)
        passwords=next(read)

def checkLogIn(username,password):
    for user,word in zip(usernames,passwords):
        if user == username and word==password:
            root.destroy()
            gui.main(username)
            return

def newUser(username,password):
    if username in usernames:
         return
    with open("loginInfo.csv", "w", newline="", encoding="utf-8") as file:
        csvWriter = csv.writer(file)
        usernames.append(username)
        passwords.append(password)
        csvWriter.writerows([usernames, passwords])


root=Tk()
passLabel=Label(root,text="Enter Username and Password:")
usernameFrame=Frame(root)
usernameFrame.pack()
passwordFrame=Frame(root)
passwordFrame.pack()

usernameInput=StringVar()
usernameLabel=Label(usernameFrame,text="Username:")
usernameLabel.pack(side=LEFT,padx=10)
username=Entry(usernameFrame,textvariable=usernameInput)
username.pack(side=LEFT)

passwordInput=StringVar()
passwordLabel=Label(passwordFrame,text="Password: ")
passwordLabel.pack(side=LEFT,padx=10)
password=Entry(passwordFrame,textvariable=passwordInput)
password.pack(side=LEFT)

buttonFrame=Frame(root)
buttonFrame.pack()
newUserButton=Button(buttonFrame,text="New User",command=lambda: newUser(usernameInput.get(),passwordInput.get()))
newUserButton.pack(side=LEFT)
logInButton=Button(buttonFrame,text="Log In",command=lambda: checkLogIn(usernameInput.get(),passwordInput.get()))
logInButton.pack(side=LEFT)

root.mainloop()