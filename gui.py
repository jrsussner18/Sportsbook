from tkinter import *
import csv

root = Tk()

def labels_buttons(root, csv_file):
    with open(csv_file, "r") as file:
        read = csv.reader(file)
        next(read)
        for index, row in enumerate(read):
            #Need help here, I have index set to 0 but this is where I would like to generate user input
            if index == game:
                ravens = Label(root, text=row[0]).grid(row=1, column=0, sticky=W)
                cheifs = Label(root, text=row[1]).grid(row=2, column=0, sticky=W)
                spread_away = Button(root, text=row[2]).grid(row=1, column=1)
                spread_odds_away = Button(root, text=row[3]).grid(row=1, column=2)
                ml_away = Button(root, text=row[4]).grid(row=1, column=3)
                spread_home = Button(root, text=row[5]).grid(row=2, column=1)
                spread_odds_home = Button(root, text=row[6]).grid(row=2, column=2)
                ml_home = Button(root, text=row[7]).grid(row=2, column=3)


question=Label(root, text="What game do you want to bet on?").grid(row=10, column=0, sticky=W)
user_input = Entry(root, width=25).grid(row=10, column=2, sticky=W)
submit = Button(root, text="Submit").grid(row=10, column=3)

teams_title = Label(root, text="Teams").grid(row=0, column=0, sticky=W)
spread_title = Label(root, text="Spread", width=10).grid(row=0, column=1)
spread_odds_title = Label(root, text="Spread odds", width=10).grid(row=0, column=2)
ml_title = Label(root, text="Money line", width=10).grid(row=0, column=3)



labels_buttons(root, 'lines.csv')

root.mainloop()