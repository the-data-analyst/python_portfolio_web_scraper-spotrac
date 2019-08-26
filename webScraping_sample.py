import requests
import csv

from bs4 import BeautifulSoup
from csv import writer

response = requests.get ("https://www.spotrac.com/nfl/arizona-cardinals/cap/#").text

#pass contents of website using bs and convert to txt
soup = BeautifulSoup(response,"html.parser")

#use find all function to scrape positions in the table
players = soup.find_all("td", class_ = "player")
player_list = []
for player in players[0:54]:
    player_list.append(player.a.text)
    

#use find all function to scrape positions in the table
positions = soup.find_all("td", class_ = "center small") 
position_list = []
for position in positions[0:54]:
    position_list.append(position.text)
   
#use find all function to scrape salaries in the table
salaries = soup.find_all("td", class_ = "right xs-hide")


#create empty sal list 
#add salary to empty list
#loop and add elements to sal_list
sal = []
for salary in salaries:
 sal.append(salary.text)
 i = 0
 sal_list = []
 for s in sal:
  try:
   sal_list.append(sal[i])
   i +=7
  except:
   break

salary_list = []
for s in sal_list[0:54]:
    salary_list.append(s)
   
#create master list    
list_of_all = [player_list,position_list,salary_list]

#test list by printing contents
print (list_of_all)


#open csv file
#write to csv file
#create headers
#loop using writefow function   
with open ("salaryCap1.csv", "w") as csvFile:
    csv_writer = writer(csvFile)
    headers = ["Player","Position", "NFL Contract"]
    csv_writer.writerow (headers)
    for  i in range(53):
        csv_writer.writerow ([player_list[i],position_list[i],salary_list[i]])
        


   

   
    


