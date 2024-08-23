# Libaries used to import
from tkinter import *
import csv

# Creating and Labeling the GUI window
# Global variables
total_odds = 1  # Used to keep track of the total odds of a parlay
final_odds = ""  # Used to keep track of the + or - odds of total_odds
widgets = []  # List to store all widgets to be cleared in clearWidgets
curr_bets = []  # List to store all the current bets of a parlay
disabled_buttons = {}  # Dictionary to store the disabled buttons number and week


def main(username):
    global user
    user = username
    root = Tk()
    root.geometry("750x500")
    root.title("Sportsbook")
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
    # Creating the initial dropdown menu for picking different weeks
    clicked = StringVar()
    clicked.set(options[0])
    # Corrected lambda to pass the selected week directly
    drop = OptionMenu(
        root, clicked, *options, command=lambda selection: change(selection, root)
    )
    x=getBets()
    betsOptions=[z+1 for z in range(len(x))]
    betClicked=IntVar()
    betDropDown=OptionMenu(root, betClicked, *betsOptions, command=lambda selection, prevBets=x:printPrevBets(selection,prevBets,root))
    drop.pack()

    prevBetLabel=Label(root, text="Previous Bets:")
    prevBetLabel.pack()
    betDropDown.pack()

    # Initialize with the first week's data
    change(clicked.get(), root)
    root.mainloop()


# Function that finds all the bets from the given username and makes a list of bets to be displayed later. Add bets to curr_bets maybe?
def getBets():
    lists=[]
    with open("prevBetInfo.csv", "r", newline="", encoding="utf-8") as file:
        reader=csv.reader(file)
        counter=1
        for thing in reader:
            if thing[0]==user:
                thing[0]=counter
                counter+=1
                lists.append(thing)
    return lists

def printPrevBets(selection, prevBets,root):
    global curr_bets
    global final_odds
    curr_bets=prevBets[selection-1]
    final_odds=curr_bets[2]
    change("Week 1", root)


def calcOdds(
    odds, button1, button2, team_name, bet_name, button_number1, button_number2
):

    # Make sure you are printing multiple final odds
    finalOddsTextArea.delete(0.0, END)

    # grab global variables to update
    global total_odds
    global final_odds

    # algroithm to convert american "+" or "-" odds to European decimal odds
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

    # Button 1 is the opposite button
    # Button 2 is the button the user is pressing
    # Disable buttons so user can't make the same bet more than once
    button2.config(bg="green")
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)

    # add disabled buttons to dictionary
    disabled_buttons[button_number1] = test
    disabled_buttons[button_number2] = test

    # Add bet to list
    curr_bets.append([team_name, bet_name, odds])

    # call function to put odds in respective textbox widgets
    keepPicksOnText()


# Function that will prevent the parlay from being cleared from view
def keepPicksOnText():
    global final_odds
    oddsTextArea.delete("1.0", "end")
    if len(curr_bets)==0:
        finalOddsTextArea.insert(END, f"Total Odds: {final_odds}")
    elif type(curr_bets[0])==int:
        bet_string=curr_bets[1]
        # First, split the string by commas to separate each bet
        bets = bet_string.split(',')

        # Iterate over each bet and extract the team name, bet type, and odds
        for bet in bets:
            if bet:
                parts = bet.split()
                team_name = parts[0] + " " + parts[1]
                bet_type = parts[2]
                bet_odds = parts[3]
                oddsTextArea.insert(END, f"{team_name} {bet_type} {bet_odds}\n")
        finalOddsTextArea.delete(0.0, END)
        finalOddsTextArea.insert(END, f"Total Odds: {final_odds}")
        finalOddsTextArea.insert(END,f"\n\nBet Amount: {curr_bets[3]} \nTo win: {curr_bets[4]}")
    elif type(curr_bets[0][0])==str:
        for bet in curr_bets:
            oddsTextArea.insert(END, f"{bet[0]} {bet[1]}: {bet[2]}\n")
        finalOddsTextArea.insert(END, f"Total Odds: {final_odds}")


