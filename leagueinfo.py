from datetime import date

currentYear = date.today().year


class League:

    def __init__(self, name, startYear, endYear=currentYear, earlySeason="Spring_Season", lateSeason="Summer_Season"):
        self.name = name
        self.startYear = startYear
        self.endYear = endYear
        self.earlySeason = earlySeason
        self.lateSeason = lateSeason

    def getSeason(self, i):
        if i == 1:
            return self.earlySeason
        else:
            return self.lateSeason


def buildLeagueList():
    leagueList = [League("NA_LCS", 2014, 2018), League("LCS", 2019), League("EU_LCS", 2014, 2018), League("LEC", 2019),
                  League("LCK", 2016), League("LPL", 2013),
                  League("CBLOL", 2015, earlySeason="Split_1", lateSeason="Split_2"), League("LCL", 2016),
                  League("LJL", 2016), League("LLA", 2019, earlySeason="Opening_Season", lateSeason="Closing_Season"),
                  League("OPL", 2015, earlySeason="Split_1", lateSeason="Split_2"), League("PCS", 2020),
                  League("TCL", 2015, earlySeason="Winter_Season"), League("VCS", 2018), League("LMS", 2015, 2019)]

    return leagueList
# I've opted not to include LST this time around since data is very difficult to retrieve from the wiki about players.
