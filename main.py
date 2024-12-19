from webCrawler import start
from predict import predictTeam

def guessWhat():
    # link=input("Enter the squad link from www.espncricinfo.com : ")
    link='https://www.espncricinfo.com/series/australia-vs-india-2024-25-1426547/india-2nd-3rd-4th-and-5th-test-squad-1460697/series-squads'
    print()
    start(link)
    
    team=predictTeam()
    for i in range(len(team)):
        print(i+1,team[i])
    
    

guessWhat()
