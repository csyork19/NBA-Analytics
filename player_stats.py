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

results = soup.find_all("div", attrs={'class':'stats_pullout'})
stats_cols = ['Games', 'PTS','TRB', 'AST', 'FG%', 'FG3%', 'FT%', 'eFG%', 'PER', 'WS']


for stats in results:
    #player_stats = ' '.join(stats.text.split())
    #print(player_stats)
    player_stats = stats.get_text().strip()
    #print("Size of "+ str(len(stats)))
    print(player_stats)
