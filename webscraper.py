from selenium import webdriver
from bs4 import BeautifulSoup
from leagueinfo import *
# import pandas as pd

driver = webdriver.Chrome()

currentYear = date.today().year
currentMonth = date.today().month

leagueList = buildLeagueList()

players = []
# kdas = []

selectedLeague = selectedYear = selectedSeason = 0

print("Names of currently supported leagues are:\nNA_LCS, LCS, EU_LCS, LEC, LCK, LPL, CBLOL, LCL, LJL, LLA, OPL, PCS, TCL, VCS, LMS")

inputStatus = 0

while inputStatus == 0:

    leagueName = input("Enter the name of the desired league: ")
    
    selectedLeague = next((league for league in leagueList if league.name == leagueName), None)
    if selectedLeague is None:
        print("Invalid league name entered.")
        continue

    selectedYear = input("Enter the desired year: ")
    if int(selectedYear) < selectedLeague.startYear or int(selectedYear) > selectedLeague.endYear:
        print("Invalid year entered.")
        continue

    selectedSeason = input("Enter 1 for the first season of the year or 2 for the second season of the year: ")
    if selectedLeague.endYear == currentYear and currentMonth < 6 and selectedSeason == 2:
        print("Invalid season entered.")
        continue

    inputStatus = 1

driver.get("https://lol.gamepedia.com/" + selectedLeague.name + "/" + selectedYear + "_Season/" +
           selectedLeague.getSeason(selectedSeason) + "/Player_Statistics")

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
# for a in soup.find_all("td"):
#    player = a.find("a", attrs={"class": "catlink-players"})
#    players.append(player.text)
playerList = soup.find_all("a", attrs={"class": "catlink-players"})
for player in playerList:
    players.append(player.getText().split('\n')[0])

print(players)
