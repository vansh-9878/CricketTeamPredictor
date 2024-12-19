import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from joblib import load
import warnings
from sklearn.exceptions import InconsistentVersionWarning

def findBatsmen(n):
    df=pd.read_csv('batting.csv')
    try:
        df['HS']=df['HS'].str.split('*').str[0]
    except:
        a=1
    weights={'Matches':0.2,'Average': 0.2,'HS':0.1,'NO':0.2,'100s':0.2,'50s':0.1}
    scaler=MinMaxScaler()
    normalized_data = scaler.fit_transform(df[['Matches','Average', 'HS','NO','100s','50s']])
    df_normalized = pd.DataFrame(normalized_data, columns=['Matches', 'Average', 'HS','NO','100s','50s'])
    df['Weighted Score'] = (
        df_normalized['Matches'] * weights['Matches'] +
        df_normalized['Average'] * weights['Average'] +
        df_normalized['HS'] * weights['HS'] +
        df_normalized['NO'] * weights['NO'] +
        df_normalized['100s'] * weights['100s'] +
        df_normalized['50s'] * weights['50s']
    )
    batsmen=df.nlargest(n,'Weighted Score')
    bat=batsmen['Player'].to_numpy()
    return bat


def findBowler(n):
    df2=pd.read_csv('bowling.csv')
    df2['WpM']=df2['Wickets']/df2['Matches']
    weights2={'Matches':0.2,'Economy': 0.2,'WpM':0.4,'5w':0.2}
    scaler=MinMaxScaler()
    normalized_data2 = scaler.fit_transform(df2[['Matches','Economy','WpM','5w']])
    df_normalized2 = pd.DataFrame(normalized_data2, columns=['Matches','Economy','WpM','5w'])
    df_normalized2['Economy']=1-df_normalized2['Economy']
    df2['Weighted Score'] = (
        df_normalized2['Matches'] * weights2['Matches'] +
        df_normalized2['Economy'] * weights2['Economy'] +
        df_normalized2['WpM'] * weights2['WpM'] +
        df_normalized2['5w'] * weights2['5w']
    )
    bowlers=df2.nlargest(n,'Weighted Score')
    return bowlers['Player'].to_numpy()
    
    
def findAllrounder(n):
    df=pd.read_csv('allRounder.csv')
    try:
        df['HS']=df['HS'].str.split('*').str[0]
        df['Wickets']=df['Wickets'].str.split('*').str[0]
    except:
        a=0
        
    df['Wickets']=df['Wickets'].astype(int)
    # print(df['Wickets'])
    df['WpM']=df['Wickets']/df['Matches']
    weights={'Matches':0.05,'Average': 0.25,'100s':0.15,'50s':0.05,'Economy':0.15,'WpM':0.25,'5w':0.1}
    scaler=MinMaxScaler()
    normalized_data = scaler.fit_transform(df[['Matches','Average','100s','50s','Economy','WpM','5w']])
    df_normalized = pd.DataFrame(normalized_data, columns=['Matches', 'Average','100s','50s','Economy','WpM','5w'])
    df_normalized['Economy']=1-df_normalized['Economy']
    df['Weighted Score'] = (
        df_normalized['Matches'] * weights['Matches'] +
        df_normalized['Average'] * weights['Average'] +
        df_normalized['100s'] * weights['100s'] +
        df_normalized['Economy'] * weights['Economy'] +
        df_normalized['WpM'] * weights['WpM'] +
        df_normalized['5w'] * weights['5w'] 
    )
    allRounder=df.nlargest(n,'Weighted Score')
    middleOrder=allRounder['Player'].to_numpy()
    return middleOrder
    
    
def makeTeam(n1,n2,n3):
    top=findBatsmen(n1)
    bottom=findBowler(n2)
    middle=findAllrounder(n3)
    team=np.append(top,middle)
    team=np.append(team,bottom)
    return team



def predictTeam(venue,team1):
    code={
        'australia':'AUS',
        'india':'IND',
        'west':'WI',
        'bangladesh':'BAN',
        'south':'RSA',
        'pakistan':'PAK',
        'england':'ENG',
        'sri':'SL',
        'new':'NZ'
    }
    # print(code[venue],code[team1])
    # exit(0)
    new_match = pd.DataFrame({'Venue': [code[venue]], 'Team': [code[team1]]})
    df=pd.read_csv('teamData.csv')
    X=df[['Team','Venue']]
    X=pd.get_dummies(X)
    new_match = pd.get_dummies(new_match).reindex(columns=X.columns, fill_value=0)
    warnings.filterwarnings("ignore", category=InconsistentVersionWarning)
    loaded_model = load('teamPrediction.joblib')
    predictions = loaded_model.predict(new_match)
# print(predictions)
# predicted_batsmen = model.predict(new_match)
    team=makeTeam(predictions[0][0],predictions[0][1],predictions[0][2])
    return team

