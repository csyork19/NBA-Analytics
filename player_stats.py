from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:/Users/csyor/Documents/NBA-Analytics/mozilla/geckodriver.exe")

driver.get('https://www.basketball-reference.com/teams/BRK/2022.html')
table = []
roster_table = driver.find_element_by_id('roster')
for row in roster_table.find_elements_by_tag()
