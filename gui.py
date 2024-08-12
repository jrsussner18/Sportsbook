from tkinter import *
import csv
import math

root = Tk()
root.geometry('750x350')

# create global variable for total odds so it doesn't reset
total_odds = 1


# function to grab the odds and calculate parlay odds
def calcOdds(odds):
    global total_odds
    if odds[0] == "−":
        curr_odd = int(odds[1:])
        curr_odd = 1 + (100 / curr_odd)
    else:
        curr_odd = int(odds[1:])
        curr_odd = 1 + (curr_odd / 100)
    total_odds = total_odds * curr_odd
    if total_odds <= 2:
        final_odds = "-" + str(round((100 / (total_odds - 1))))
    else:
        final_odds = "+" + str(round(((total_odds - 1) * 100)))


# function to grab user input from entry bar convert it to an integer and make it global
# "week" can now be changed out with "row" in the function "labels_buttons"
def userInput():
    global week
    week = int(user_input.get())


def labels_buttons(root, csv_file):
    with open(csv_file, "r", encoding="utf-8") as file:
        read = csv.reader(file)
        next(read)
        for x, index in enumerate(read):

            # Initialize Labels and Buttons
            test = Button(root, text="test", fg="blue", bg="red", activebackground="red").grid(row=1, column=7)
            away = Label(root, text=index[0])
            home = Label(root, text=index[1])
            spread_away = Label(root, text=index[2], fg="red", bg="blue")
            spread_odds_away = Button(
                root, text=index[3], fg="red", bg="blue", command=lambda: calcOdds(index[3])
            )
            ml_away = Button(root, text=index[4], fg="red", bg="blue", command=lambda: calcOdds(index[4]))
            spread_home = Label(root, text=index[5], fg="blue", bg="red")
            spread_odds_home = Button(
                root, text=index[6], fg="blue", bg="red", command=lambda: calcOdds(index[6])
            )
            ml_home = Button(root, text=index[7], fg="blue", bg="red", command=lambda: calcOdds(index[7]))

            # Grid locations
            
            away.grid(row=(x * 2) + 1, column=0, sticky=W)
            home.grid(row=(x * 2) + 2, column=0, sticky=W)
            spread_away.grid(row=(x * 2) + 1, column=1)
            spread_odds_away.grid(row=(x * 2) + 1, column=2)
            ml_away.grid(row=(x * 2) + 1, column=3)
            spread_home.grid(row=(x * 2) + 2, column=1)
            spread_odds_home.grid(row=(x * 2) + 2, column=2)
            ml_home.grid(row=(x * 2) + 2, column=3)



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
# question.grid(row=10, column=0, sticky=W)
teams_title.grid(row=0, column=0, sticky=W)
spread_title.grid(row=0, column=1)
spread_odds_title.grid(row=0, column=2)
ml_title.grid(row=0, column=3)

# user_input.grid(row=10, column=2, sticky=W)

# submit.grid(row=10, column=3)


labels_buttons(root, "lines.csv")

root.mainloop()
