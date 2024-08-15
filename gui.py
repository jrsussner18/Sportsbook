from tkinter import *
from tkinter import ttk
import csv

root = Tk()
root.geometry("750x350")
root.title("Sportsbook")

total_odds = 1


# function to calculate the odds of a parlay
def calcOdds(odds, button1, button2, bet_name):
    # Button 1 is the opposite button
    # Button 2 is the button the user is pressing
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
        final_odds = "+" + str(round((total_odds - 1) * 100))
    button2.config(bg="green")
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    oddsTextArea.insert(END, f"{bet_name}: {odds}\n")


widgets = []


# Function that changes the given week, clears any previous widgets, and adds new ones
def change(selection):
    global test
    test = selection
    clearWidgets()
    labelsButtons(root, "lines.csv")


# Function that deletes all widgets from the list
def clearWidgets():
    for widget in widgets:
        widget.pack_forget()
    widgets.clear()


# List of different weeks to choose from for the option Menu
options = [
    "Week 1",
    "Week 2",
    "Week 3",
    "Week 4",
    "Week 5",
    "Week 6",
    "Week 7",
    "Week 8",
    "Week 9",
    "Week 10",
    "Week 11",
    "Week 12",
    "Week 13",
    "Week 14",
    "Week 15",
    "Week 16",
    "Week 17",
    "Week 18",
]
clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=change)
drop.pack()


def leftFrameWork(leftFrame, read):
    titleFrame = Frame(leftFrame)
    teams_title = Label(titleFrame, text="Teams", width=15)
    spread_title = Label(titleFrame, text="Spread", width=10)
    spread_odds_title = Label(titleFrame, text="Spread odds", width=10)
    ml_title = Label(titleFrame, text="Money line", width=10)
    titleFrame.pack()
    teams_title.pack(side=LEFT)
    spread_title.pack(side=LEFT)
    spread_odds_title.pack(side=LEFT)
    ml_title.pack(side=LEFT)
    widgets.append(titleFrame)
    widgets.append(teams_title)
    widgets.append(spread_title)
    widgets.append(spread_odds_title)
    widgets.append(ml_title)
    for x, index in enumerate(read):
        if index[-1] == test.split(" ")[1]:
            # Initialize Labels
            away_frame = Frame(leftFrame)
            home_frame = Frame(leftFrame)
            away = Label(away_frame, text=index[0], width=15)
            home = Label(home_frame, text=index[1], width=15)
            spread_away = Label(
                away_frame, text=index[2], fg="red", bg="blue", width=10
            )
            spread_odds_away = Button(
                away_frame, text=index[3], fg="red", bg="blue", width=10
            )
            ml_away = Button(away_frame, text=index[4], fg="red", bg="blue", width=10)
            spread_home = Label(
                home_frame, text=index[5], fg="blue", bg="red", width=10
            )
            spread_odds_home = Button(
                home_frame, text=index[6], fg="blue", bg="red", width=10
            )
            ml_home = Button(home_frame, text=index[7], fg="blue", bg="red", width=10)

            spread_odds_away.config(
                command=lambda odds=index[
                    3
                ], opp_button=spread_odds_home, curr_button=spread_odds_away, bet_name="Chiefs spread": calcOdds(
                    odds, opp_button, curr_button, bet_name
                )
            )
            ml_away.config(
                command=lambda odds=index[
                    4
                ], opp_button=ml_home, curr_button=ml_away, bet_name="Chiefs spread": calcOdds(
                    odds, opp_button, curr_button, bet_name
                )
            )
            spread_odds_home.config(
                command=lambda odds=index[
                    6
                ], opp_button=spread_odds_away, curr_button=spread_odds_home, bet_name="Chiefs spread": calcOdds(
                    odds, opp_button, curr_button, bet_name
                )
            )
            ml_home.config(
                command=lambda odds=index[
                    7
                ], opp_button=ml_away, curr_button=ml_home, bet_name="Chiefs spread": calcOdds(
                    odds, opp_button, curr_button, bet_name
                )
            )
            # Pack Buttons and add them to a list(widgets) to be deleted when changing weeks
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
            # Space Frame to put a small gap between games
            spaceFrame = Frame(root, height=10)
            spaceFrame.pack()
            widgets.append(spaceFrame)


def rightFrameWork(rightFrame):
    global oddsTextArea
    frameTitle = Label(rightFrame, text="Your Odds Sir")
    frameTitle.pack()
    oddsFrame = Frame(rightFrame)
    oddsFrame.pack()
    oddsTextArea = Text(oddsFrame, height="20", width="30")
    oddsTextArea.pack()
    inputFrame = Frame(rightFrame)
    inputFrame.pack()
    idkWhatToNameThisLabel = Label(
        inputFrame, text="How many dollars would you like to put in?", anchor="se"
    )
    idkWhatToNameThisLabel.pack()
    entryAmt = IntVar()
    dollarEntry = Entry(inputFrame, textvariable=entryAmt)
    button = ttk.Button(inputFrame, text="Submit")
    dollarEntry.pack(side="left")
    button.pack(side="left")


def labelsButtons(root, csv_file):
    global test
    with open(csv_file, "r", encoding="utf-8") as file:
        read = csv.reader(file)
        next(read)
        # Add Labels and then packing and appending them to a list(widgets) so that they can be deleted later
        leftFrame = Frame(root)
        rightFrame = Frame(root)
        leftFrame.pack(side=LEFT, fill=BOTH, expand=True)
        rightFrame.pack(side=LEFT, fill=BOTH, expand=True)
        leftFrameWork(leftFrame, read)
        rightFrameWork(rightFrame)


root.mainloop()
