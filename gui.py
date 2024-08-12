from tkinter import *
import csv

root = Tk()


# function to grab user input from entry bar convert it to an integer and make it global
# "week" can now be changed out with "row" in the function "labels_buttons"
total_odds = 1


def calcOdds(odds):
    global total_odds
    print(odds)
    print(odds[0])
    if odds[0] == "−":
        curr_odd = int(odds[1:])
        curr_odd = 1 + (100 / curr_odd)
        print(curr_odd)
    else:
        curr_odd = int(odds[1:])
        curr_odd = 1 + (curr_odd / 100)
        print(curr_odd)
    total_odds = total_odds * curr_odd
    print(total_odds)
    if total_odds >= 1:
        final_odds = "-" + str((100 / (total_odds - 1)))
    else:
        final_odds = "+" + str(((total_odds - 1) * 100))
    print(final_odds)


def userInput():
    global week
    week = int(user_input.get())


def labels_buttons(root, csv_file):
    with open(csv_file, "r", encoding="utf-8") as file:
        read = csv.reader(file)
        next(read)
        for x, index in enumerate(read):
            # Need help here, I have row set to 0 but this is where I would like to generate user input
            # if row == 0:

            # Initialize Labels
            away = Label(root, text=index[0])
            home = Label(root, text=index[1])
            spread_away = Label(root, text=index[2])
            spread_odds_away = Button(
                root, text=index[3], command=lambda: calcOdds(index[3])
            )
            ml_away = Button(root, text=index[4], command=lambda: calcOdds(index[4]))
            spread_home = Label(root, text=index[5])
            spread_odds_home = Button(
                root, text=index[6], command=lambda: calcOdds(index[6])
            )
            ml_home = Button(root, text=index[7], command=lambda: calcOdds(index[7]))

            # Initialize Buttons
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