# Function that changes the given week, clears any previous widgets, and adds new ones
def change(selection, root):
    global test
    test = selection
    clearWidgets()
    labelsButtons(root, "lines.csv")
    keepPicksOnText()


# Function that deletes all widgets from the list
def clearWidgets():
    for widget in widgets:
        if isinstance(widget, (Label, Button, Frame, Text, Entry)):
            widget.pack_forget()
    widgets.clear()


# Function that will submit the user bet
def submitBet():
    # grab global variables to update
    global curr_bets
    global total_odds
    global disabled_buttons

    # get user wager amount and calc winnings if parlay hits
    wager = int(dollarEntry.get())
    winnings = "${:.2f}".format(total_odds * wager)
    wager = "$" + str(wager)
    dollarEntry.delete("0", END)

    # sample output of what already made bets could look like
    # print("Your Bet: \n")
    # print(f"{wager} to win: {winnings} \n")
    # for bet in curr_bets:
    #     print(f"{bet[0]} {bet[1]}: {bet[2]}\n")
    # print(f"Total odds:  {final_odds}\n")

    # delete previous made entrys
    dollarEntry.delete("0", END)
    oddsTextArea.delete(0.0, END)
    finalOddsTextArea.delete(1.11, END)  # deletes the odds after the text "Total Odds:"
    finalOddsTextArea.delete(1.11, END)

    storeBets(curr_bets, final_odds, wager, winnings)
    # reset all betting odds
    curr_bets = []
    total_odds = 1
    # clear the disabled buttons dictionary
    disabled_buttons.clear()

    # reset the buttons to not be disabled
    for widget in widgets:
        if isinstance(widget, Button):
            widget["state"] = NORMAL


def storeBets(user_bets, final_odds, wager, winnings):
    all_bets = ""
    for bets in user_bets:
        # join the list of curr_bets together
        all_bets += f"{bets[0]} {bets[1]}: {bets[2]},"

    # open csvfile and write bets to file
    with open("prevBetInfo.csv", "a", newline="", encoding="utf-8") as file:
        csvWriter = csv.writer(file)

        # csvWriter.writerow(["Bets", "Total Odds", "Wager", "Winnings"])
        csvWriter.writerow(
            [
                user,
                all_bets,
                final_odds,
                wager,
                winnings,
            ]
        )


