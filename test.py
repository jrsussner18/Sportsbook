# Jake Sussner
# Sample of what scraping odds might be


# import libraries
import csv
from bs4 import BeautifulSoup
import requests

# get webbage and initialize script to scrape it
webPage = requests.get("https://sportsbook.draftkings.com/leagues/football/nfl")
soup = BeautifulSoup(webPage.text, "html.parser")

# find and store all of the teams, spreads, and odds on page
teams = soup.find_all("div", class_="event-cell__name-text")
# spreads also grabs O/U
spreads = soup.find_all("span", class_="sportsbook-outcome-cell__line")
spreadOdds = soup.find_all("span", class_="sportsbook-odds american default-color")
moneyline = soup.find_all(
    "span", class_="sportsbook-odds american no-margin default-color"
)


# write to a csv file
with open("lines.csv", "w", newline="", encoding="utf-8") as csvfile:
    csvWriter = csv.writer(csvfile)
    # Writing the labels for each column
    csvWriter.writerow(
        [
            "Away Team",
            "Home Team",
            "Away Team Spread",
            "Away Team Spread Odds",
            "Away Team ML",
            "Home Team Spread",
            "Home Team Spread Odds",
            "Home Team ML",
            "Week"
        ]
    )
    gameCounter = 0
    week=1
    weekArray=[30,62,94,126,154,182,212,244,274,302,330,356,388,414,446,478,510,542]
    while gameCounter < len(teams):
        # exampleList[gameCounter] is the example List of the away team and exampleList[gameCounter+1] is the home team
        csvWriter.writerow(
            [
                teams[gameCounter].text,
                teams[gameCounter + 1].text,
                spreads[gameCounter].text,
                spreadOdds[gameCounter].text,
                moneyline[gameCounter].text,
                spreads[gameCounter + 1].text,
                spreadOdds[gameCounter + 2].text,
                moneyline[gameCounter + 1].text,
                week
            ]
        )
        if gameCounter in weekArray:
            week+=1
        gameCounter += 2  # Incrementing by 2 to correctly index the next game
