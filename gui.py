from tkinter import *
import csv
import math

root = Tk()
root.geometry("750x350")

# create global variable for total odds so it doesn't reset
total_odds = 1


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


def userInput():
    global week
    week = int(user_input.get())


def labels_buttons(root, csv_file):
    global test
    with open(csv_file, "r", encoding="utf-8") as file:
        read = csv.reader(file)
        next(read)
        for x, index in enumerate(read):
            # Need help here, I have row set to 0 but this is where I would like to generate user input
            if index[-1] == test.split(" ")[1]:
                # Initialize Labels
                away_frame = Frame(root)
                home_frame = Frame(root)
                away = Label(away_frame, text=index[0])
                home = Label(home_frame, text=index[1])
                spread_away = Label(away_frame, text=index[2], fg="red", bg="blue")
                spread_odds_away = Button(
                    away_frame,
                    text=index[3],
                    fg="red",
                    bg="blue",
                    command=lambda: calcOdds(index[3]),
                )
                ml_away = Button(
                    away_frame,
                    text=index[4],
                    fg="red",
                    bg="blue",
                    command=lambda: calcOdds(index[4]),
                )
                spread_home = Label(home_frame, text=index[5], fg="blue", bg="red")
                spread_odds_home = Button(
                    home_frame,
                    text=index[6],
                    fg="blue",
                    bg="red",
                    command=lambda: calcOdds(index[6]),
                )
                ml_home = Button(
                    home_frame,
                    text=index[7],
                    fg="blue",
                    bg="red",
                    command=lambda: calcOdds(index[7]),
                )
                # Initialize Buttons
                away.pack(side="left")
                widgets.append(away)
                home.pack(side="left")
                widgets.append(home)

                spread_away.pack(side="left")
                widgets.append(spread_away)

                spread_odds_away.pack(side="left")
                widgets.append(spread_odds_away)

                ml_away.pack(side="left")
                widgets.append(ml_away)

                spread_home.pack(side="left")
                widgets.append(spread_home)

                spread_odds_home.pack(side="left")
                widgets.append(spread_odds_home)

                ml_home.pack(side="left")
                widgets.append(ml_home)
                away_frame.pack()
                home_frame.pack()
                widgets.append(away_frame)
                widgets.append(home_frame)


# # Initialize Labels
# teams_title = Label(root, text="Teams")
# spread_title = Label(root, text="Spread", width=10)
# spread_odds_title = Label(root, text="Spread odds", width=10)
# ml_title = Label(root, text="Money line", width=10)

# # Putting widgets in the GUI
# teams_title.grid(row=0, column=0, sticky=W)
# spread_title.grid(row=0, column=1)
# spread_odds_title.grid(row=0, column=2)
# ml_title.grid(row=0, column=3)

root.mainloop()
