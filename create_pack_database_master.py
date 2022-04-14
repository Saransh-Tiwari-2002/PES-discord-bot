import csv
import os
def create_pack_database():
    try:
        os.remove('IM_players.csv')
        os.remove('Legend_players.csv')
    except: pass
    
    with open('player_file.csv',errors="ignore", newline='') as csvfile:
        spamreader = list(csv.reader(csvfile, delimiter=','))
        
    f = open('IM_players.csv', 'a', newline='')
    writer = csv.writer(f)
    writer.writerow(['Player Code','Name','Player Type','Position','Playstyle','Form','Base Rating','Max rating','Height','Weight','Age', 'Skills', 'COM Skills', 'Pos Max Rating', 'RGB List', 'Offensive Awareness','Ball Control','Dribbling','Tight Possession','Low Pass','Lofted Pass','Finishing','Heading','Place Kicking','Curl','Physical Contact','Defensive Awareness','Ball Winning','Aggression','Goalkeeping','GK Catching','GK Clearing','GK Reflexes','GK Reach','Jump','Balance','Stamina','Speed','Acceleration','Kicking Power','Weak Foot Usage','Weak Foot Acc','Form','Injury Resistance'])
    for x in spamreader:
        if(x[2]=='Iconic Moment'):
            writer.writerow(x)
    f.close()

    f = open('Legend_players.csv', 'a', newline='')
    writer = csv.writer(f)
    writer.writerow(['Player Code','Name','Player Type','Position','Playstyle','Form','Base Rating','Max rating','Height','Weight','Age', 'Skills', 'COM Skills', 'Pos Max Rating', 'RGB List', 'Offensive Awareness','Ball Control','Dribbling','Tight Possession','Low Pass','Lofted Pass','Finishing','Heading','Place Kicking','Curl','Physical Contact','Defensive Awareness','Ball Winning','Aggression','Goalkeeping','GK Catching','GK Clearing','GK Reflexes','GK Reach','Jump','Balance','Stamina','Speed','Acceleration','Kicking Power','Weak Foot Usage','Weak Foot Acc','Form','Injury Resistance'])
    for x in spamreader:
        if(x[2]=='Legend'):
            writer.writerow(x)
    f.close()