def leftFrameWork(leftFrame, read, root):
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

    button_count = 1

    for x, index in enumerate(read):
        if index[-1] == test.split(" ")[1]:
            # Initialize Labels
            spread_odds_away_button_count = button_count
            spread_odds_home_button_count = button_count + 2
            Ml_odds_away_button_count = button_count + 1
            ML_odds_home_button_count = button_count + 3
            away_frame = Frame(leftFrame)
            home_frame = Frame(leftFrame)
            away = Label(away_frame, text=index[0], width=15)
            home = Label(home_frame, text=index[1], width=15)
            spread_away = Label(
                away_frame, text=index[2], fg="red", bg="blue", width=10
            )
            spread_odds_away = Button(
                away_frame,
                text=index[3],
                fg="red",
                bg="blue",
                name=str(spread_odds_away_button_count),
                width=10,
            )
            ml_away = Button(
                away_frame,
                text=index[4],
                fg="red",
                bg="blue",
                name=str(Ml_odds_away_button_count),
                width=10,
            )
            spread_home = Label(
                home_frame, text=index[5], fg="blue", bg="red", width=10
            )
            spread_odds_home = Button(
                home_frame,
                text=index[6],
                fg="blue",
                bg="red",
                name=str(spread_odds_home_button_count),
                width=10,
            )
            ml_home = Button(
                home_frame,
                text=index[7],
                fg="blue",
                bg="red",
                name=str(ML_odds_home_button_count),
                width=10,
            )

            spread_odds_away.config(
                command=lambda odds=index[
                    3
                ], opp_button=spread_odds_home, curr_button=spread_odds_away, team_name=index[
                    0
                ], bet_name="spread", away_button_number=spread_odds_away_button_count, home_button_number=spread_odds_home_button_count: calcOdds(
                    odds,
                    opp_button,
                    curr_button,
                    team_name,
                    bet_name,
                    away_button_number,
                    home_button_number,
                )
            )
            ml_away.config(
                command=lambda odds=index[
                    4
                ], opp_button=ml_home, curr_button=ml_away, team_name=index[
                    0
                ], bet_name="ML", away_button_number=Ml_odds_away_button_count, home_button_number=ML_odds_home_button_count: calcOdds(
                    odds,
                    opp_button,
                    curr_button,
                    team_name,
                    bet_name,
                    away_button_number,
                    home_button_number,
                )
            )
            spread_odds_home.config(
                command=lambda odds=index[
                    6
                ], opp_button=spread_odds_away, curr_button=spread_odds_home, team_name=index[
                    1
                ], bet_name="spread", home_button_number=spread_odds_home_button_count, away_button_number=spread_odds_away_button_count: calcOdds(
                    odds,
                    opp_button,
                    curr_button,
                    team_name,
                    bet_name,
                    home_button_number,
                    away_button_number,
                )
            )
            ml_home.config(
                command=lambda odds=index[
                    7
                ], opp_button=ml_away, curr_button=ml_home, team_name=index[
                    1
                ], bet_name="ML", home_button_number=ML_odds_home_button_count, away_button_number=Ml_odds_away_button_count: calcOdds(
                    odds,
                    opp_button,
                    curr_button,
                    team_name,
                    bet_name,
                    home_button_number,
                    away_button_number,
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
            # Space Frame to put a small gap between games
            spaceFrame = Frame(root, height=100)
            spaceFrame.pack()
            away_frame.pack()
            home_frame.pack()
            widgets.append(away_frame)
            widgets.append(home_frame)
            widgets.append(spaceFrame)

            button_count += 4

    # once the widgets are made disable buttons that are still in the disabled_buttons dictionary
    for widget in widgets:
        if isinstance(widget, Button):
            for button_number, week in disabled_buttons.items():
                if int(widget._name) == button_number and test == week:
                    widget["state"] = DISABLED

def clearChoices():
    curr_bets.clear
    oddsTextArea.delete("1.0", "end")
    finalOddsTextArea.delete("1.0", "end")
    dollarEntry.delete(0, END)
    for widget in widgets:
        if isinstance(widget, Button):
            widget["state"] = NORMAL
    


def rightFrameWork(rightFrame):
    global oddsTextArea
    global finalOddsTextArea
    global dollarEntry
    global inputFrame

    frameTitle = Label(rightFrame, text="Your Odds Sir")
    frameTitle.pack()
    oddsFrame = Frame(rightFrame)
    oddsFrame.pack()
    oddsTextArea = Text(oddsFrame, height="20", width="30")
    oddsTextArea.pack(side="top")
    finalOddsTextArea = Text(oddsFrame, height="5", width="30")
    finalOddsTextArea.pack(side="bottom")
    inputFrame = Frame(rightFrame)
    inputFrame.pack()
    MoneyLabel = Label(
        inputFrame, text="How many dollars would you like to put in?", anchor="se"
    )
    MoneyLabel.pack()
    entryAmt = IntVar()
    dollarEntry = Entry(inputFrame, textvariable=entryAmt)
    button = Button(inputFrame, text="Submit", command=submitBet)
    dollarEntry.pack(side="left")
    button.pack(side="left")
    clear_button = Button(rightFrame, text="Clear", command= lambda: clearChoices())
    clear_button.pack()
    widgets.append(frameTitle)
    widgets.append(oddsFrame)
    widgets.append(oddsTextArea)
    widgets.append(finalOddsTextArea)
    widgets.append(inputFrame)
    widgets.append(MoneyLabel)
    widgets.append(entryAmt)
    widgets.append(dollarEntry)
    widgets.append(button)


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
        leftFrameWork(leftFrame, read, root)
        rightFrameWork(rightFrame)
        widgets.append(leftFrame)
        widgets.append(rightFrame)


# for debugging code to bypass login
main("test")
