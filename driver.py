import requests
import pandas as pd
from bs4 import BeautifulSoup

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
    baseurl = "https://www.basketball-reference.com"
    team = selected_team
    url = 'https://www.basketball-reference.com/teams/'+str(team)+'/2022.html'
    response = requests.get(url)
    df_list = pd.read_html(response.text) # this parses all the tables in webpages to a list
    df = df_list[0]
    df = df.drop('No.', 1)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    print(df)

    # Prompt user to select a player from the roster
    user_nba_player = input("Please select a player from the roster above. Enter row number: \n")
    user_nba_player = df.loc[int(user_nba_player),"Player"]
    print(user_nba_player)

    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    results = soup.find_all('a')

    for tag in results:
        if tag.get_text() == user_nba_player:
            link = tag.get('href')
            baseurl += link
    file = open("urls/player_url.txt","w")
    file.write(baseurl)



def mainMenu():
    # Prompt user to select from the list of teams
    get_list_of_teams()
    user_nba_team = input("Please select a team from the list above: \n")

    # Get the abbriviation for the nba team
    get_list_of_team_abbrv()
    teams = get_abbreviation_for_user_nba_team(str(user_nba_team))

    # Print team roster
    get_team_roster("".join(teams.split()))

    # Execute the player_stats.py file after a player is selected
    exec(open("player_stats.py").read())



mainMenu()
