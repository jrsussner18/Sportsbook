from tkinter import *
import csv

root = Tk()


# function to grab user input from entry bar convert it to an integer and make it global
# "week" can now be changed out with "row" in the function "labels_buttons"
def userInput():
    global week
    week = int(user_input.get())


def labels_buttons(root, csv_file):
    with open(csv_file, "r", encoding="utf-8") as file:
        read = csv.reader(file)
        next(read)
        for row, index in enumerate(read):
            # Need help here, I have row set to 0 but this is where I would like to generate user input
            if row == 0:

                # Initialize Labels
                away = Label(root, text=index[0])
                home = Label(root, text=index[1])
                spread_away = Button(root, text=index[2])
                spread_odds_away = Button(root, text=index[3])
                ml_away = Button(root, text=index[4])
                spread_home = Button(root, text=index[5])
                spread_odds_home = Button(root, text=index[6])
                ml_home = Button(root, text=index[7])

                # Initialize Buttons
                away.grid(row=1, column=0, sticky=W)
                home.grid(row=2, column=0, sticky=W)
                spread_away.grid(row=1, column=1)
                spread_odds_away.grid(row=1, column=2)
                ml_away.grid(row=1, column=3)
                spread_home.grid(row=2, column=1)
                spread_odds_home.grid(row=2, column=2)
                ml_home.grid(row=2, column=3)


# Initialize Labels
question = Label(root, text="What week do you want to bet on?")
teams_title = Label(root, text="Teams")
spread_title = Label(root, text="Spread", width=10)
spread_odds_title = Label(root, text="Spread odds", width=10)
ml_title = Label(root, text="Money line", width=10)

# Initialize Entry box
user_input = Entry(root, width=25)

# Initialize Button
submit = Button(root, text="Submit", command=userInput)

# Putting widgets in the GUI
question.grid(row=10, column=0, sticky=W)
teams_title.grid(row=0, column=0, sticky=W)
spread_title.grid(row=0, column=1)
spread_odds_title.grid(row=0, column=2)
ml_title.grid(row=0, column=3)

user_input.grid(row=10, column=2, sticky=W)

submit.grid(row=10, column=3)


labels_buttons(root, "lines.csv")

root.mainloop()
