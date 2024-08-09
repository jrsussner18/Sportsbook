from tkinter import *
root = Tk()

teams_title = Label(root, text="Teams").grid(row=0, column=0, sticky=W)
spread_title = Label(root, text="Spread", width=10).grid(row=0, column=1)
spread_odds_title = Label(root, text="Spread odds", width=10).grid(row=0, column=2)
ml_title = Label(root, text="Money line", width=10).grid(row=0, column=3)

ravens = Label(root, text="BAL Ravens").grid(row=1, column=0, sticky=W)
cheifs = Label(root, text="KC Cheifs").grid(row=2, column=0, sticky=W)

spread_away = Button(root, text="+3").grid(row=1, column=1)
spread_odds_away = Button(root, text="-118").grid(row=1, column=2)
ml_away = Button(root, text="+124").grid(row=1, column=3)

spread_home = Button(root, text="46.5").grid(row=2, column=1)
spread_odds_home = Button(root, text="-108").grid(row=2, column=2)
ml_home = Button(root, text="-148").grid(row=2, column=3)

root.mainloop()