import csv      #inbuilt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import re
from github import Github
from pathlib import Path
import os
import requests
from bs4 import BeautifulSoup
import unidecode
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

options = webdriver.FirefoxOptions()
	
# enable trace level for debugging 
options.log.level = "trace"

options.add_argument("-remote-debugging-port=9224")
options.add_argument("-headless")
options.add_argument("-disable-gpu")
options.add_argument("-no-sandbox")

binary = FirefoxBinary(os.environ.get('FIREFOX_BIN'))

driver = webdriver.Firefox(firefox_binary=binary,executable_path=os.environ.get('GECKODRIVER_PATH'),options=options)






#driver=webdriver.Chrome()

def push_to_github():
    g = Github('Enter GitHub Token here')
    repo = g.get_user().get_repo('efootball_player_files')
    all_files = []
    contents = repo.get_contents("")
    
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            file = file_content
            all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))
   

   
    git_file =f'{Path(__file__).stem}.csv'
    if git_file in all_files:
        contents = repo.get_contents(git_file)
        repo.delete_file(contents.path, f"Deleted{git_file}", contents.sha, branch="main")
        print(git_file + ' UPDATED')
        push_to_github()
    else:
        file=open('final_player_file.csv', 'r', encoding='utf-8')
        content = file.read()
        #print(content)
        repo.create_file(git_file, "committing files", content, branch="main")
        print(git_file + ' CREATED')



def main(url):
    driver.get(url)
    driver.find_element_by_xpath("//input[@id='levelRange']").send_keys(Keys.CONTROL, 'a')
    driver.find_element_by_xpath("//input[@id='levelRange']").send_keys(Keys.BACKSPACE)
    level_max=int(driver.find_element_by_xpath("//input[@id='levelRange']").get_attribute('max'))
    for x in range(level_max):
        driver.find_element_by_xpath("//input[@id='levelRange']").send_keys(Keys.ARROW_RIGHT)
    
    Offensive_Awareness=driver.find_element_by_xpath("//td[@id='offensiveAwarness']").text
    Ball_Control=driver.find_element_by_xpath("//td[@id='ballControl']").text
    Dribbling=driver.find_element_by_xpath("//td[@id='dribbling']").text
    Tight_Possession=driver.find_element_by_xpath("//td[@id='tightPossession']").text
    Low_Pass=driver.find_element_by_xpath("//td[@id='low_pass']").text
    Lofted_Pass=driver.find_element_by_xpath("//td[@id='lofted_pass']").text
    Finishing=driver.find_element_by_xpath("//td[@id='finishing']").text
    Heading=driver.find_element_by_xpath("//td[@id='header']").text
    Place_Kicking=driver.find_element_by_xpath("//td[@id='place_kicking']").text
    Curl=driver.find_element_by_xpath("//td[@id='swerve']").text

    Physical_Contact=driver.find_element_by_xpath("//td[@id='physical_contact']").text
    Defensive_Awareness=driver.find_element_by_xpath("//td[@id='def_prowess']").text
    Ball_Winning=driver.find_element_by_xpath("//td[@id='ball_winning']").text
    Aggression=driver.find_element_by_xpath("//td[@id='aggression']").text
    Goalkeeping=driver.find_element_by_xpath("//td[@id='aggression']").text
    GK_Catching=driver.find_element_by_xpath("//td[@id='catching']").text
    GK_Clearing=driver.find_element_by_xpath("//td[@id='clearing']").text
    GK_Reflexes=driver.find_element_by_xpath("//td[@id='reflexes']").text
    GK_Reach=driver.find_element_by_xpath("//td[@id='coverage']").text

    Jump=driver.find_element_by_xpath("//td[@id='jump']").text
    Balance=driver.find_element_by_xpath("//td[@id='balance']").text
    Stamina=driver.find_element_by_xpath("//td[@id='stamina']").text
    Speed=driver.find_element_by_xpath("//td[@id='speed']").text
    Acceleration=driver.find_element_by_xpath("//td[@id='explosive_power']").text
    Kicking_Power=driver.find_element_by_xpath("//td[@id='kicking_power']").text
    Weak_Foot_Usage=driver.find_elements_by_xpath("//td[@class='other-ability foot-ability']")[0].text
    Weak_Foot_Acc=driver.find_elements_by_xpath("//td[@class='other-ability foot-ability']")[1].text
    Form=driver.find_element_by_xpath("//td[@class='other-ability form-ability']").text
    Injury_Resistance=driver.find_element_by_xpath("//td[@class='other-ability injury-ability']").text

    
    skill_list, COM_skill_list=[], []
    for x in driver.find_elements_by_xpath("//label[@class='lbl-block']"):
        if(x.text!='' and 'COM SKILLS' not in x.find_element_by_xpath("./..").text):   
            skill_list.append(x.text)
        elif(x.text!='' and 'COM SKILLS' in x.find_element_by_xpath("./..").text):   
            re_outer = re.compile(r'([^A-Z ])([A-Z])')
            re_inner = re.compile(r'(?<!^)([A-Z])([^A-Z])')
            COM_skill_list.append(re_outer.sub(r'\1 \2', re_inner.sub(r' \1\2', x.text)))
    pos_rating_list=[]
    rgb_list=[]
    for x in driver.find_elements_by_xpath("//div[@class='overall-position']"):
        temp_rect_info=x.get_attribute('style')
        rgb=temp_rect_info[temp_rect_info.find('(')+1:temp_rect_info.find(')')]
        rgb_list.append(rgb.replace(' ','').split(','))
        
        pos_rating_list.append(x.text)
    return [skill_list, COM_skill_list, pos_rating_list, rgb_list, Offensive_Awareness,    Ball_Control,    Dribbling,    Tight_Possession,    Low_Pass,    Lofted_Pass,    Finishing,    Heading,    Place_Kicking, Curl,    Physical_Contact,    Defensive_Awareness,    Ball_Winning,    Aggression,    Goalkeeping,    GK_Catching,    GK_Clearing,    GK_Reflexes,    GK_Reach,    Jump,    Balance,    Stamina,    Speed,    Acceleration,    Kicking_Power,    Weak_Foot_Usage,    Weak_Foot_Acc,    Form,    Injury_Resistance]




