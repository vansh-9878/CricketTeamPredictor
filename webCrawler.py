import requests
from bs4 import BeautifulSoup
import csv
    

url ="https://www.espncricinfo.com/series/australia-vs-india-2024-25-1426547/india-2nd-3rd-4th-and-5th-test-squad-1460697/series-squads"
# url ="https://www.espncricinfo.com/series/australia-vs-india-2024-25-1426547/australia-2nd-test-squad-1461795/series-squads"
# url="https://www.espncricinfo.com/series/south-africa-vs-pakistan-2024-25-1432205/south-africa-odi-squad-1464701/series-squads"
url2="https://www.espncricinfo.com"
# +"/cricketers/rohit-sharma-34102"

#format -> Tests=1, ODIs=2, T20Is=3

format=-1
url3=url.split("-")
if "tests" in url3 or "test" in url3:
    format=1
elif "ODIs" in url3 or "odi" in url3:
    format=2
elif "t20i" in url3 or "T20I" in url3:
    format=3

if format==-1:
    print("Error Encountered!!!")
    exit(0) 

# print(format)

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
team = soup.find_all('div',class_='ds-p-0')
# print(reviews[0])
team2=team[1].find_all('div',recursive=False)
# print(team[4])

def fetchBatsman(url2, team2,format):
    newData=[["Player","Matches","Innings","NO","Runs","HS","Average","BF","Sr","100s","50s","4s","6s","Ct","St"]]
    bat=team2[0].find('div',class_='ds-grid lg:ds-grid-cols-2').find_all('div',class_='ds-border-line odd:ds-border-r ds-border-b')
    for player in bat:
        name=player.find('div',class_='ds-relative ds-flex ds-flex-row ds-space-x-4 ds-p-3').find('div',class_='ds-popper-wrapper ds-inline').find('a')
    # print(name)
    # print("")
        href=name.get('href')
        playerName=href.split('/')[2].split('-')
        fullName=playerName[0]+" "+playerName[1]
    # print(fullName)
        url3=url2+href
        data2=''
        try:
            response2=requests.get(url3)
            soup2=BeautifulSoup(response2.content,"html.parser")
            data=soup2.find_all('tr')
            data2=data[format].find_all('td')                #change format
        except:
            print("Error occured skipping...")
            continue
        stats=[]
        count=0
        flag=0
        for imp in data2:
            if count==0:
                stats.append(fullName)
                count=count+1
            # print(imp.text.strip()=="FC")
                if imp.text.strip()=="FC":
                    flag=1
                continue
            stats.append(imp.text.strip())
        if flag==1:
        # print(stats)
            for i in range(len(stats)):
                try:
                    stats[i]=int(stats[i])/10
                except:
                    continue
        newData.append(stats)

# print(newData)

    with open('batting.csv','w',encoding='utf-8') as f:
        writer=csv.writer(f)
        writer.writerows(newData)
        print("data written..")



def fetchBowler(url2, team2,format):
    newData=[["Player","Matches","Innings","Balls","Runs","Wickets","BBI","BBM","Ave","Economy","SR","4w","5w","10w"]]
# print(team2[2])
    ball=team2[2].find('div',class_='ds-grid lg:ds-grid-cols-2').find_all('div',class_='ds-border-line odd:ds-border-r ds-border-b')
    for player in ball:
        name=player.find('div',class_='ds-relative ds-flex ds-flex-row ds-space-x-4 ds-p-3').find('div',class_='ds-popper-wrapper ds-inline').find('a')
    # print(name)
    # print("")
        href=name.get('href')
        playerName=href.split('/')[2].split('-')
        fullName=playerName[0]+" "+playerName[1]
    # print(fullName)
        url3=url2+href
        data2=''
        try:
            response2=requests.get(url3)
            soup2=BeautifulSoup(response2.content,"html.parser")
            data=soup2.find_all('tr')
            data2=data[format].find_all('td')
        except:
            print("Error occured skipping...")
            continue
        stats=[]
        count=0
        flag=0
        for imp in data2:
            if count==0:
                stats.append(fullName)
                if imp.text.strip()=="FC":
                    flag=1
                count=count+1
                continue
            stats.append(imp.text.strip())
        if flag==1:
            for i in range(len(stats)):
                try:
                    stats[i]=int(stats[i]/10)
                except:
                    continue
        newData.append(stats)
# print(newData)

    with open('bowling.csv','w',encoding='utf-8') as f:
        writer=csv.writer(f)
        writer.writerows(newData)
        print("data written")    
    
    
    

def fetchAllRounder(url2, team2,format):
    newData=[["Player","Matches","Innings","Balls","Runs","Wickets","BBI","BBM","Ave","Economy","SR","4w","5w","10w","Player","Matches2","Innings","NO","Runs","HS","Average","BF","Sr","100s","50s","4s","6s","Ct","St"]]

# print(team2)
    bat=team2[1].find('div',class_='ds-grid lg:ds-grid-cols-2').find_all('div',class_='ds-border-line odd:ds-border-r ds-border-b')
    for player in bat:
        name=player.find('div',class_='ds-relative ds-flex ds-flex-row ds-space-x-4 ds-p-3').find('div',class_='ds-popper-wrapper ds-inline').find('a')
    # print(name)
    # print("")
        href=name.get('href')
        playerName=href.split('/')[2].split('-')
        fullName=playerName[0]+" "+playerName[1]
    # print(fullName)
        url3=url2+href
        data2=''
        try:
            response2=requests.get(url3)
            soup2=BeautifulSoup(response2.content,"html.parser")
            data=soup2.find_all('tr')
            data2=data[format].find_all('td')
        except:
            print("Error occured skipping...")
            continue
        stats=[]
        count=0
        flag=0
        for imp in data2:
            if count==0:
                stats.append(fullName)
                count=count+1
            # print(imp.text.strip()=="FC")
                if imp.text.strip()=="FC":
                    flag=1
                continue
            stats.append(imp.text.strip())
        if flag==1:
        # print(stats)
            for i in range(len(stats)):
                try:
                    stats[i]=int(stats[i])/10
                except:
                    continue
            
    # print(data[8])
    # print()
    
        flag=0
        count=0
        try:
            data2=data[format+7].find_all('td')        #8
        # print(data2)
        except:
            print("Error occured skipping...")
            continue
    
        for imp in data2:
            if count==0:
                stats.append(fullName)
                count=count+1
            # print(imp.text.strip()=="FC")
                if imp.text.strip()=="FC":
                    flag=1
                continue
            stats.append(imp.text.strip())
        if flag==1:
        # print(stats)
            for i in range(len(stats)):
                try:
                    stats[i]=int(stats[i])/10
                except:
                    continue
    
    
    
        newData.append(stats)

# print(newData)

    with open('allRounder.csv','w',encoding='utf-8') as f:
        writer=csv.writer(f)
        writer.writerows(newData)
        print("data written..")


fetchBatsman(url2,team2,format)
fetchAllRounder(url2,team2,format)
fetchBowler(url2,team2,format)


