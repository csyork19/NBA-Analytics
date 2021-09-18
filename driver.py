import requests
import pandas as pd

lines = []

def addTeamsToList():
    with open('files/nba_teams_abbreviations.txt','r') as file:
        count = 0
        for line in file:
            line = line.strip()
            lines.append(line)

def getListOfTeams():
    print("NBA Teams")
    with open('files/nba_teams.txt','r') as file:
        count = -1
        for line in file:
            count +=1
            print(str(count) + ". " + line.strip())

def getListOfTeamAbbrv():
    with open('files/nba_teams_abbreviations.txt','r') as file:
        count = 0
        for line in file:
            count +=1

def getAbbreviationForUserNbaTeam(nba_team):
    abbr_line_count = 0
    with open('files/nba_teams.txt','r') as file:
        count = 0
        for line in file:
            if count == int(nba_team):
                abbr_line_count = count
            count +=1

    with open('files/nba_teams_abbreviations.txt','r') as file:
        count = 0
        for line in file:
            if count == abbr_line_count:
                return str(line)
            count +=1

def getTeamRoster(selected_team):
    team = selected_team
    url = 'https://www.basketball-reference.com/teams/'+str(team)+'/2022.html'
    response = requests.get(url)
    df_list = pd.read_html(response.text) # this parses all the tables in webpages to a list
    df = df_list[0]
    print(df)

def mainMenu():
    # Prompt user to select from the list of teams
    getListOfTeams()
    user_nba_team = input("Please select a team from the list above: \n")

    # Get the abbriviation for the nba team
    getListOfTeamAbbrv()
    teams = getAbbreviationForUserNbaTeam(str(user_nba_team))

    # Print team roster
    getTeamRoster("".join(teams.split()))

mainMenu()
