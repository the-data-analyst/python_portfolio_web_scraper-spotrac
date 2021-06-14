import requests
import csv
import time
from bs4 import BeautifulSoup
from csv import writer


from selenium.webdriver.support.ui import Select


#import selenium package
from selenium import webdriver
#set path for web driver download
PATH = "C:\Program Files (x86)\chromedriver.exe"
#set browser and
driver = webdriver.Chrome(PATH)

#go to website
driver.get("https://www.spotrac.com")
nfl_click = driver.find_element_by_link_text("NFL").click()
#wait
#time.sleep(2)


#click on Arizona Cardinal. Will make it a variable to loop through all teams
nfl_click = driver.find_element_by_link_text("Arizona Cardinals").click()


time.sleep(2)
#click on NFL team
s = Select(driver.find_element_by_xpath("//select[@name='team']"))

#click on
s.select_by_index(1)


#click on update button
s = driver.find_element_by_class_name("go").click()

# response = requests.get('https://www.spotrac.com/nfl/arizona-cardinals/cap/#').text

# pass contents of website using bs and convert to txt
soup = BeautifulSoup(response, "html.parser")


def get_team_names():
    response = requests.get('https://www.spotrac.com/nfl/arizona-cardinals/cap/#').text
    soup = BeautifulSoup(response, "html.parser")
    teams = soup.select("[class = table-filter] option[value]")
    team_list = []

    for team in teams:
        if len(team.text) > 10:
            team_list.append(team.text)

    return team_list

my_team_list = get_team_names()


# use find all function to scrape positions in the spotrac table
def get_players():
    response = requests.get('https://www.spotrac.com/nfl/arizona-cardinals/cap/#').text
    soup = BeautifulSoup(response, "html.parser")
    players = soup.find_all("td", class_="player")
    player_list = []
    for player in players[0:54]:
        player_list.append(player.a.text)

    return player_list

# use find all function to scrape positions in the spotrac table
def get_postions():
    soup = BeautifulSoup(response, "html.parser")
    positions = soup.find_all("td", class_="center small")
    position_list = []
    for position in positions[0:54]:
        position_list.append(position.text)

    return position_list

# use find all function to scrape salaries in the spotrac table
salaries = soup.find_all("td", class_ = "right result xs-hide")

# create empty sal list
# add salary to empty list
# loop and add elements to sal_list
#print(f'this is salaries: {salaries}')

sal = []
sal_list = []
for salary in salaries:
    sal.append(salary.text)
    i = 0
    sal_list = []
    for s in sal:
        try:
            sal_list.append(sal[i])
            i += 7
        except:
            break
salary_list = []
print(F"this is sal: {sal}")
for s in sal_list[0:57]:
    salary_list.append(s)
print(F"this is sal_list: {sal_list}")
# create master list
# create master list of all player data
#list_of_all = [player_list, position_list, sal_list]


# test list by printing contents
#print(f"list_of_all contents: {list_of_all}")
##@ @


##-59, 7 + 59, 7 @ @
# loop using writefow function
with open("salaryCap1.csvA", "w") as csvFile:
    csv_writer = writer(csvFile)
    headers = ["Player", "Position", "NFL Contract"]
    csv_writer.writerow(headers)
    for i in range(50):
        csv_writer.writerow([player_list[i], position_list[i], sal[i]])
        # for i in range(57):
        #     csv_writer.writerow([player_list[i], position_list[i], sal[i]])