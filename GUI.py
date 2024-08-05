# Jake Sussner
# Graphical User Interfaces
# 9/13/23

# GUI: an interface that ues windows, icons, buttons...graphics
# Window: An area on the screen that displays information.
# Menu: Allows users to execute commands by selecting from a list of options.
# Icon: A small picture that represents something else (e.g., a file, an application, a command, etc).
# Control (Widget): A component that users directly interact with to perform some task (e.g., a list, a label, a check box, a radio button, a slider, etc.)
# Tab: A way of grouping GUI components in an area of a window.

# Tkinter (TK Interface): a librarly used for creating GUI's in python
# Use GUI's by first creating a window then placing widgets on the window.
#    GUI's have a listener and an event handler
#    These get triggered when the user does something relevant
#    The event then gets registered and the coded action occurs


# #create a window
# window = Tk()
# #add a text box
# text1 = Label(window, text= "GUIs in Python are pretty easy!")
# text2 = Label(window, text = "Python is great!")
# #putting the text label in the window
# text1.pack()
# text2.pack()
# #loop until user closes window
# window.mainloop()


# specifing that the app will fit inside a frame.
#     Frames are objects that let us organize GUI widgets

# class App(Frame):
#     def __init__(self, master):
#         Frame.__init__(self, master)
#         # the buttons are widgets of the app class
#         self.button1 = Button(master, text="BYE!", fg="red", command=self.quit)
#         # 'fill = X' expands the button horizontally, and 'Y' vertically
#         self.button1.pack(fill = BOTH)
#         self.button2 = Button(master, text="Say something!",  command=self.say)
#         self.button2.pack(fill = BOTH)
#     def say(self):
#         print("Froot Loops!")
#         self.button2.config(text = "Clicked", fg = "red")
#
# ###MAIN PROGRAM###
# window = Tk()
# app = App(window)

from tkinter import *

# class App(Frame):
#     def __init__(self, window):
#         Frame.__init__(self, window)
#         self.label = Label(window, text = "Hello World!", bg = "white", fg = "black")
#         self.label.pack(side = TOP)
#         self.button1 = Button(window, text = "Hello!", fg = "black", command = self.say)
#         self.button1.pack(side = TOP)
#         self.check = Checkbutton(window, text = "Check!", bg = "white", fg = "black")
#         self.check.pack(side = TOP)
#         self.img = PhotoImage(file = "Circle.png")
#         self.image = Label(width = 500, image = self.img)
#         self.image.pack(side=LEFT, fill = Y)
#     def say(self):
#         self.label.config(text = "Goodbye World!", fg = "black")
#
# window = Tk()
# window.title("Playing with GUI's")
# app = App(window)
# window.mainloop()

# Grid manager organizes widgets like Frame does, but by using rows and cols.
# Width of a column = width of its widest widget
# Height of a row = height of its tallest widget
# Each box is called a cell, where you place a widget
# if you place 2+ widgets in a single cell, they could end up on top of each other.


class App(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.label1 = Label(window, text="Email:", bg="#E200E6")
        self.label2 = Label(window, text="Password:", bg="#E200E6")
        # putting both label widgets in a grid
        # initializing the grids row and column for the widget
        # sticky lets us place a widget in a cell where you want to
        # without sticky itll just center itself
        self.label1.grid(row=0, column=0, sticky=E)
        self.label2.grid(row=1, column=0, sticky=E)
        # Entry is where the user can type in single line strings
        self.emailBox = Entry(window)
        self.pwBox = Entry(window)
        self.emailBox.grid(row=0, column=1)
        self.pwBox.grid(row=1, column=1)
        # "Command=None" because the login button doesn't do anything
        self.loginBtn = Button(window, text="Login", command=None)
        # "columnspan = 2" spreads the widget into two columns
        # Similar with rowspan
        self.loginBtn.grid(row=2, columnspan=2)
        self.can1 = Canvas(window, bg="black", height=300, width=300)
        self.oval = self.can1.create_oval(50, 50, 250, 250)


window = Tk()
window.title("Adding an Image")
g = App(window)
window.config(bg="#E200E6")

window.mainloop()
