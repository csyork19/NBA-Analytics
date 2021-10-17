import requests
import pandas as pd

lines = []

def get_list_of_teams():
    print("NBA Teams")
    with open('files/nba_teams.txt','r') as file:
        count = -1
        for line in file:
            count +=1
            print(str(count) + ". " + line.strip())

def get_list_of_team_abbrv():
    with open('files/nba_teams_abbreviations.txt','r') as file:
        count = 0
        for line in file:
            count +=1

def get_abbreviation_for_user_nba_team(nba_team):
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

def get_team_roster(selected_team):
    team = selected_team
    url = 'https://www.basketball-reference.com/teams/'+str(team)+'/2022.html'
    response = requests.get(url)
    df_list = pd.read_html(response.text) # this parses all the tables in webpages to a list
    df = df_list[0]
    print(df)

def mainMenu():
    # Prompt user to select from the list of teams
    get_list_of_teams()
    user_nba_team = input("Please select a team from the list above: \n")

    # Get the abbriviation for the nba team
    get_list_of_team_abbrv()
    teams = get_abbreviation_for_user_nba_team(str(user_nba_team))

    # Print team roster
    get_team_roster("".join(teams.split()))

mainMenu()
