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

# store names and odds into variables for same
ravens = teams[0]
ravensSpread = spreads[0]
ravensSpreadOdds = spreadOdds[0]
ravensML = moneyline[0]
chiefs = teams[1]
chiefsSpread = spreads[2]
chiefsSpreadOdds = spreadOdds[1]
chiefsML = moneyline[1]

# write to a text file
with open("lines.txt", "w", newline="", encoding="utf-8") as txtfile:
    txtfile.write(ravens.text + " vs. " + chiefs.text + "\n")
    txtfile.write(
        ravens.text
        + ": "
        + ravensSpread.text
        + " -> "
        + ravensSpreadOdds.text
        + ", ML -> "
        + ravensML.text
        + "\n"
    )
    txtfile.write(
        chiefs.text
        + ": "
        + chiefsSpread.text
        + " -> "
        + chiefsSpreadOdds.text
        + ", ML -> "
        + chiefsML.text
        + "\n"
    )
# write to a csv file
with open("lines.csv", "w", newline="", encoding="utf-8") as csvfile:
    csvWriter = csv.writer(csvfile)
    # Writing the labels for each column
    csvWriter.writerow(["Away Team","Home Team","Away Team Spread", "Away Team Spread Odds", "Away Team ML", "Home Team Spread", "Home Team Spread Odds", "Home Team ML"])
    gameCounter=0
    while gameCounter<len(teams):
        # exampleList[gameCounter] is the example List of the away team and exampleList[gameCounter+1] is the home team
        csvWriter.writerow([
            teams[gameCounter].text,
            teams[gameCounter + 1].text,
            spreads[gameCounter].text,
            spreadOdds[gameCounter].text,
            moneyline[gameCounter].text,
            spreads[gameCounter + 1].text,
            spreadOdds[gameCounter + 1].text,
            moneyline[gameCounter + 1].text
        ])
        gameCounter+=2  # Incrementing by 2 to correctly index the next game


