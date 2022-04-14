import requests
from bs4 import BeautifulSoup
import csv      #inbuilt
from selenium import webdriver
import unidecode

f = open('csv_file_managers.csv', 'a', newline='')
writer = csv.writer(f)
writer.writerow(['Manager Code', 'Name', 'Formation', 'Pos0', 'Pos1', 'Pos2', 'Pos3', 'Pos4', 'Pos5', 'Pos6', 'Pos7', 'Pos8', 'Pos9', 'Pos10', 'Management Skill', 'Cost GP', 'Attacking Style 0', 'Build Up 0', 'Attacking Area 0', 'Positioning 0', 'Support Range 0', 'Numbers in Attack 0', 'Defensive Style 0', 'Containment Area 0', 'Presurring 0', 'Defensive Line 0','Compactness 0', 'Numbers in Defense 0','Attacking Style 1', 'Build Up 1', 'Attacking Area 1', 'Positioning 1', 'Support Range 1', 'Numbers in Attack 1', 'Defensive Style 1', 'Containment Area 1', 'Presurring 1', 'Defensive Line 1','Compactness 1', 'Numbers in Defense 1'])


def get_param(url, param):
    driver.get(url)
    p_element = driver.find_element_by_xpath(f"//div[@id='supportRangeF{param}']")
    a=str(p_element.get_attribute('style'))

    p_element = driver.find_element_by_xpath(f"//div[@id='defensiveLineF{param}']")
    b=str(p_element.get_attribute('style'))

    p_element = driver.find_element_by_xpath(f"//div[@id='compactnessF{param}']")
    c=str(p_element.get_attribute('style'))

    return a[a.find('background-position: -')+22:a.find('%')-1], b[b.find('background-position: -')+22:b.find('%')-1],c[c.find('background-position: -')+22:c.find('%')-1] 

    
    
    
def get_links():
    temp=[]
    page_count=40
    for x in range(1,page_count):
        while True:
            page_url=f'https://efootballhub.net/pes21/search/coaches?page={x}'
            
        
            r=requests.get(page_url)
            soup=BeautifulSoup(r.content, "html.parser")

            data=soup.find('div',{'class':'d-flex justify-content-center flex-wrap cards-grid-container'})
            try:links=data.findAll('a')
            except: continue
            for link in links:
                manager_code=str(link['onclick'])[29:-3]
                name=unidecode.unidecode(link.find(['b']).text)
                formation=link.find('div',{'class':'formation'}).text.strip().replace('-','--')
                print(name)
                formation_parent=link.findAll('div',{'class':'position-image'})
                position_xy=[]
                for position in formation_parent:
                    bottom=float(position['style'][7:position['style'].find('px;')])*8.5+40
                    left=float(position['style'][position['style'].rfind('left:')+5:position['style'].rfind('px;')])*8.5
                    #print(bottom, left)
                    position_xy.append([bottom, left])
                temp1=[manager_code, name, formation]
                temp1.extend(position_xy)
                temp.append(temp1)
            break
    return temp
        


def get_tactics(temp, final_list=[]):
    manager_code=temp[0]
    page_url=f'https://efootballhub.net/pes21/coach/{manager_code}'
    r=requests.get(page_url)
    soup=BeautifulSoup(r.content, "html.parser")

    management_skill=soup.find('th',text='Management Skill').find_next('td').text
    cost_GP=soup.find('th',text='GP').find_next('td').text
    temp.extend([management_skill, cost_GP])


    for data in [soup.find('div',{'class':'coach-strategy-attack-container container-backgroud-colored'}), soup.find('div',{'class':'coach-strategy-defense-container container-backgroud-colored'})]:
        #print(data.find('tbody').text)
        Attacking_Style=data.find('th',text='Attacking Style').find_next('td').text
        Build_Up=data.find('th',text='Build Up').find_next('td').text
        Attacking_Area=data.find('th',text='Attacking Area').find_next('td').text
        Positioning=data.find('th',text='Positioning').find_next('td').text
        
        Numbers_in_Attack=data.find('th',text='Numbers in Attack').find_next('td').text
        Defensive_Style=data.find('th',text='Defensive Style').find_next('td').text
        Containment_Area=data.find('th',text='Containment Area').find_next('td').text
        Presurring=data.find('th',text='Pressuring').find_next('td').text
        
        Numbers_in_Defense=data.find('th',text='Numbers in Defense').find_next('td').text
        
        if('Offensive' in data.find('h4',{'class':'text-center pt-2'}).text):
            Support_Range,Defensive_Line,Compactness=get_param(page_url, '1')
            temp.extend([Attacking_Style, Build_Up, Attacking_Area, Positioning, Support_Range, Numbers_in_Attack, Defensive_Style, Containment_Area, Presurring, Defensive_Line,Compactness, Numbers_in_Defense])
        elif('Defensive' in data.find('h4',{'class':'text-center pt-2'}).text):
            Support_Range,Defensive_Line,Compactness=get_param(page_url, '2')
            temp.extend([Attacking_Style, Build_Up, Attacking_Area, Positioning, Support_Range, Numbers_in_Attack, Defensive_Style, Containment_Area, Presurring, Defensive_Line,Compactness, Numbers_in_Defense])

    writer.writerow(temp)
    final_list.append(temp)
    return final_list

final_list=[]


driver = webdriver.Chrome()
manager_list=get_links()
w=open('manager_code.csv', 'a', newline='')
writer1=csv.writer(w)
#writer1.writerow(['Manager Code', 'Name', 'Formation'])
writer1.writerow(['Manager Code', 'Name', 'Formation', 'Pos0', 'Pos1', 'Pos2', 'Pos3', 'Pos4', 'Pos5', 'Pos6', 'Pos7', 'Pos8', 'Pos9', 'Pos10'])
for x in manager_list:
    writer1.writerow(x)
w.close()
for x in manager_list:
    
    while True:
        print(x)
        try: final_list=get_tactics(x, final_list)
        except: continue
        break
for x in final_list:
    writer.writerow(x)
f.close()
driver.close()
