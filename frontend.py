# Libaries used to import
from tkinter import *
import csv
import utils

# Creating and Labeling the GUI window
# Global variables
total_odds = 1  # Used to keep track of the total odds of a parlay
final_odds = ""  # Used to keep track of the + or - odds of total_odds
widgets = []  # List to store all widgets to be cleared in clearWidgets
curr_bets = []  # List to store all the current bets of a parlay
disabled_buttons = {}  # Dictionary to store the disabled buttons number and week


# Main Function that sets up the initial screen and pulls and stores previous bets from the given username
def main(username):
    global user
    user = username
    # Creating the Tkinter window and fitting it to our needs
    root = Tk()
    root.geometry("1300x650")
    root.title("Sportsbook")
    # List of different weeks to choose from for the option Menu
    week_options = [
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
    clicked_week = StringVar()
    clicked_week.set(week_options[0])
    # Corrected lambda to pass the selected week directly
    drop = OptionMenu(
        root,
        clicked_week,
        *week_options,
        command=lambda selection: change(selection, root),
    )
    prev_bets = getBets()
    bets_options = [prev_bet_index + 1 for prev_bet_index in range(len(prev_bets))]
    bet_clicked = IntVar()
    bet_drop_down = OptionMenu(
        root,
        bet_clicked,
        *bets_options,
        command=lambda selection, prev_bets=prev_bets: printPrevBets(
            selection, prev_bets, root
        ),
    )
    drop.pack()

    prev_bet_label = Label(root, text="Previous Bets:")
    prev_bet_label.pack()
    bet_drop_down.pack()

    # Initialize with the first week's data
    change(clicked_week.get(), root)
    root.mainloop()


# Function that finds all the bets from the given username and makes a list of bets to be displayed later. Add bets to curr_bets maybe?
def getBets():
    prev_bet_list = []
    with open("prevBetInfo.csv", "r", newline="", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        counter = 1
        for prev_bet in csv_reader:
            if prev_bet[0] == user:
                prev_bet[0] = counter
                counter += 1
                prev_bet_list.append(prev_bet)
    return prev_bet_list


def printPrevBets(selection, prevBets, root):
    global curr_bets
    global final_odds
    clearChoices()
    curr_bets = prevBets[selection - 1]
    final_odds = curr_bets[2]
    change("Week 1", root, False)


def calcOdds(
    odds,
    opp_button,
    clicked_button,
    team_name,
    bet_name,
    button_number1,
    button_number2,
):

    # Make sure you are printing multiple final odds
    final_odds_text_area.delete(0.0, END)

    # grab global variables to update
    global total_odds
    global final_odds
    global curr_odd

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
    opp_button.config(state=DISABLED)
    clicked_button.config(state=DISABLED)

    # add disabled buttons to dictionary
    disabled_buttons[button_number1] = week_selection
    disabled_buttons[button_number2] = week_selection

    # Add bet to list
    curr_bets.append([team_name, bet_name, odds])

    # call function to put odds in respective textbox widgets
    keepPicksOnText(True)


# Function that will prevent the parlay from being cleared from view
def keepPicksOnText(flag=True):
    global final_odds
    # add a flag to see if function is called from calcOdds or change function
    if flag == False:
        odds_text_area.delete("1.0", "end")
        if len(curr_bets) == 0:
            final_odds_text_area.insert(END, f"Total Odds: {final_odds}")
        elif type(curr_bets[0]) == int:
            bet_string = curr_bets[1]
            bets = bet_string.split(",")

            # Iterate over each bet and extract the team name, bet type, and odds
            for prev_bet in bets:
                if prev_bet:
                    parts_of_prev_bets = prev_bet.split()
                    team_name = parts_of_prev_bets[0] + " " + parts_of_prev_bets[1]
                    bet_type = parts_of_prev_bets[2]
                    bet_odds = parts_of_prev_bets[3]
                    odds_text_area.insert(END, f"{team_name} {bet_type} {bet_odds}\n")
            final_odds_text_area.delete(0.0, END)
            final_odds_text_area.insert(END, f"Total Odds: {final_odds}")
            final_odds_text_area.insert(
                END, f"\n\nBet Amount: {curr_bets[3]} \nTo win: {curr_bets[4]}"
            )
        elif type(curr_bets[0][0]) == str:
            for bet in curr_bets:
                odds_text_area.insert(END, f"{bet[0]} {bet[1]}: {bet[2]}\n")
            final_odds_text_area.insert(END, f"Total Odds: {final_odds}")
    else:
        odds_text_area.delete("1.0", "end")
        final_odds_text_area.delete(0.0, END)
        final_odds_text_area.insert(END, f"Total Odds: {final_odds}")
        for index in range(len(curr_bets)):
            if type(curr_bets[index]) == list:
                odds_text_area.insert(
                    END,
                    f"{curr_bets[index][0]} {curr_bets[index][1]}: {curr_bets[index][2]}\n",
                )


# Function that changes the given week, clears any previous widgets, and adds new ones
def change(selection, root, flag=True):
    global week_selection
    week_selection = selection
    clearWidgets()
    labelsButtons(root, "lines.csv")
    if flag == False:
        keepPicksOnText(flag)
    else:
        keepPicksOnText(flag)


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
    wager = int(dollar_entry.get())
    winnings = "${:.2f}".format(total_odds * wager)
    wager = "$" + str(wager)
    dollar_entry.delete("0", END)

    # delete previous made entrys
    dollar_entry.delete("0", END)
    odds_text_area.delete(0.0, END)
    final_odds_text_area.delete(
        1.11, END
    )  # deletes the odds after the text "Total Odds:"
    final_odds_text_area.delete(1.11, END)

    # make sure that only the current user bets are sent to the storeBets function
    user_bets = []
    for index in range(len(curr_bets)):
        if type(curr_bets[index]) == list:
            user_bets.append(curr_bets[index])

    storeBets(user_bets, final_odds, wager, winnings)
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
        csv_writer = csv.writer(file)

        # csvWriter.writerow(["Bets", "Total Odds", "Wager", "Winnings"])
        csv_writer.writerow(
            [
                user,
                all_bets,
                final_odds,
                wager,
                winnings,
            ]
        )


def leftFrameWork(left_frame, read, root):
    button_count = 1
    left_left_frame = Frame(left_frame)
    left_right_frame = Frame(left_frame)
    widgets.append(left_left_frame)
    widgets.append(left_right_frame)
    curr_frame = left_left_frame
    for thing in range(2):
        titleFrame = Frame(curr_frame)
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
        curr_frame = left_right_frame
    for x, index in enumerate(read):
        if index[-1] == week_selection.split(" ")[1]:
            # Initialize Labels
            spread_odds_away_button_count = button_count
            spread_odds_home_button_count = button_count + 2
            Ml_odds_away_button_count = button_count + 1
            ML_odds_home_button_count = button_count + 3
            away_frame = Frame(curr_frame)
            home_frame = Frame(curr_frame)
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
            left_left_frame.pack(side=LEFT)
            left_right_frame.pack(side=LEFT)
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
            if curr_frame == left_left_frame:
                curr_frame = left_right_frame
            else:
                curr_frame = left_left_frame
            button_count += 4

    # once the widgets are made disable buttons that are still in the disabled_buttons dictionary
    for widget in widgets:
        if isinstance(widget, Button):
            for button_number, week in disabled_buttons.items():
                if int(widget._name) == button_number and week_selection == week:
                    widget["state"] = DISABLED


def clearChoices():
    global curr_bets
    global final_odds
    global total_odds
    total_odds = 1
    final_odds = 0
    curr_bets = []
    odds_text_area.delete("1.0", "end")
    final_odds_text_area.delete("1.0", "end")
    dollar_entry.delete(0, END)
    for widget in widgets:
        if isinstance(widget, Button):
            widget["state"] = NORMAL


def rightFrameWork(right_frame):
    global odds_text_area
    global final_odds_text_area
    global dollar_entry
    global input_frame
    frame_title = Label(right_frame, text="Your Odds Sir")
    frame_title.pack()
    odds_frame = Frame(right_frame)
    odds_frame.pack()
    odds_text_area = Text(odds_frame, height="20", width="30")
    odds_text_area.pack(side="top")
    final_odds_text_area = Text(odds_frame, height="5", width="30")
    final_odds_text_area.pack(side="bottom")
    input_frame = Frame(right_frame)
    input_frame.pack()
    money_label = Label(
        input_frame, text="How many dollars would you like to put in?", anchor="se"
    )
    money_label.pack()
    entry_amt = IntVar()
    dollar_entry = Entry(input_frame, textvariable=entry_amt)
    submit_button = Button(input_frame, text="Submit", width=7, command=submitBet)
    dollar_entry.pack(side="left")
    submit_button.pack(side="left")
    clear_button = Button(
        input_frame, text="Clear", width=7, command=lambda: clearChoices()
    )
    clear_button.pack(side="left")
    widgets.append(frame_title)
    widgets.append(odds_frame)
    widgets.append(odds_text_area)
    widgets.append(final_odds_text_area)
    widgets.append(input_frame)
    widgets.append(money_label)
    widgets.append(entry_amt)
    widgets.append(dollar_entry)
    widgets.append(submit_button)


def labelsButtons(root, csv_file):
    with open(csv_file, "r", encoding="utf-8") as file:
        read = csv.reader(file)
        next(read)
        # Add Labels and then packing and appending them to a list(widgets) so that they can be deleted later
        left_frame = Frame(root)
        right_frame = Frame(root)
        left_frame.pack(side=LEFT, fill=BOTH, expand=True)
        right_frame.pack(side=LEFT, fill=BOTH, expand=True)
        leftFrameWork(left_frame, read, root)
        rightFrameWork(right_frame)
        widgets.append(left_frame)
        widgets.append(right_frame)


# for debugging code to bypass login
main("test")
