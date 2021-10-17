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
count = 0

def get_dictionary_of_player_stats(category,complete_player_stats,dict):
    print(dict)
    print(complete_player_stats)
    print(category)

    index = 0
    for i in category:
        if index < 2:
            for j in complete_player_stats[0:1]:
                print ("inside loop")
                print("index is " + str(index))
                value = complete_player_stats[index]
                dict[i] = dict.get(i,[]).append(value)
                index += 1


    print(dict)

    #for i in category, complete_player_stats:
        #i = i.strip()
        #index = 0
        #if index < 2:
            #dict[i] = complete_player_stats[i]

for stats in results:
    #player_stats = ' '.join(stats.text.split())
    #print(player_stats)
    list = []
    player_stats = []
    dict = {}
    season_stats = []
    career_stats = []
    #player_stats = stats.get_text().strip()
    divs = stats.find_all('strong')
    stat = stats.find_all('p')

    for item in divs:
        list.append(item.text.strip())
        item = item.text.strip()
        dict[item] = None

    #print("Size of "+ str(len(stats)))
    for item in stat:

        print("The index is " + str(count))

        if count % 2 == 0:
            print(item.text.strip())
            season_stats.append(item.text.strip())
            count += 1
            print ("The index count is even " + str(count))
        else:
            print ("The index count is odd " + str(count))
            career_stats.append(item.text.strip())
            count += 1
        #player_stats.append(item.text.strip())


    #print(list)
    #print(player_stats)
    #print(dict)

    #get_dictionary_of_player_stats(list,player_stats,dict)

    print ("The season stats are")
    print(season_stats)
    print("The career stats are")
    print(career_stats)
