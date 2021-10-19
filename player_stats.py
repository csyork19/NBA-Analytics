import requests
from bs4 import BeautifulSoup
import pandas as pd


url = None
with open('urls/player_url.txt','r') as file:
    for line in file:
        url = line
        str(url)

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

# Games, PTS, TRB, AST
results = soup.find_all("div", attrs={'class':'p1'})

# FG, FG3%, FT%, eFG%
results1 = soup.find_all("div", attrs={'class':'p2'})

# PER, WS
results2 = soup.find_all("div", attrs={'class':'p3'})

stats_cols = ['Summary','Games', 'PTS','TRB', 'AST', 'FG%', 'FG3%', 'FT%', 'eFG%', 'PER', 'WS']
season_stats = ['Season']
career_stats = ['Career']
complete_stats = []
count = 0

for stats in results:
    list = []
    divs = stats.find_all('strong')
    stat = stats.find_all('p')

    for item in divs:
        list.append(item.text.strip())
        item = item.text.strip()

    for item in stat:
        if count % 2 == 0:
            season_stats.append(item.text.strip())
            count += 1
        else:
            career_stats.append(item.text.strip())
            count += 1

for stats in results1:
    list = []
    divs = stats.find_all('strong')
    stat = stats.find_all('p')

    for item in divs:
        list.append(item.text.strip())
        item = item.text.strip()

    for item in stat:
        if count % 2 == 0:
            season_stats.append(item.text.strip())
            count += 1
        else:
            career_stats.append(item.text.strip())
            count += 1

for stats in results2:
    list = []
    divs = stats.find_all('strong')
    stat = stats.find_all('p')

    for item in divs:
        list.append(item.text.strip())
        item = item.text.strip()

    for item in stat:
        if count % 2 == 0:
            season_stats.append(item.text.strip())
            count += 1
        else:
            career_stats.append(item.text.strip())
            count += 1

    complete_stats.append(season_stats)
    complete_stats.append(career_stats)

df = pd.DataFrame(complete_stats, columns = stats_cols)
print(df)
