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



urls=['https://www.cricbuzz.com/cricket-match-squads/32047/eng-vs-ind-1st-test-india-tour-of-england-2021',
      'https://www.cricbuzz.com/cricket-match-squads/32052/eng-vs-ind-2nd-test-india-tour-of-england-2021',
      'https://www.cricbuzz.com/cricket-match-squads/32058/eng-vs-ind-4th-test-india-tour-of-england-2021',
      'https://www.cricbuzz.com/cricket-match-squads/78551/ind-vs-aus-1st-odi-australia-tour-of-india-2023',
      'https://www.cricbuzz.com/cricket-match-squads/78558/ind-vs-aus-2nd-odi-australia-tour-of-india-2023',
      'https://www.cricbuzz.com/cricket-match-squads/53350/eng-vs-aus-1st-test-the-ashes-2023',
      'https://www.cricbuzz.com/cricket-match-squads/53352/eng-vs-aus-2nd-test-the-ashes-2023'
     ]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    team = soup.find('div',class_='cb-col cb-col-100 cb-bg-white').find('div',class_='cb-col cb-col-67 cb-sqds-lft-col html-refresh')
    # print(team)
    getData(team)
    
    
    
# "https://www.cricbuzz.com/cricket-match-squads/92408/nz-vs-eng-3rd-test-england-tour-of-new-zealand-2024",
#      'https://www.cricbuzz.com/cricket-match-squads/94336/rsa-vs-pak-3rd-t20i-pakistan-tour-of-south-africa-2024-25',
#      'https://www.cricbuzz.com/cricket-match-squads/91778/aus-vs-ind-1st-test-india-tour-of-australia-2024-25',
#      'https://www.cricbuzz.com/cricket-match-squads/100274/ind-vs-nz-3rd-test-new-zealand-tour-of-india-2024',
    #   'https://www.cricbuzz.com/cricket-match-squads/94404/rsa-vs-sl-1st-test-sri-lanka-tour-of-south-africa-2024',
    #   'https://www.cricbuzz.com/cricket-match-squads/108425/ban-vs-rsa-2nd-test-south-africa-tour-of-bangladesh-2024',
    #   'https://www.cricbuzz.com/cricket-match-squads/94327/rsa-vs-pak-1st-t20i-pakistan-tour-of-south-africa-2024-25',
    #   'https://www.cricbuzz.com/cricket-match-squads/94426/rsa-vs-sl-2nd-test-sri-lanka-tour-of-south-africa-2024',
    #        'https://www.cricbuzz.com/cricket-match-squads/100272/ind-vs-nz-2nd-test-new-zealand-tour-of-india-2024',
    # 'https://www.cricbuzz.com/cricket-match-squads/76570/eng-vs-aus-4th-odi-australia-tour-of-england-2024'
# 'https://www.cricbuzz.com/cricket-match-squads/95187/wi-vs-eng-3rd-t20i-england-tour-of-west-indies-2024',
# "https://www.cricbuzz.com/cricket-match-squads/95178/wi-vs-eng-2nd-t20i-england-tour-of-west-indies-2024",
# 'https://www.cricbuzz.com/cricket-match-squads/95160/wi-vs-eng-3rd-odi-england-tour-of-west-indies-2024',
#      'https://www.cricbuzz.com/cricket-match-squads/100265/ind-vs-nz-1st-test-new-zealand-tour-of-india-2024',
#          'https://www.cricbuzz.com/cricket-match-squads/92057/aus-vs-pak-3rd-t20i-pakistan-tour-of-australia-2024',
#      'https://www.cricbuzz.com/cricket-match-squads/92039/aus-vs-pak-1st-t20i-pakistan-tour-of-australia-2024',
#      'https://www.cricbuzz.com/cricket-match-squads/76577/eng-vs-aus-5th-odi-australia-tour-of-england-2024',


#  