def get_player_links():
    temp=[]
    pagecount=int(BeautifulSoup(requests.get(f'https://efootballhub.net/pes21/search/players').content, "html.parser").findAll('li', {'class':'page-item'})[-2].text)
    for page in range(pagecount+1):
        while True:
            try:
                url=f'https://efootballhub.net/pes21/search/players?page={page}'
                r=requests.get(url)
                soup=BeautifulSoup(r.content, "html.parser")
                all_button=soup.findAll('tr', {'role':'button'})
                print('Hello', page)
                if(len(all_button)==0): continue
            except: 
                print('Error')
                continue
            for x in all_button:
                player_code=x['onclick'][x['onclick'].rfind('/')+1:x['onclick'].rfind("'")]
                
                if(x.find('td', {'class':'headcol'})['style']=='background: linear-gradient(135deg, rgba(20, 20, 20, 1) 0%, rgba(218,182,28, 1) 20%, rgba(20, 20, 20, 1) 80%, rgba(20, 20, 20, 1) 100%);;'):
                    player_type='Legend'
                elif(x.find('td', {'class':'headcol'})['style']=='background: linear-gradient(135deg, rgba(20, 20, 20, 1) 0%, rgba(93,37,201, 1) 20%, rgba(20, 20, 20, 1) 80%, rgba(20, 20, 20, 1) 100%);;'):
                    player_type='Featured'
                elif(x.find('td', {'class':'headcol'})['style']=='background: linear-gradient(135deg, rgba(20, 20, 20, 1) 0%, rgba(237,37,96, 1) 20%, rgba(20, 20, 20, 1) 80%, rgba(20, 20, 20, 1) 100%);;'):
                    player_type='Iconic Moment'
                else: player_type='Base'
                
                #print(player_type)
                #print(player_code)
                form=x.find('div',{'class':'player-table-condition'}).text
                #print(form)
                name=unidecode.unidecode(x.find('span',{'class':'player-name'}).text)
                position=x.find('span', {'class':'player-position-playingstyle'}).text.split(' ')[0]
                playstyle=''
                for temp_playstyle in x.find('span', {'class':'player-position-playingstyle'}).text.split(' ')[1:]:
                    playstyle+=temp_playstyle+' '
                playstyle=playstyle[:-1]
                base_rating=x.find('div', {'class':'search-ability'}).text
                max_rating=x.find('div', {'class':'search-ability'}).find_next('td').text
                height=x.find('div', {'class':'search-ability'}).find_next('td').find_next('td').find_next('td').find_next('td').text
                weight=x.find('div', {'class':'search-ability'}).find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').text
                age=x.find('div', {'class':'search-ability'}).find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').find_next('td').text
                #print(name, position, playstyle, base_rating, max_rating, height, weight, age)
                temp.append([player_code, name, player_type, position, playstyle, form, base_rating, max_rating, height, weight, age])
                print(page)
                
            
            break      
        #temp.append([player_code, name, player_type, position, playstyle, form, base_rating, max_rating, height, weight, age])
    return temp







player_list=get_player_links()
w=open('player_code.csv', 'a', newline='')
writer1=csv.writer(w)
writer1.writerow(['Player Code', 'Name', 'Player Type', 'Position', 'Playstyle', 'Form', 'Base Rating', 'Max rating', 'Height', 'Weight', 'Age'])
for x in player_list:
    writer1.writerow(x)
w.close()




with open('player_code.csv',errors="ignore", newline='') as csvfile:
    player_list = list(csv.reader(csvfile, delimiter=','))[1:]


f = open('final_player_file.csv', 'a', newline='')
writer = csv.writer(f)
writer.writerow(['Player Code','Name','Player Type','Position','Playstyle','Form','Base Rating','Max rating','Height','Weight','Age', 'Skills', 'COM Skills', 'Pos Max Rating', 'RGB List', 'Offensive Awareness','Ball Control','Dribbling','Tight Possession','Low Pass','Lofted Pass','Finishing','Heading','Place Kicking','Curl','Physical Contact','Defensive Awareness','Ball Winning','Aggression','Goalkeeping','GK Catching','GK Clearing','GK Reflexes','GK Reach','Jump','Balance','Stamina','Speed','Acceleration','Kicking Power','Weak Foot Usage','Weak Foot Acc','Form','Injury Resistance'])

for x in player_list:  
    while True:
        try: temp_list=main(f'https://efootballhub.net/pes21/player/{x[0]}')
        except: continue
        y=x
        y.extend(temp_list)
        writer.writerow(y)
        break
f.close()
push_to_github()
driver.close()
