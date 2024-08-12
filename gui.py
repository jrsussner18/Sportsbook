from tkinter import *
import csv

root = Tk()
root.geometry('750x350')

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


# def userInput():
#     global week
#     week = int(user_input.get())

widgets = []

def change(selection):
    global test
    test = selection
    clear_widgets()
    labels_buttons(root, "lines.csv")
    
def clear_widgets():
    """Clear the widgets from the window."""
    for widget in widgets:
        widget.pack_forget()
    widgets.clear()

options=["Week 1", "Week 2", "Week 3", 
         "Week 4", "Week 5", "Week 6", 
         "Week 7", "Week 8", "Week 9", 
         "Week 10", "Week 11", "Week 12", 
         "Week 13", "Week 14", "Week 15",
         "Week 16", "Week 17", "Week 18"]
clicked=StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=change)
drop.pack()


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
