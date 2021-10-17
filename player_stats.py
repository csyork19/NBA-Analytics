#from selenium import webdriver

#driver = webdriver.Firefox(executable_path="C:/Users/csyor/Documents/NBA-Analytics/mozilla/geckodriver.exe")

#driver.get('https://www.basketball-reference.com/teams/BRK/2022.html')
#table = []
#roster_table = driver.find_element_by_id('roster')
#for row in roster_table.find_elements_by_tag('tbody'):

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.basketball-reference.com/players/i/irvinky01.html'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

# Games, PTS, TRB, AST
results = soup.find_all("div", attrs={'class':'p1'})
stats_cols = ['Games', 'PTS','TRB', 'AST', 'FG%', 'FG3%', 'FT%', 'eFG%', 'PER', 'WS']

# FG, FG3%, FT%, eFG%
results1 = soup.find_all("div", attrs={'class':'p2'})

# PER, WS
results2 = soup.find_all("div", attrs={'class':'p3'})



for stats in results:
    #player_stats = ' '.join(stats.text.split())
    #print(player_stats)
    list = []
    player_stats = []
    #player_stats = stats.get_text().strip()
    divs = stats.find_all('strong')
    stat = stats.find_all('p')

    for item in divs:
        list.append(item.text.strip())

    for item in stat:
        player_stats.append(item.text.strip())
    #print("Size of "+ str(len(stats)))
    print(list)
    print(player_stats)

for stats1 in results1:
    #player_stats = ' '.join(stats.text.split())
    #print(player_stats)
    list = []
    player_stats = []
    #player_stats = stats.get_text().strip()
    divs = stats1.find_all('strong')
    stat = stats1.find_all('p')

    for item in divs:
        list.append(item.text.strip())

    for item in stat:
        player_stats.append(item.text.strip())
    #print("Size of "+ str(len(stats)))
    print(list)
    print(player_stats)

for stats2 in results2:
    #player_stats = ' '.join(stats.text.split())
    #print(player_stats)
    list = []
    player_stats = []
    #player_stats = stats.get_text().strip()
    divs = stats2.find_all('strong')
    stat = stats2.find_all('p')

    for item in divs:
        list.append(item.text.strip())

    for item in stat:
        player_stats.append(item.text.strip())
    #print("Size of "+ str(len(stats)))
    print(list)
    print(player_stats)
