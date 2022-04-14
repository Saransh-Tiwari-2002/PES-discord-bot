import requests
from bs4 import BeautifulSoup
import csv
import os

def create_potw_pack():
    try: os.remove('Latest_featured_players.csv')
    except: pass
    with open('player_file.csv',errors="ignore", newline='') as csvfile:
        spamreader = list(csv.reader(csvfile, delimiter=','))

    f = open('Latest_featured_players.csv', 'a', newline='')
    writer = csv.writer(f)
    writer.writerow(['Player Code','Name','Player Type','Position','Playstyle','Form','Base Rating','Max rating','Height','Weight','Age', 'Skills', 'COM Skills', 'Pos Max Rating', 'RGB List', 'Offensive Awareness','Ball Control','Dribbling','Tight Possession','Low Pass','Lofted Pass','Finishing','Heading','Place Kicking','Curl','Physical Contact','Defensive Awareness','Ball Winning','Aggression','Goalkeeping','GK Catching','GK Clearing','GK Reflexes','GK Reach','Jump','Balance','Stamina','Speed','Acceleration','Kicking Power','Weak Foot Usage','Weak Foot Acc','Form','Injury Resistance'])

    url=f'https://efootballhub.net/pes21'
    r=requests.get(url)
    soup=BeautifulSoup(r.content, "html.parser")
    data=soup.find('div', {'class':'featured-players-container'}).findAll('div', {'class':'player-image-parent'})

    for div in data:
        #print(div.find('div',{'class':'player-image-position'}).text)
        #print(div.find('span',{'id':'overall'}).text)
        #print(div.find('div',{'class':'player-image-potential'}).text)
        #print(div.find('div',{'class':'player-image-name'}).text)
        player_code=div.find('img', {'class':'player-image'})["src"]
        player_code=player_code[player_code.rfind('/')+1:player_code.find('_')]
        for x in spamreader:
            if(x[0]==player_code):
                writer.writerow(x)
                break
    f.close()
