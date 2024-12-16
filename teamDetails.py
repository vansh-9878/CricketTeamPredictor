import requests
from bs4 import BeautifulSoup
import csv



def getData(team):
    teamNames=team.find_all('a')
    # print(team)
    # return 0
# print(teamNames[0].text.strip())

    batters=0
    bowlers=0
    allRounders=0

    team1=team.find('div',class_='cb-col cb-col-50 cb-play11-lft-col')

    players=team1.find_all('div',class_='cb-col cb-col-100')

    for player in players:
        role=player.find('span',class_='cb-font-12 text-gray')
    # print(role.text)
        roleArray=role.text.strip().split("-")
    
        if "Batter" in roleArray:
            batters+=1
        elif "Bowler" in roleArray:
            bowlers+=1
        elif "Bowling Allrounder" in roleArray or "Batting Allrounder" in roleArray:
            allRounders+=1

# print(batters,bowlers,allRounders)
    stats=[]
    stats1=[teamNames[0].text.strip(),teamNames[0].text.strip(),batters,bowlers,allRounders]
    stats.append(stats1)

# team2
    batters=0
    bowlers=0
    allRounders=0
    team1=team.find('div',class_='cb-col cb-col-50 cb-play11-rt-col')

    players=team1.find_all('div',class_='cb-col cb-col-100')

    for player in players:
        role=player.find('span',class_='cb-font-12 text-gray')
    # print(role.text)
        roleArray=role.text.strip().split("-")
    
        if "Batter" in roleArray:
            batters+=1
        elif "Bowler" in roleArray:
            bowlers+=1
        elif "Bowling Allrounder" in roleArray or "Batting Allrounder" in roleArray:
            allRounders+=1

# print(batters,bowlers,allRounders)

    stats1=[teamNames[1].text.strip(),teamNames[0].text.strip(),batters,bowlers,allRounders]
    stats.append(stats1)

# print(stats)

    with open("teamData.csv",'a',encoding='utf-8') as f:
        writer=csv.writer(f)
        writer.writerows(stats)
        print("data Written...")



urls=[ 
            
      ]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    team = soup.find('div',class_='cb-col cb-col-100 cb-bg-white').find('div',class_='cb-col cb-col-67 cb-sqds-lft-col html-refresh')
    # print(team)
    getData(team)
    
