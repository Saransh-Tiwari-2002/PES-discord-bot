import asyncio
import discord
import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import re
import random
from datetime import date
import json
import time
import unidecode
import difflib

cred_obj1 = firebase_admin.credentials.Certificate('FB_json.json')
app1 = firebase_admin.initialize_app(cred_obj1, {'databaseURL':'https://test2-b4778-default-rtdb.firebaseio.com/'})
ref1=db.reference('/')

cred_obj3 = firebase_admin.credentials.Certificate('IM.json')
app3 = firebase_admin.initialize_app(cred_obj3, {'databaseURL':'https://im-database-231bb-default-rtdb.firebaseio.com/'}, name='app3')
ref3=db.reference('/', app3)

cred_obj4 = firebase_admin.credentials.Certificate('legend.json')
app4 = firebase_admin.initialize_app(cred_obj4, {'databaseURL':'https://legend-database-default-rtdb.firebaseio.com/'}, name='app4')
ref4=db.reference('/', app4)

cred_obj_a = firebase_admin.credentials.Certificate('manager-01.json')
app_a = firebase_admin.initialize_app(cred_obj_a, {'databaseURL':'https://manager-01-8f694-default-rtdb.firebaseio.com/'}, name='app_a')
ref_a=db.reference('/', app_a)

cred_obj_b = firebase_admin.credentials.Certificate('manager-02.json')
app_b = firebase_admin.initialize_app(cred_obj_b, {'databaseURL':'https://manager-02-b9cf5-default-rtdb.firebaseio.com/'},name= 'app_b')
ref_b=db.reference('/', app_b)

cred_obj_c = firebase_admin.credentials.Certificate('manager-03.json')
app_c = firebase_admin.initialize_app(cred_obj_c, {'databaseURL':'https://manager-03-5df24-default-rtdb.firebaseio.com/'},name= 'app_c')
ref_c=db.reference('/', app_c)

cred_obj_d = firebase_admin.credentials.Certificate('manager-04.json')
app_d = firebase_admin.initialize_app(cred_obj_d, {'databaseURL':'https://manager-04-2da97-default-rtdb.firebaseio.com/'},name= 'app_d')
ref_d=db.reference('/', app_d)

cred_obj_e = firebase_admin.credentials.Certificate('manager-05.json')
app_e = firebase_admin.initialize_app(cred_obj_e, {'databaseURL':'https://manager-05-default-rtdb.firebaseio.com/'},name= 'app_e')
ref_e=db.reference('/', app_e)

cred_obj_f = firebase_admin.credentials.Certificate('manager-06.json')
app_f = firebase_admin.initialize_app(cred_obj_f, {'databaseURL':'https://manager-06-default-rtdb.firebaseio.com/'},name= 'app2_f')
ref_f=db.reference('/', app_f)

cred_obj_g = firebase_admin.credentials.Certificate('manager-07.json')
app_g = firebase_admin.initialize_app(cred_obj_g, {'databaseURL':'https://manager-07-default-rtdb.firebaseio.com/'},name= 'app_g')
ref_g=db.reference('/', app_g)

cred_obj_h = firebase_admin.credentials.Certificate('manager-08.json')
app_h = firebase_admin.initialize_app(cred_obj_h, {'databaseURL':'https://manager-08-default-rtdb.firebaseio.com/'},name= 'app_h')
ref_h=db.reference('/', app_h)

cred_obj_i = firebase_admin.credentials.Certificate('manager-09.json')
app_i = firebase_admin.initialize_app(cred_obj_i, {'databaseURL':'https://manager-09-default-rtdb.firebaseio.com/'},name= 'app_i')
ref_i=db.reference('/', app_i)

cred_obj_j = firebase_admin.credentials.Certificate('manager-10.json')
app_j = firebase_admin.initialize_app(cred_obj_j, {'databaseURL':'https://manager-10-424ea-default-rtdb.firebaseio.com/'},name= 'app_j')
ref_j=db.reference('/', app_j)

cred_obj_k = firebase_admin.credentials.Certificate('manager-11.json')
app_k = firebase_admin.initialize_app(cred_obj_k, {'databaseURL':'https://manager-11-4eda6-default-rtdb.firebaseio.com/'},name= 'app_k')
ref_k=db.reference('/', app_k)

cred_obj_l = firebase_admin.credentials.Certificate('manager-12.json')
app_l = firebase_admin.initialize_app(cred_obj_l, {'databaseURL':'https://manager-12-9cb36-default-rtdb.firebaseio.com/'},name= 'app_l')
ref_l=db.reference('/', app_l)

cred_obj_m = firebase_admin.credentials.Certificate('manager-13.json')
app_m = firebase_admin.initialize_app(cred_obj_m, {'databaseURL':'https://manager-13-de784-default-rtdb.firebaseio.com/'},name= 'app_m')
ref_m=db.reference('/', app_m)

cred_obj_n = firebase_admin.credentials.Certificate('manager-14.json')
app_n = firebase_admin.initialize_app(cred_obj_n, {'databaseURL':'https://manager-14-default-rtdb.firebaseio.com/'},name= 'app_n')
ref_n=db.reference('/', app_n)

cred_obj_o = firebase_admin.credentials.Certificate('manager-15.json')
app_o = firebase_admin.initialize_app(cred_obj_o, {'databaseURL':'https://manager-15-default-rtdb.firebaseio.com/'},name= 'app_o')
ref_o=db.reference('/', app_o)

cred_obj_p = firebase_admin.credentials.Certificate('manager-16.json')
app_p = firebase_admin.initialize_app(cred_obj_p, {'databaseURL':'https://manager-16-default-rtdb.firebaseio.com/'},name= 'app_p')
ref_p=db.reference('/', app_p)

cred_obj_q = firebase_admin.credentials.Certificate('manager-17.json')
app_q = firebase_admin.initialize_app(cred_obj_q, {'databaseURL':'https://manager-17-b5338-default-rtdb.firebaseio.com/'},name= 'app_q')
ref_q=db.reference('/', app_q)

cred_obj_r = firebase_admin.credentials.Certificate('manager-18.json')
app_r = firebase_admin.initialize_app(cred_obj_r, {'databaseURL':'https://manager-18-default-rtdb.firebaseio.com/'},name= 'app_r')
ref_r=db.reference('/', app_r)

cred_obj_s = firebase_admin.credentials.Certificate('manager-19.json')
app_s = firebase_admin.initialize_app(cred_obj_s, {'databaseURL':'https://manager-19-default-rtdb.firebaseio.com/'},name= 'app_s')
ref_s=db.reference('/', app_s)

cred_obj_t = firebase_admin.credentials.Certificate('manager-20.json')
app_t = firebase_admin.initialize_app(cred_obj_t, {'databaseURL':'https://manager-20-171d4-default-rtdb.firebaseio.com/'},name= 'app_t')
ref_t=db.reference('/', app_t)

cred_obj_u = firebase_admin.credentials.Certificate('manager-21.json')
app_u = firebase_admin.initialize_app(cred_obj_u, {'databaseURL':'https://manager-21-242e4-default-rtdb.firebaseio.com/'},name= 'app_u')
ref_u=db.reference('/', app_u)

cred_obj_v = firebase_admin.credentials.Certificate('manager-22.json')
app_v = firebase_admin.initialize_app(cred_obj_v, {'databaseURL':'https://manager-22-2254b-default-rtdb.firebaseio.com/'},name= 'app_v')
ref_v=db.reference('/', app_v)

cred_obj_w = firebase_admin.credentials.Certificate('manager-23.json')
app_w = firebase_admin.initialize_app(cred_obj_w, {'databaseURL':'https://manager-23-default-rtdb.firebaseio.com/'},name= 'app_w')
ref_w=db.reference('/', app_w)

cred_obj_x = firebase_admin.credentials.Certificate('manager-24.json')
app_x = firebase_admin.initialize_app(cred_obj_x, {'databaseURL':'https://manager-24-default-rtdb.firebaseio.com/'},name= 'app_x')
ref_x=db.reference('/', app_x)

cred_obj_y = firebase_admin.credentials.Certificate('manager-25.json')
app_y = firebase_admin.initialize_app(cred_obj_y, {'databaseURL':'https://manager-25-default-rtdb.firebaseio.com/'},name= 'app_y')
ref_y=db.reference('/', app_y)

cred_obj_z = firebase_admin.credentials.Certificate('manager-26.json')
app_z = firebase_admin.initialize_app(cred_obj_z, {'databaseURL':'https://manager-26-default-rtdb.firebaseio.com/'},name= 'app_z')
ref_z=db.reference('/', app_z)

cred_obj_backup= firebase_admin.credentials.Certificate('manager-27.json')
app_backup = firebase_admin.initialize_app(cred_obj_backup, {'databaseURL':'https://manager-27-default-rtdb.firebaseio.com/'}, name='app_backup')
ref_backup=db.reference('/', app_backup)

cred_obj_base1 = firebase_admin.credentials.Certificate('base1.json')
app_base1 = firebase_admin.initialize_app(cred_obj_base1, {'databaseURL':'https://base1-b1868-default-rtdb.firebaseio.com/'}, name='app_base1')
ref_base1=db.reference('/', app_base1)

cred_obj_base2 = firebase_admin.credentials.Certificate('base2.json')
app_base2 = firebase_admin.initialize_app(cred_obj_base2, {'databaseURL':'https://base2-9dff0-default-rtdb.firebaseio.com/'}, name='app_base2')
ref_base2=db.reference('/', app_base2)

cred_obj_base3 = firebase_admin.credentials.Certificate('base3.json')
app_base3 = firebase_admin.initialize_app(cred_obj_base3, {'databaseURL':'https://base3-787dc-default-rtdb.firebaseio.com/'}, name='app_base3')
ref_base3=db.reference('/', app_base3)

cred_obj_base4 = firebase_admin.credentials.Certificate('base4.json')
app_base4 = firebase_admin.initialize_app(cred_obj_base4, {'databaseURL':'https://base4-df4a8-default-rtdb.firebaseio.com/'}, name='app_base4')
ref_base4=db.reference('/', app_base4)

cred_obj_base5 = firebase_admin.credentials.Certificate('base5.json')
app_base5 = firebase_admin.initialize_app(cred_obj_base5, {'databaseURL':'https://base5-8ff5e-default-rtdb.firebaseio.com/'}, name='app_base5')
ref_base5=db.reference('/', app_base5)

cred_obj_base6 = firebase_admin.credentials.Certificate('base6.json')
app_base6 = firebase_admin.initialize_app(cred_obj_base6, {'databaseURL':'https://base6-7195f-default-rtdb.firebaseio.com/'}, name='app_base6')
ref_base6=db.reference('/', app_base6)

cred_obj_base7 = firebase_admin.credentials.Certificate('base7.json')
app_base7 = firebase_admin.initialize_app(cred_obj_base7, {'databaseURL':'https://base7-97169-default-rtdb.firebaseio.com/'}, name='app_base7')
ref_base7=db.reference('/', app_base7)

cred_obj_base8 = firebase_admin.credentials.Certificate('base8.json')
app_base8 = firebase_admin.initialize_app(cred_obj_base8, {'databaseURL':'https://base8-5efbb-default-rtdb.firebaseio.com/'}, name='app_base8')
ref_base8=db.reference('/', app_base8)

cred_obj_base9 = firebase_admin.credentials.Certificate('base9.json')
app_base9 = firebase_admin.initialize_app(cred_obj_base9, {'databaseURL':'https://base9-8e49f-default-rtdb.firebaseio.com/'}, name='app_base9')
ref_base9=db.reference('/', app_base9)

cred_obj_base10 = firebase_admin.credentials.Certificate('base10.json')
app_base10 = firebase_admin.initialize_app(cred_obj_base10, {'databaseURL':'https://base10-d1dcb-default-rtdb.firebaseio.com/'}, name='app_base10')
ref_base10=db.reference('/', app_base10)

cred_obj_base11 = firebase_admin.credentials.Certificate('base11.json')
app_base11 = firebase_admin.initialize_app(cred_obj_base11, {'databaseURL':'https://base11-36239-default-rtdb.firebaseio.com/'}, name='app_base11')
ref_base11=db.reference('/', app_base10)



client = discord.Client()


def first_letter(a):
  if(a in 'a'): temp_ref=ref_a
  elif(a in 'b'): temp_ref=ref_b
  elif(a in 'c'): temp_ref=ref_c
  elif(a in 'd'): temp_ref=ref_d
  elif(a in 'e'): temp_ref=ref_e
  elif(a in 'f'): temp_ref=ref_f
  elif(a in 'g'): temp_ref=ref_g
  elif(a in 'h'): temp_ref=ref_h
  elif(a in 'i'): temp_ref=ref_i
  elif(a in 'j'): temp_ref=ref_j
  elif(a in 'k'): temp_ref=ref_k
  elif(a in 'l'): temp_ref=ref_l
  elif(a in 'm'): temp_ref=ref_m
  elif(a in 'n'): temp_ref=ref_n
  elif(a in 'o'): temp_ref=ref_o
  elif(a in 'p'): temp_ref=ref_p
  elif(a in 'q'): temp_ref=ref_q
  elif(a in 'r'): temp_ref=ref_r
  elif(a in 's'): temp_ref=ref_s
  elif(a in 't'): temp_ref=ref_t
  elif(a in 'u'): temp_ref=ref_u
  elif(a in 'v'): temp_ref=ref_v
  elif(a in 'w'): temp_ref=ref_w
  elif(a in 'x'): temp_ref=ref_x
  elif(a in 'y'): temp_ref=ref_y
  elif(a in 'z'): temp_ref=ref_z
  else: temp_ref=ref_backup
  
  return temp_ref
  






def convert(query):
  query=query.strip(' ')
  query=re.sub(' +', ' ', query)
  query_new=query
  query_new=query_new.replace('.', ' ')
  query_new=query_new.replace('  ',' ')
  list1=query_new.split(' ')
  if(query_new[1]==' '):query_new=list1[0]+'.+'
  else: query_new=list1[0]+'+'
  for x in range(1,len(list1)):
    query_new+=list1[x]+'+'
  query_new=query_new[:-1]

  LINK_NEW=f'https://www.pesmaster.com/pes-2021/?q={query_new}'
  if(query_new!=query): 
    if(query_new[:6]=="p.+bos" or query_new[:7]=="peter+b"): return(1,f'https://www.pesmaster.com/p-bosz/pes-2021/coach/435/')
    elif(query_new[:5]=="m.+ro" or query_new[:8]=="marco+ro"): return(1, f'https://www.pesmaster.com/m-rossi/pes-2021/coach/232894/')
    elif(query_new[:10]=="zinedine+z"): return(1, f'https://www.pesmaster.com/y-grimault/pes-2021/coach/362884/')
    elif(query_new[:8]=="ronald+k" or query_new[:6]=="r.+koe"): return(1, f'https://www.pesmaster.com/r-koeman/pes-2021/coach/350/')
    elif(query_new[:8]=="steven+g" or query_new[:5]=="s.+ge"): return(1, f'https://www.pesmaster.com/s-gerrard/pes-2021/coach/101634/')
    elif(query_new[:8]=="andrea+p" or query_new[:5]=="a.+pi"): return(1, f'https://www.pesmaster.com/a-pirlo/pes-2021/coach/102298/')
    elif(query_new[:3]=="rya" or query_new[:4]=="r.+g"): return(1, f'https://www.pesmaster.com/r-giggs/pes-2021/coach/232551/')
    elif(query_new[:8]=="mario+sa" or query_new[:6]=="m.+sal" or query_new[:8]=="mario+al"): 
      return(1, f'https://www.pesmaster.com/m-salas/pes-2021/coach/195/')
    r=requests.get(LINK_NEW)
    soup=BeautifulSoup(r.content, "html.parser")
    title=soup.find('title').get_text()
    if('PES 2021 Database' in title): 
      for data in soup.findAll('div',{'class':'team-block'}):
        data_str=str(data)
        if("coach" in data_str):
          c1=data_str.find("href=") +7
          c2=data_str.find('/">')
          query2=data_str[c1:c2]
          LINK_NEW=f'https://www.pesmaster.com/{query2}/'
    return(1, LINK_NEW)
  else: return(0, LINK_NEW)

def get_manager_scrape(name):
  name_checker_flag, URL_FINAL=convert(name)
  if(name_checker_flag==1): return URL_FINAL
  else:
    r=requests.get(URL_FINAL)
    soup=BeautifulSoup(r.content, "html.parser")
    for data in soup.findAll('div',{'class':'team-block'}):
      data_str=str(data)
      if("coach" in data_str):
        c1=data_str.find("href=") +7
        c2=data_str.find('/">')
        query2=data_str[c1:c2]
        URL_FINAL=f'https://www.pesmaster.com/{query2}/'
    return(URL_FINAL)

def get_manager(name):
  try:
    if(' ' in name):
      return get_manager_scrape(name)
    else: 
      URL_FINAL=first_letter(name[0]).get().get(name).get('URL')
      return URL_FINAL
  except:
      a=first_letter(name[0]).get()
      for key in a.keys():
        if(name in key):
          URL_FINAL=a.get(key).get('URL')
          print('HERE')
          return URL_FINAL
      
      autocorrect_list=difflib.get_close_matches(name, ref_backup.get().keys())
      if(len(autocorrect_list)!=0):
        return get_manager(autocorrect_list[0])
      return get_manager_scrape(name)

def get_condition(name):
  if(name[1]==" "):name=name.replace(" ",". ") 
  elif(" " in name and name[1]!=" "): name=name.replace(" ", "%20")
  else:
    name=name.replace(" ","")
    name=name.replace(".",".%20")
  url =f'https://pesdb.net/pes2021/?name={name}'
  r=requests.get(url)
  soup=BeautifulSoup(r.content, "html.parser")
  text1=soup.find('td', text=["C","B", "A", "D", "E"])
  data=soup.find('td', {'class': 'left'}).text

  return data, text1.text

def get_table(name, tactic):
  try:
    t1=time.time()
    name_new=name.replace(" ", "-")
    name_new=name_new.replace(".", "-")
    name_new=name_new.replace("--", "-")
    manager_name=first_letter(name[0]).get().get(name_new).get('Name')

    if(tactic==2): 
      Attacking_Style=first_letter(name[0]).get().get(name_new).get('Attacking Style  off')
      Build_Up=first_letter(name[0]).get().get(name_new).get('Build Up  off')
      Attacking_Area=first_letter(name[0]).get().get(name_new).get('Attacking Area  off')
      Positioning=first_letter(name[0]).get().get(name_new).get('Positioning  off')
      Defensive_Style=first_letter(name[0]).get().get(name_new).get('Defensive Style  off')
      Containment_Area=first_letter(name[0]).get().get(name_new).get('Containment Area  off')
      Pressuring=first_letter(name[0]).get().get(name_new).get('Pressuring  off')
      Support_Range=first_letter(name[0]).get().get(name_new).get('Support Range  off')
      Defensive_Line=first_letter(name[0]).get().get(name_new).get('Defensive Line  off')
      Compactness=first_letter(name[0]).get().get(name_new).get('Compactness  off')
    elif(tactic==3): 
      Attacking_Style=first_letter(name[0]).get().get(name_new).get('Attacking Style  def')
      Build_Up=first_letter(name[0]).get().get(name_new).get('Build Up  def')
      Attacking_Area=first_letter(name[0]).get().get(name_new).get('Attacking Area  def')
      Positioning=first_letter(name[0]).get().get(name_new).get('Positioning  def')
      Defensive_Style=first_letter(name[0]).get().get(name_new).get('Defensive Style  def')
      Containment_Area=first_letter(name[0]).get().get(name_new).get('Containment Area  def')
      Pressuring=first_letter(name[0]).get().get(name_new).get('Pressuring  def')
      Support_Range=first_letter(name[0]).get().get(name_new).get('Support Range  def')
      Defensive_Line=first_letter(name[0]).get().get(name_new).get('Defensive Line  def')
      Compactness=first_letter(name[0]).get().get(name_new).get('Compactness  def')
    print(time.time()-t1)
    return manager_name, Attacking_Style,Build_Up,Attacking_Area,Positioning,Defensive_Style,Containment_Area,Pressuring,Support_Range,Defensive_Line,Compactness
  except:
    a=first_letter(name[0]).get()
    for key in a.keys():
      if(name in key):
        manager_name=a.get(key).get('Name')
        if(tactic==2): 
          Attacking_Style=first_letter(name[0]).get().get(key).get('Attacking Style  off')
          Build_Up=first_letter(name[0]).get().get(key).get('Build Up  off')
          Attacking_Area=first_letter(name[0]).get().get(key).get('Attacking Area  off')
          Positioning=first_letter(name[0]).get().get(key).get('Positioning  off')
          Defensive_Style=first_letter(name[0]).get().get(key).get('Defensive Style  off')
          Containment_Area=first_letter(name[0]).get().get(key).get('Containment Area  off')
          Pressuring=first_letter(name[0]).get().get(key).get('Pressuring  off')
          Support_Range=first_letter(name[0]).get().get(key).get('Support Range  off')
          Defensive_Line=first_letter(name[0]).get().get(key).get('Defensive Line  off')
          Compactness=first_letter(name[0]).get().get(key).get('Compactness  off')
        elif(tactic==3): 
          Attacking_Style=first_letter(name[0]).get().get(key).get('Attacking Style  def')
          Build_Up=first_letter(name[0]).get().get(key).get('Build Up  def')
          Attacking_Area=first_letter(name[0]).get().get(key).get('Attacking Area  def')
          Positioning=first_letter(name[0]).get().get(key).get('Positioning  def')
          Defensive_Style=first_letter(name[0]).get().get(key).get('Defensive Style  def')
          Containment_Area=first_letter(name[0]).get().get(key).get('Containment Area  def')
          Pressuring=first_letter(name[0]).get().get(key).get('Pressuring  def')
          Support_Range=first_letter(name[0]).get().get(key).get('Support Range  def')
          Defensive_Line=first_letter(name[0]).get().get(key).get('Defensive Line  def')
          Compactness=first_letter(name[0]).get().get(key).get('Compactness  def')
        print(time.time()-t1)
        return manager_name, Attacking_Style,Build_Up,Attacking_Area,Positioning,Defensive_Style,Containment_Area,Pressuring,Support_Range,Defensive_Line,Compactness   
    
    autocorrect_list=difflib.get_close_matches(name, ref_backup.get().keys())
    if(len(autocorrect_list)!=0):
      return get_table(autocorrect_list[0], tactic)
  
    url = get_manager(name)
    r = requests.get(url)
    soup=BeautifulSoup(r.content, "html.parser")
    text2=soup.find('td', text="Name").find_next('td')         #Manager name
    manager_parameter= []
    table = soup.find_all('table', attrs={'class':'player-stats-modern coach-tactics'})[tactic-2]
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
      cols = row.find_all('td')
      cols = [ele.text.strip() for ele in cols]
      manager_parameter.append([ele for ele in cols if ele]) # Get rid of empty values
    manager_parameter.pop(9)
    manager_parameter.pop(8)
    manager_parameter.pop(4)
  
    data=soup.findAll('table')[tactic]
    data_str=str(data)
    res = [i for i in range(len(data_str)) if data_str.startswith('background-position:', i)]
    manager_parameter.append(data_str[res[0]+22])
    manager_parameter.append(data_str[res[1]+22])
    manager_parameter.append(data_str[res[2]+22])
    Attacking_Style=manager_parameter[0][1]
    Build_Up=manager_parameter[1][1]
    Attacking_Area=manager_parameter[2][1]
    Positioning=manager_parameter[3][1]
    Defensive_Style=manager_parameter[4][1]
    Containment_Area=manager_parameter[5][1]
    Pressuring=manager_parameter[6][1]
    Support_Range=manager_parameter[7]
    Defensive_Line=manager_parameter[8]
    Compactness=manager_parameter[9]
    if(data_str[res[0]+24]=="0"):Support_Range="10"
    if(data_str[res[1]+24]=="0"):Defensive_Line="10"
    if(data_str[res[2]+24]=="0"):Compactness="10"
    print(time.time()-t1)
  return text2.text, Attacking_Style,Build_Up,Attacking_Area,Positioning,Defensive_Style,Containment_Area,Pressuring,Support_Range,Defensive_Line,Compactness

def get_formation(name):
  try:
    manager_name=first_letter(name[0]).get().get(name).get('Name')
    formation=first_letter(name[0]).get().get(name).get('Formation')
    management_skill=first_letter(name[0]).get().get(name).get('Management Skill')
  except:    
    a=first_letter(name[0]).get()
    for key in a.keys():
      if(name in key):
        formation=a.get(key).get('Formation')
        manager_name=a.get(key).get('Name')
        management_skill=a.get(key).get('Management Skill')
        return manager_name, formation, management_skill  
    autocorrect_list=difflib.get_close_matches(name, ref_backup.get().keys())
    if(len(autocorrect_list)!=0):
      return get_formation(autocorrect_list[0])
    url=get_manager(name)
    r = requests.get(url)
    soup=BeautifulSoup(r.content, "html.parser")
    soup.prettify()
    formation=soup.find('td', text="Formation").find_next('td').text
    manager_name=soup.find('td', text="Name").find_next('td').text
    management_skill=soup.find('td', text="Management Skills").find_next('td').text
  return manager_name, formation, management_skill

def get_player_list(name):
  player_list,count=[],0
  query=f'https://www.pesmaster.com/pes-2021/?q={name}'
  r=requests.get(query)
  #webbrowser.open(query)
  soup=BeautifulSoup(r.content, "html.parser")
  soup.prettify()
  title=soup.find('title').get_text()
  if('PES 2021 Stats' in title):
    URL=soup.find('link', {'rel': True}).get('href')
    start=URL.find('player/')+7
    img_code=URL[start:URL.rfind('_')]
    img_link=f'https://pesmaster.fra1.cdn.digitaloceanspaces.com/players/pes-2021/player_{img_code}.png'
    ovr=soup.find('div', attrs={'class':'player-card-ovr'}).text
    player_name=soup.find('div', attrs={'class':'player-card-name'}).text
    player_position=soup.find('div', attrs={'class':'player-card-position'}).text
    player_list.append({'link':URL, 'img':img_link, 'ovr':ovr, 'player name':player_name, 'player position':player_position})
  else:  
    data = soup.findAll('div',attrs={'class':'player-card-container'})
    for div in data:
      links = div.findAll('a')
      ovr=div.findAll('div', attrs={'class':'player-card-ovr'})
      player_name=div.findAll('div', attrs={'class':'player-card-name'})
      player_position=div.findAll('div', attrs={'class':'player-card-position'})
      for a in links:
        URL='https://www.pesmaster.com/pes-2021'+a['href']
        start=URL.find('player/')+7
        img_code=URL[start:URL.rfind('_')]
        #print(img_code)
        if(str(div).find(img_code+'_l')!=-1):
          img_link=f'https://pesmaster.fra1.cdn.digitaloceanspaces.com/players/pes-2021/player_{img_code}_l.png'      
        else:
          img_link=f'https://pesmaster.fra1.cdn.digitaloceanspaces.com/players/pes-2021/player_{img_code}.png'
        #print(img_link)
        player_list.append({'link':URL, 'img':img_link, 'ovr':ovr[count].text, 'player name':player_name[count].text, 'player position':player_position[count].text})
        count+=1
  return player_list

def get_player_stats(link):
  r=requests.get(link)
  soup=BeautifulSoup(r.content, "html.parser")
  vars  = str(soup).index("const levelStats =")  # get each var entry
  b=str(soup).rfind('boost"')-2
  if(b==-3):  b=str(soup).rindex('}];')
  test=str(soup)[vars:b]
  c=test.rindex('{')
  dic=json.loads(test[c:b]+'}')
  player_list=[]
  for data in soup.findAll('ul',attrs={'class':'player-index-list'}):
    player_list.append(data.text.strip())
  player_list.append(soup.find('td', text="Nationality").find_next('td').text)
  player_list.append(soup.find('td', text="Stronger Foot").find_next('td').text)
  player_list.append(soup.find('td', text="Height (cm)").find_next('td').text)
  player_list.append(soup.find('td', text="Condition").find_next('td').text.strip())
  player_list.append(soup.find('span', attrs={'class':'weak_foot_usage'}).text)
  player_list.append(soup.find('span', attrs={'class':'weak_foot_acc'}).text)
  player_list.append(soup.find('span', attrs={'class':'form'}).text)
  player_list.append(soup.find('span', attrs={'class':'injury_resistance'}).text)

  return dic, player_list

def advanced_search(text):
  card=''
  if('base' in text): card='type=default&'
  elif('featured' in text): card='type=featured&'
  elif('legend' in text): card='type=legend&'
  elif('im' in text or 'iconic' in text): card='type=IconicMoment&'  

  pos=''
  if('gk' in text or 'goalkeep' in text): pos='pos=0&'
  elif('cb' in text or 'centreb' in text or 'centerb' in text ):pos='pos=1&'
  elif('lb' in text  or 'leftb' in text ):pos='pos=2&'
  elif('rb' in text  or 'rightb' in text ):pos='pos=3&'    
  elif('dm' in text  or 'defensivem' in text ):pos='pos=4&'    
  elif('cm' in text  or 'centrem' in text  or 'centerm' in text ):pos='pos=5&'
  elif('lm' in text  or 'leftm' in text ):pos='pos=6&'
  elif('rm' in text  or 'rightm' in text ):pos='pos=7&'
  elif('amf' in text  or 'att' in text ):pos='pos=8&'
  elif('lw' in text  or 'leftw' in text ):pos='pos=9&'
  elif('rwf' in text  or 'rightw' in text ):pos='pos=10&'
  elif('ss' in text  or 'sec' in text  or 'supp' in text):
    if('sec' not in text and 'supp' not in text): pos='pos=11&'
    else:
      temp=[m.start() for m in re.finditer('ss', text)]
      for x in temp:
        if(text[x-3:x] != 'cro' and text[x-3:x] != 'cla'): pos='pos=11&'    
  elif('cf' in text  or 'centref' in text  or 'centerf' in text ):pos='pos=12&'

  playstyle=''
  if('no' in text):playstyle='playingstyle=0&'
  if('goalpoach' in text or 'gp' in text): playstyle='playingstyle=1&'
  elif('dummy' in text): playstyle='playingstyle=2&'
  elif('fox' in text or 'fitb' in text): playstyle='playingstyle=3&'
  elif('prolific' in text): playstyle='playingstyle=4&'
  elif('classic' in text or 'cn' in text): playstyle='playingstyle=5&'
  elif('hole' in text): playstyle='playingstyle=6&'
  elif('box' in text or 'b2b' in text): playstyle='playingstyle=7&'
  elif('anchor' in text): playstyle='playingstyle=8&'
  elif('destroy' in text): playstyle='playingstyle=9&'
  elif('extra' in text): playstyle='playingstyle=10&'
  elif('offensivef' in text): playstyle='playingstyle=11&'
  elif('defensivef' in text): playstyle='playingstyle=12&'
  elif('target' in text): playstyle='playingstyle=13&'
  elif('creative' in text or 'cp' in text): playstyle='playingstyle=14&'
  elif('build' in text): playstyle='playingstyle=15&'
  elif('offensiveg' in text): playstyle='playingstyle=16&'
  elif('defensiveg' in text): playstyle='playingstyle=17&'
  elif('roam' in text): playstyle='playingstyle=18&'
  elif('rf' in text):
    temp=[m.start() for m in re.finditer('rf', text)]
    for x in temp:
      if(text[x-3:x] != 'nte'): playstyle='playingstyle=18&'
  elif('cross' in text): playstyle='playingstyle=19&'
  elif('orches' in text): playstyle='playingstyle=20&'
  elif('finish' in text or 'fbf' in text): playstyle='playingstyle=21&'

  card_type='All'
  if('default' in card): card_type='Base'
  elif('featured' in card): card_type='Featured'
  elif('legend' in card): card_type='Legend'
  elif('Iconic' in card): card_type='IM'

  pos_list=['Goalkeeper', 'Centre-back', 'Left-back', 'Right-back', 'Defensive Midfield', 'Centre Midfield', 'Left Midfield', 'Right Midfield', 'Attacking Midfield', 'Left Winger', 'Right Winger', 'Second Striker', 'Centre Forward']
  try: pos_type=pos_list[int(pos[4:-1])]
  except: pos_type='All'

  playstyle_list=['None', 'Goal Poacher', 'Dummy Runner', 'Fox in the Box', 'Prolific Winger', 'Classic No. 10',
  'Hole Player', 'Box-to-Box', 'Anchor Man', 'Destroyer', 'Extra Frontman', 'Offensive Full Back', 'Defensive Full Back',
  'Target Man', 'Creative Playmaker', 'Build Up', 'Offensive Goalkeeper', 'Defensive Goalkeeper', 'Roaming Flank',
  'Cross Specialist', 'Orchestrator', 'Full-back Finisher']
  try: playstyle_type=playstyle_list[int(playstyle[13:-1])]
  except: playstyle_type='All'


  return card, pos, playstyle, card_type, pos_type, playstyle_type

def latest_featured():
  player_list,count=[],0
  query=f'https://www.pesmaster.com/pes-2021/player/featured/'
  r=requests.get(query)
  soup=BeautifulSoup(r.content, "html.parser")
  soup.prettify()
  data = soup.findAll('div',attrs={'class':'player-card-container'})
  for div in data:
    flag=count
    links = div.findAll('a')
    ovr=div.findAll('div', attrs={'class':'player-card-ovr'})
    player_name=div.findAll('div', attrs={'class':'player-card-name'})
    player_position=div.findAll('div', attrs={'class':'player-card-position'})
    for a in links:
      URL='https://www.pesmaster.com/pes-2021'+a['href']
      start=URL.find('player/')+7
      img_code=URL[start:URL.rfind('_')]
      if(img_code+'_l' not in str(div)):
        img_link=f'https://pesmaster.fra1.cdn.digitaloceanspaces.com/players/pes-2021/player_{img_code}_l.png'      
      else:
        img_link=f'https://pesmaster.fra1.cdn.digitaloceanspaces.com/players/pes-2021/player_{img_code}.png'
      player_list.append({'link':URL, 'img':img_link, 'ovr':ovr[count-flag].text, 'player name':player_name[count-flag].text, 'player position':player_position[count-flag].text})
      count+=1
  return player_list

def scouts(name):
  r=requests.get(f'https://pesdb.net/pes2021/?name={name}')
  soup=BeautifulSoup(r.content, "html.parser")
  data=soup.find('tr').find_next('tr').find('a')['href']
  url=f'https://pesdb.net/pes2021{data[1:]}'
  img_link=f'	https://pesdb.net/pes2021/images/players{data[5:]}.png'
  r=requests.get(url)
  scoutlist=[]
  soup=BeautifulSoup(r.content, "html.parser")
  name=soup.find('th', text='Player Name:').find_next('td').text
  pos=soup.find('th', text='Position:').find_next('td').text
  ovr=soup.find('th', text='Overall Rating:').find_next('td').text  
  print(name, pos, ovr)
  for data in soup.findAll('tr',{'class':'scout_row', 'data-percent':'100'}):
    templist=[]
    for div in data.findAll('td'):
      templist.append(div.text)
    scoutlist.append(templist)
  return name, pos, ovr, img_link, scoutlist

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if '  ' in message.content:
      while '  ' in message.content:
        message.content= message.content.replace('  ', ' ')
  message.content=message.content.lower().strip()
  message.content=unidecode.unidecode(message.content)
  if client.user.mentioned_in(message):
    print(message.content)
    message.content=message.content.replace(f'<@{client.user.id}>', '').strip()
    if '  ' in message.content:
      while '  ' in message.content:
        message.content= message.content.replace('  ', ' ')
    print(message.content)
    if('help' in message.content or len(message.content)==0): message.content='-peshelp'
  if(message.content.startswith('-manager')):
    name=message.content[9:]
    if(name.replace(' ','').replace('.','').isalpha()): 
      URL=get_manager(name)
      await message.reply(URL)
    else: 
      query, sum=str(),0 
      for x in message.content:
        if(x.isdigit()):
          query+=x+'-'
          sum+=int(x)
      if(len(query)==6 or len(query)==8): 
        if(sum==10):  
          embedVar=discord.Embed(title=f'https://www.pesmaster.com/pes-2021/coach/?formation={query[:-1]}', color=0xf1c40f)
          await message.reply(embed=embedVar)
          
  elif(message.content.startswith('-player')):
    plist=get_player_list(message.content[8:])
    count=0
    flag=0
    timeout = 20   # [seconds]
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
      if(flag==1): break
      img_link=plist[count]['img']
      player_name=plist[count]['player name']
      player_ovr=plist[count]['ovr']
      player_pos=plist[count]['player position']
      player_link=plist[count]['link']
      embedVar=discord.Embed(title=f'{count+1}.  {player_name}, {player_pos}, {player_ovr}', color=0xf1c40f)
      embedVar.set_image(url=img_link)
      text=await message.channel.send(embed=embedVar)
      await text.add_reaction('⏮️')
      await text.add_reaction('◀️')
      await text.add_reaction('⬛')
      await text.add_reaction('▶️')
      await text.add_reaction('⏭️')
      while time.time() < timeout_start + timeout:
        try:
          if(flag==1): break
          text = await text.channel.fetch_message(text.id)
          count_n, count_p, count_nn, count_pp, count_this=0, 0, 0, 0, 0
          for reaction in text.reactions:
            if(reaction.emoji == '⬛'):
              count_this=reaction.count-1
            if(reaction.emoji == '◀️'):
              count_n=reaction.count-1
            elif(reaction.emoji == '▶️'):
              count_p=reaction.count-1
            elif(reaction.emoji == '⏮️'):
              count_nn=reaction.count-1
            elif(reaction.emoji == '⏭️'):
              count_pp=reaction.count-1
            if(count_this==1):
              flag=1
              dic, additional_info=get_player_stats(player_link)
              dic=list(dic.values())
              await text.delete()
              ##############SECOND MENU STARTS#########################
              
              count1=0
              timeout1 = 60   # [seconds]
              timeout_start1 = time.time()
              while time.time() < timeout_start1 + timeout1:
                if(count1==0):  
                  if(dic[20]=='40'):  
                    embed2=discord.Embed(title=f'{player_name}, {player_pos}, {dic[25]}',
                    description=f'**Attacking** \nOffensive Awareness: **{dic[0]}** \nBall Control: **{dic[1]}** \nDribbling: **{dic[2]}** \nTight Possession: **{dic[3]}**'
                    f'\nLow Pass: **{dic[4]}** \nLofted Pass: **{dic[5]}** \nFinishing: **{dic[6]}** \nHeading: **{dic[7]}** \nPlace Kicking: **{dic[8]}**'
                    f'\nCurl: **{dic[9]}** \n\n**Athletiscism**\nSpeed: **{dic[10]}** \nAcceleration: **{dic[11]}** \nKicking Power: **{dic[12]}** \nJump: **{dic[13]}** \nPhysical Contact: **{dic[14]}**'
                    f'\nBalance: **{dic[15]}** \nStamina: **{dic[16]}** \n\n**Defending** \nDefensive Awareness: **{dic[17]}** \nBall Winning: **{dic[18]}** \nAggression: **{dic[19]}** \n[Link]({player_link})', color=0xf1c40f)
                    embed2.set_thumbnail(url=img_link)
                    
                  else:
                    embed2=discord.Embed(title=f'{player_name}, {player_pos}',
                    description=f'**GoalKeeeping** \nGK Awareness: **{dic[20]}** \nGK Catching: **{dic[21]}** \nGK Clearing: **{dic[22]}** \nGK Reflexes: **{dic[23]}** \nGK Reach: **{dic[24]}** \n[Link]({player_link})', color=0xf1c40f) 
                    embed2.set_thumbnail(url=img_link)
                    
                elif(count1==1):
                  embed2=discord.Embed(title=f'{player_name}, {player_pos}, {dic[25]}', color=0xf1c40f)
                  embed2.add_field(name=f'\a\nNationality: {additional_info[3]} \nStronger Foot: {additional_info[4]} \nHeight: {additional_info[5]}cm \nCondition: {additional_info[6]} \nWeak Foot Usage: {additional_info[7]} \nWeak Foot Acc: {additional_info[8]} \nForm: {additional_info[9]} \nInjury Resistance: {additional_info[10]}', value='\a', inline=True)
                  embed2.add_field(name=f'Playing Style', value=additional_info[0], inline=True)
                  skill_counter=additional_info[1].count('\n')+1 if additional_info[1].count('\n')!=10 else 10
                  embed2.add_field(name=f'\a\nPlayer Skills- {skill_counter}', value=additional_info[1], inline=True)
                  embed2.add_field(name=f'\a\nCOM Playing Styles', value=additional_info[2], inline=True)
                  embed2.set_thumbnail(url=img_link)
                  
                text1=await message.channel.send(embed=embed2)
                await text1.add_reaction('◀️')
                await text1.add_reaction('▶️')
                while time.time() < timeout_start1 + timeout1:
                  try:
                    text1= await text1.channel.fetch_message(text1.id)
                    count_n1, count_p1=0, 0
                    for reaction in text1.reactions:
                      if(reaction.emoji == '◀️'):
                        count_n1=reaction.count-1
                      elif(reaction.emoji == '▶️'):
                        count_p1=reaction.count-1
                      if(count_n1==1 and count1!=0): 
                        await text1.delete()
                        timeout_start1 = time.time()
                        count1=0
                        break
                      elif(count_p1==1 and count1!=1): 
                        await text1.delete()
                        timeout_start1 = time.time()
                        count1=1
                        break
                  except: break
              await text1.remove_reaction('◀️', client.get_user(text1.author.id))
              await text1.remove_reaction('▶️', client.get_user(text1.author.id))       
                                              
              break
            if(count_n==1 and count!=0): 
              await text.delete()
              timeout_start = time.time()
              count-=1
              break
            elif(count_p==1 and count!=len(plist)-1): 
              await text.delete()
              timeout_start = time.time()
              print('+++++++++++++')
              count+=1
              break
            elif(count_nn==1): 
              await text.delete()
              timeout_start = time.time()
              count=0
              break
            elif(count_pp==1): 
              await text.delete()
              timeout_start = time.time()
              count=len(plist)-1
              break
        except: break
    await text.delete()
    await message.reply(f'Oops, the bot timed out. Please respond within 20 seconds next time.')

  elif(message.content.startswith('-featured') or message.content.startswith('-ft')):
    plist=latest_featured()
    count=0
    flag=0
    timeout = 20   # [seconds]
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
      if(flag==1): break
      img_link=plist[count]['img']
      player_name=plist[count]['player name']
      player_ovr=plist[count]['ovr']
      player_pos=plist[count]['player position']
      player_link=plist[count]['link']
      embedVar=discord.Embed(title=f'{count+1}.  {player_name}, {player_pos}, {player_ovr}', color=0xf1c40f)
      embedVar.set_image(url=img_link)
      text=await message.channel.send(embed=embedVar)
      await text.add_reaction('⏮️')
      await text.add_reaction('◀️')
      await text.add_reaction('⬛')
      await text.add_reaction('▶️')
      await text.add_reaction('⏭️')
      while time.time() < timeout_start + timeout:
        try:
          if(flag==1): break
          text = await text.channel.fetch_message(text.id)
          count_n, count_p, count_nn, count_pp, count_this=0, 0, 0, 0, 0
          for reaction in text.reactions:
            if(reaction.emoji == '⬛'):
              count_this=reaction.count-1
            if(reaction.emoji == '◀️'):
              count_n=reaction.count-1
            elif(reaction.emoji == '▶️'):
              count_p=reaction.count-1
            elif(reaction.emoji == '⏮️'):
              count_nn=reaction.count-1
            elif(reaction.emoji == '⏭️'):
              count_pp=reaction.count-1
            if(count_this==1):
              flag=1
              dic, additional_info=get_player_stats(player_link)
              dic=list(dic.values())
              await text.delete()
              ##############SECOND MENU STARTS#########################
              
              count1=0
              timeout1 = 60   # [seconds]
              timeout_start1 = time.time()
              while time.time() < timeout_start1 + timeout1:
                if(count1==0):  
                  if(dic[20]=='40'):  
                    embed2=discord.Embed(title=f'{player_name}, {player_pos}, {dic[25]}',
                    description=f'**Attacking** \nOffensive Awareness: **{dic[0]}** \nBall Control: **{dic[1]}** \nDribbling: **{dic[2]}** \nTight Possession: **{dic[3]}**'
                    f'\nLow Pass: **{dic[4]}** \nLofted Pass: **{dic[5]}** \nFinishing: **{dic[6]}** \nHeading: **{dic[7]}** \nPlace Kicking: **{dic[8]}**'
                    f'\nCurl: **{dic[9]}** \n\n**Athletiscism**\nSpeed: **{dic[10]}** \nAcceleration: **{dic[11]}** \nKicking Power: **{dic[12]}** \nJump: **{dic[13]}** \nPhysical Contact: **{dic[14]}**'
                    f'\nBalance: **{dic[15]}** \nStamina: **{dic[16]}** \n\n**Defending** \nDefensive Awareness: **{dic[17]}** \nBall Winning: **{dic[18]}** \nAggression: **{dic[19]}** \n[Link]({player_link})', color=0xf1c40f)
                    embed2.set_thumbnail(url=img_link)
                  else:
                    embed2=discord.Embed(title=f'{player_name}, {player_pos}',
                    description=f'**GoalKeeeping** \nGK Awareness: **{dic[20]}** \nGK Catching: **{dic[21]}** \nGK Clearing: **{dic[22]}** \nGK Reflexes: **{dic[23]}** \nGK Reach: **{dic[24]}** \n[Link]({player_link})', color=0xf1c40f) 
                    embed2.set_thumbnail(url=img_link)
                elif(count1==1):
                  embed2=discord.Embed(title=f'{player_name}, {player_pos}, {dic[25]}', color=0xf1c40f)
                  embed2.add_field(name=f'Playing Style', value=additional_info[0], inline=True)
                  embed2.add_field(name=f'\a\nNationality: {additional_info[3]} \nStronger Foot: {additional_info[4]} \nHeight: {additional_info[5]}cm \nCondition: {additional_info[6]} \nWeak Foot Usage: {additional_info[7]} \nWeak Foot Acc: {additional_info[8]} \nForm: {additional_info[9]} \nInjury Resistance: {additional_info[10]}', value='\a', inline=True)
                  embed2.add_field(name=f'Playing Style', value=additional_info[0], inline=True)
                  skill_counter=additional_info[1].count('\n')+1 if additional_info[1].count('\n')!=10 else 10
                  embed2.add_field(name=f'\a\nPlayer Skills- {skill_counter}', value=additional_info[1], inline=True)
                  embed2.add_field(name=f'\a\nCOM Playing Styles', value=additional_info[2], inline=True)
                  embed2.set_thumbnail(url=img_link)
                
                text1=await message.channel.send(embed=embed2)
                await text1.add_reaction('◀️')
                await text1.add_reaction('▶️')
                while time.time() < timeout_start1 + timeout1:
                  try:
                    text1= await text1.channel.fetch_message(text1.id)
                    count_n1, count_p1=0, 0
                    for reaction in text1.reactions:
                      if(reaction.emoji == '◀️'):
                        count_n1=reaction.count-1
                      elif(reaction.emoji == '▶️'):
                        count_p1=reaction.count-1
                      if(count_n1==1 and count1!=0): 
                        await text1.delete()
                        timeout_start1 = time.time()
                        count1=0
                        break
                      elif(count_p1==1 and count1!=1): 
                        await text1.delete()
                        timeout_start1 = time.time()
                        count1=1
                        break
                  except: break
              await text1.remove_reaction('◀️', client.get_user(text1.author.id))
              await text1.remove_reaction('▶️', client.get_user(text1.author.id))       
                                              
              break
            if(count_n==1 and count!=0): 
              await text.delete()
              timeout_start = time.time()
              count-=1
              break
            elif(count_p==1 and count!=len(plist)-1): 
              await text.delete()
              timeout_start = time.time()
              print('+++++++++++++')
              count+=1
              break
            elif(count_nn==1): 
              await text.delete()
              timeout_start = time.time()
              count=0
              break
            elif(count_pp==1): 
              await text.delete()
              timeout_start = time.time()
              count=len(plist)-1
              break
        except: break
    await text.delete()
    await message.reply(f'Oops, the bot timed out. Please respond within 20 seconds next time.')

  elif(message.content.startswith('-condition')): 
    name=message.content[11:]
    name, player_condition=get_condition(name)
    await message.reply(f'**{name}** has condition {player_condition} for this week')
  
  elif(message.content.startswith('-offensive') or message.content.startswith('-attacking')):
    name=message.content[11:]
    name, Attacking_Style,Build_Up,Attacking_Area,Positioning,Defensive_Style,Containment_Area,Pressuring,Support_Range,Defensive_Line,Compactness=get_table(name,2)
    if(Build_Up!=None): await message.reply(f'Offensive tactics of `{name}` are:\n'
    f'\n**Attacking Style                       {Attacking_Style}**'
    f'\nBuild Up                                    {Build_Up}'
    f'\n**Attacking Area                       {Attacking_Area}**'
    f'\nPositioning                               {Positioning}'
    f'\n**Defensive Style                       {Defensive_Style}**'
    f'\nContainment Area                 {Containment_Area}'
    f'\n**Pressuring                                {Pressuring}**'
    f'\nSupport Range                          {Support_Range}'
    f'\n**Defensive Line                          {Defensive_Line}**'
    f'\nCompactness                            {Compactness}')
    print(name)
  elif(message.content.startswith('-defensive')):
    name=message.content[11:]
    name, Attacking_Style,Build_Up,Attacking_Area,Positioning,Defensive_Style,Containment_Area,Pressuring,Support_Range,Defensive_Line,Compactness=get_table(name,3)
    if(Build_Up!=None): await message.reply(f'Defensive tactics of `{name}` are:\n'
    f'\n**Attacking Style                       {Attacking_Style}**'
    f'\nBuild Up                                    {Build_Up}'
    f'\n**Attacking Area                       {Attacking_Area}**'
    f'\nPositioning                               {Positioning}'
    f'\n**Defensive Style                       {Defensive_Style}**'
    f'\nContainment Area                 {Containment_Area}'
    f'\n**Pressuring                                {Pressuring}**'
    f'\nSupport Range                          {Support_Range}'
    f'\n**Defensive Line                          {Defensive_Line}**'
    f'\nCompactness                            {Compactness}')

  elif(message.content.startswith('-formation')):
    name=message.content[11:]
    name, formation, skill= get_formation(name)
    
    if(formation!= None):await message.reply(f'Manager **{name}**({skill}) has formation **{formation}** this week')

  elif(message.content.startswith('-position')):
    text=message.content[10:].replace(' ','')
    card, pos, playstyle, card_type, pos_type, playstyle_type=advanced_search(text)

    embedVar=discord.Embed(title=f'{message.author.display_name}, here are your search results',
    description=f'[Card Type: {card_type}\nPosition: {pos_type}\nPlaystyle: {playstyle_type}](https://www.pesmaster.com/pes-2021/search/?{card}{pos}{playstyle}sort=ovr&sort_order=desc)', color=0xf1c40f)
    await message.reply(embed=embedVar)

  elif(message.content.startswith('-playstyle')):
    text=message.content[11:].replace(' ','')
    card, pos, playstyle, card_type, pos_type, playstyle_type=advanced_search(text)

    embedVar=discord.Embed(title=f'{message.author.display_name}, here are your search results',
    description=f'[Card Type: {card_type}\nPosition: {pos_type}\nPlaystyle: {playstyle_type}](https://www.pesmaster.com/pes-2021/search/?{card}{pos}{playstyle}sort=ovr&sort_order=desc)', color=0xf1c40f)
    await message.reply(embed=embedVar)

  elif(message.content.startswith('-peshelp manager')):
    embedVar=discord.Embed(title='-manager', 
    description='To get manager details, use **-manager**\n Example: **-manager gasperini**\n\nTo search for all managers with a particular formation, use **-manager**\n Example: **-manager 433**\n', color=0xf1c40f)
    await message.channel.send(embed=embedVar)  

  elif(message.content.startswith('-peshelp player')):
    embedVar=discord.Embed(title='-player',
    description='For a player search use **-player** which will lead you to a paginated menu with various versions of a player.\n\nYou can choose your preferred card by clicking on the  ⬛ emote\nExample: **-player Messi**\n', color=0xf1c40f)
    await message.channel.send(embed=embedVar)

  elif(message.content.startswith('-peshelp position') or message.content.startswith('-peshelp playstyle')):
    embedVar=discord.Embed(title='-position or -playstyle',
    description='To search for players by position use **-position** \n Example: **-position CB**\n\nTo search for players by playstyle use **-playstyle** \n Example: **-playstyle build up**\n\nYou can also search by position, card types and/or playstyle simultaneously types by adding `base` or `featured` or `legend` or `IM` or `playstyle name` to the text \nExample: **-position CF legend destroyer**', color=0xf1c40f) 
    await message.channel.send(embed=embedVar)
  
  elif(message.content.startswith('-peshelp condition')):
    embedVar=discord.Embed(title='-condition',
    description='To get player condition for the week use **-condition** \n Example: **-condition Ramos**\n', color=0xf1c40f) 
    await message.channel.send(embed=embedVar)

  elif(message.content.startswith('-peshelp featured')):
    embedVar=discord.Embed(title='-featured',
    description='To see the latest featured for the week use **-featured** or **-ft** \n Example: **-featured**\n', color=0xf1c40f) 
    await message.channel.send(embed=embedVar)

  elif(message.content.startswith('-peshelp offensive') or message.content.startswith('-peshelp defensive')):
    embedVar=discord.Embed(title='-offensive or -defensive',
    description='To get the offensive tactics of a manager, use **-offensive** or **-attacking**\n Example: **-offensive Dominguez**\n\nTo get the defensive tactics of a manager, use **-defensive**\n Example: **-defensive Bindewald**\n', color=0xf1c40f)
    await message.channel.send(embed=embedVar)

  elif(message.content.startswith('-peshelp formation')):
    embedVar=discord.Embed(title='-formation',
    description='To get the formation of a manager, use **-formation**\n Example: **-formation Rossi**\n', color=0xf1c40f)
    await message.channel.send(embed=embedVar)

  elif(message.content.startswith('-peshelp id add')):
    embedVar=discord.Embed(title='-id add',
    description='To store your PES ID with the bot, use **-id add <Your 9 digit ID>**\n Example: **-id add 123456789**\n', color=0xf1c40f)
    await message.channel.send(embed=embedVar)

  elif(message.content.startswith('-peshelp id delete')):
    embedVar=discord.Embed(title='-id delete',
    description="To delete your PES ID from the bot's records, use **-id delete**\n", color=0xf1c40f)
    await message.channel.send(embed=embedVar)
  
  elif(message.content.startswith('-peshelp id update')):
    embedVar=discord.Embed(title='-id update',
    description='To update your PES ID, use **-id update <Your 9 digit ID>**\n Example: **-id update 123456789**', color=0xf1c40f)
    await message.channel.send(embed=embedVar)

  elif(message.content.startswith('-peshelp id get') or message.content.startswith('-peshelp id')):
    embedVar=discord.Embed(title='-id or -id get',
    description=f'To get the PES ID of another user, use **-id @That_User** or **-id get @That_User**\n Example: **-id @{message.author.display_name}** \n', color=0xf1c40f)
    await message.channel.send(embed=embedVar)
  
  elif(message.content.startswith('-peshelp pull im') or message.content.startswith('-peshelp pull iconic')):
    embedVar=discord.Embed(title='-pull IM or -pull iconic',
    description='To pull a random IM, use **-pull IM** or **-pull iconic** \n Example: **-pull IM** \n', color=0xf1c40f)
    await message.channel.send(embed=embedVar)
  
  elif(message.content.startswith('-peshelp pull legend') or message.content.startswith('-peshelp pack legend')):
    embedVar=discord.Embed(title='-pull legend or -pack legend',
    description='To pull a random legend, use **-pull legend** or **-pack legend** \n Example: **-pull legend** \n', color=0xf1c40f)
    await message.channel.send(embed=embedVar)

  elif(message.content.startswith('-peshelp pull') or message.content.startswith('-peshelp pack')):
    embedVar=discord.Embed(title='-pull or -pack',
    description='To pack a random card, use -pull or -pack \n Example: **-pack** \n', color=0xf1c40f)
    await message.channel.send(embed=embedVar)

  elif(message.content.startswith('-peshelp invite') or message.content.startswith('-invite')):
    embedVar=discord.Embed(title='-invite',
    description='Click the link in my bio to invite the bot to your server\n', color=0xf1c40f)
    await message.channel.send(embed=embedVar)

  elif(message.content.startswith('-peshelp friendly')):
    embedVar=discord.Embed(title='-friendly',
    description=f'To challenge others to a friendly, use **-friendly** \n Example: **-friendly**', color=0xf1c40f)
    await message.channel.send(embed=embedVar)
  
  elif(message.content.startswith('-peshelp scout')):
    embedVar=discord.Embed(title='-scout',
    description=f'To see the 100% scout combinations for a player, use **-scout** \n Example: **-scout Messi**', color=0xf1c40f)
    await message.channel.send(embed=embedVar)

  elif(message.content.startswith('-peshelp')):    
    help_title=['PES Bot Help', 'Manager commands', 'Player Commands', 'ID Commands', 'Pack Opening Commands']
    help_commands=['-manager', '-formation', '-offensive or -defensive', '-player',
    '-condition', '-position or -playstyle','-featured or -FT', '-scout', '-friendly', '-id or -id get', '-id add', '-id update', '-id delete',
    '-pull IM', '-pull legend', '-pack or -pull']
    help_content=['To get manager details, use -manager\n Example: **-manager gasperini**\n\nTo search for all managers with a particular formation, use -manager\n Example: **-manager 433**',
    'To get the formation of a manager, use -formation\n Example: **-formation Rossi**',
    'To get the offensive tactics of a manager, use -offensive or -attacking\n Example: **-offensive Dominguez**\n\nTo get the defensive tactics of a manager, use -defensive\n Example: **-defensive Bindewald**',
    'For a player search use -player which will lead you to a paginated menu with various versions of a player.\n\nYou can choose your preferred card by clicking on the  ⬛ emote\nExample: **-player Messi**',
    'To get player condition for the week use -condition \n Example: **-condition Ramos**',
    'To search for players by position use -position \n Example: **-position CB**\n\nTo search for players by playstyle use -playstyle \n Example: **-playstyle build up**\n\nYou can also search by position, card types and/or playstyle simultaneously types by adding `base` or `featured` or `legend` or `IM` or `playstyle name` to the text \nExample: **-position CF legend destroyer**',
    'To see the latest featured for the week use **-featured** or **-ft** \n Example: **-featured**',
    f'To see the 100% scout combinations for a player, use **-scout** \n Example: **-scout Messi**',
    'To challenge others to a friendly, use **-friendly** \n Example: **-friendly**',
    f'To get the PES ID of another user, use -id @That_User or -id get @That_User\n Example: **-id @{message.author.display_name}**',
    "To delete your PES ID from the bot's records, use -id delete",    
    'To store your PES ID with the bot, use -id add <Your 9 digit ID>\n Example: **-id add 123456789**',
    'To update your PES ID, use -id update <Your 9 digit ID>\n Example: **-id update 123456789**',    
    'To pack a random IM, use -pull IM or -pull iconic. You can also use -pack instead of -pull. \n Example: **-pull IM**',
    'To pack a random legend, use -pull legend. You can also use -pack instead of -pull. \n Example: **-pull legend**',
    'To pack a random card, use -pull or -pack \n Example: **-pack**' ]

    count=0
    timeout = 60   # [seconds]
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
      if(count==0):
        embedVar = discord.Embed(title=help_title[0], description='Type -peshelp `command name` to know more about any of the following commands or traverse the menu with the reactions added below', color=0xf1c40f)
        embedVar.add_field(name="-invite \n-manager \n-formation \n-offensive \n-defensive \n-player \n-condition \n-position \n-playstyle \n-featured \n-scout \n-friendly \n-id get \n-id add \n-id update \n-id delete \n-pull IM \n-pull legend \n-pack", value='\a', inline=True)
        text=await message.channel.send(embed=embedVar)
      elif(count==1):
        embedVar = discord.Embed(title=f'_                       _ {help_title[1]}', color=0xf1c40f)
        embedVar.add_field(name=f'\n{help_commands[0]}', value=help_content[0], inline=True)
        embedVar.add_field(name=f'\a\n{help_commands[1]}', value=help_content[1], inline=True)
        embedVar.add_field(name=f'\a\n{help_commands[2]}', value=help_content[2], inline=True)
        text=await message.channel.send(embed=embedVar)
      elif(count==2):
        embedVar = discord.Embed(title=f'_                           _ {help_title[2]}', color=0xf1c40f)
        embedVar.add_field(name=f'\n{help_commands[3]}', value=help_content[3], inline=True)
        embedVar.add_field(name=f'\a\n{help_commands[4]}', value=help_content[4], inline=True)
        embedVar.add_field(name=f'\a\n{help_commands[5]}', value=help_content[5], inline=True)
        embedVar.add_field(name=f'\a\n{help_commands[6]}', value=help_content[6], inline=True)
        embedVar.add_field(name=f'\a\n{help_commands[7]}', value=help_content[7], inline=True)
        text=await message.channel.send(embed=embedVar)
      elif(count==3):
        embedVar = discord.Embed(title=f'_                              _ {help_title[3]}', color=0xf1c40f)
        embedVar.add_field(name=f'\n{help_commands[8]}', value=help_content[8], inline=True)
        embedVar.add_field(name=f'\a\n{help_commands[9]}', value=help_content[9], inline=True)
        embedVar.add_field(name=f'\a\n{help_commands[10]}', value=help_content[10], inline=True)
        embedVar.add_field(name=f'\a\n{help_commands[11]}', value=help_content[11], inline=True)
        embedVar.add_field(name=f'\n{help_commands[12]}', value=help_content[12], inline=True)
        text=await message.channel.send(embed=embedVar)
      elif(count==4):
        embedVar = discord.Embed(title=f'_                  _ {help_title[4]}', color=0xf1c40f)
        embedVar.add_field(name=f'\n{help_commands[13]}', value=help_content[13], inline=True)
        embedVar.add_field(name=f'\a\n{help_commands[14]}', value=help_content[14], inline=True)
        embedVar.add_field(name=f'\a\n{help_commands[15]}', value=help_content[15], inline=True)
        text=await message.channel.send(embed=embedVar)
      await text.add_reaction('⏮️')
      await text.add_reaction('◀️')
      await text.add_reaction('▶️')
      await text.add_reaction('⏭️')
      while time.time() < timeout_start + timeout:
        try:
          text = await text.channel.fetch_message(text.id)
          count_n, count_p, count_pp, count_this=0, 0, 0, 0
          for reaction in text.reactions:
            if(reaction.emoji == '◀️'):
              count_n=reaction.count-1
            elif(reaction.emoji == '▶️'):
              count_p=reaction.count-1
            elif(reaction.emoji == '⏮️'):
              count_nn=reaction.count-1
            elif(reaction.emoji == '⏭️'):
              count_pp=reaction.count-1
            if(count_n==1 and count!=0): 
              await text.delete()
              timeout_start = time.time()
              count-=1
              break
            elif(count_p==1 and count!=4): 
              await text.delete()
              timeout_start = time.time()
              count+=1
              break
            elif(count_nn==1): 
              await text.delete()
              timeout_start = time.time()
              count=0
              break
            elif(count_pp==1): 
              await text.delete()
              timeout_start = time.time()
              count=4
              break
        except: break
    await text.remove_reaction('◀️', client.get_user(text.author.id))  
    await text.remove_reaction('▶️', client.get_user(text.author.id))
    await text.remove_reaction('⏮️', client.get_user(text.author.id))
    await text.remove_reaction('⏭️', client.get_user(text.author.id))

  elif(message.content.startswith('-id add')):
    PES_ID=str()
    for x in message.content:
      if(x.isdigit()): PES_ID+=x
    username=message.author.name
    userid=str(message.author.id)
    User={
      "PES_ID": PES_ID,
      "Username": username
    }
    if(len(PES_ID)==9 and PES_ID.isdecimal()):
      ref1.child(userid).set(User)
      await message.reply(f'Your ID has now been registered')
    else: await message.reply(f'Please enter a 9 digit PES ID in the format: \n'
    f'**-id add 123456789**')

  elif(message.content.startswith('-id delete')):
    userid=str(message.author.id)
    try:
      ref1.child(userid).delete()
      await message.reply(f'Your user ID has been deleted from my storage')
    except: await message.reply(f'Your ID was not stored with the bot in the first place')

  elif(message.content.startswith('-id update')):
    userid=str(message.author.id)
    PES_ID=str()
    for x in message.content:
      if(x.isdigit()): PES_ID+=x
    username=message.author.name
    if(len(PES_ID)==9 and PES_ID.isdecimal()):
        ref1.child(userid).update({"Username": username})
        ref1.child(userid).update({"PES_ID":PES_ID})
        await message.reply(f'Your ID has been updated')
    else: await message.reply(f'Please enter a 9 digit PES ID in the format: \n'
    f'**-id update 123456789**')
  
  elif(message.content.startswith('-id') or message.content.startswith('-id get')):
    if(message.content=='-id' or message.content=='-get id'): 
      userid=str(message.author.id)
      PES_ID=ref1.get().get(userid).get('PES_ID')
      await message.reply(f'Your PES ID is {PES_ID}')
    else:  
      try:
        temp = re.findall(r"\d+", message.content)
        userid = str(list(map(int, temp))).replace("[","").replace("]","")
        PES_ID=ref1.get().get(userid).get('PES_ID')
        await message.reply(f'Your requested ID is {PES_ID}')
      except: await message.reply(f'The tagged user has not registered their ID with me yet')
  
  elif(message.content.startswith('-friendly')):
    embedVar=discord.Embed(title=f'{message.author.display_name} is looking for a friendly', description='Press the emote below to accept', color=0xf1c40f)
    text= await message.channel.send(embed=embedVar)
    try: 
      PES_ID=ref1.get().get(str(message.author.id)).get('PES_ID')
      await text.add_reaction('🆔')
    except: 
      await text.add_reaction('✅')
    timeout = 86400   # [seconds]
    timeout_start = time.time()
    flag=0
    while time.time() < timeout_start + timeout:
      if(flag==1): break
      reaction, user=await client.wait_for('reaction_add')
      print(reaction.emoji)
      if(reaction.emoji == '✅' and reaction.message.id==text.id):
        if(user.id!=client.user.id and user.id!= message.author.id): 
          await message.channel.send(f"{user.mention} has accepted {message.author.mention}'s challenge. This where you exchange IDs and stuff.")
          await text.delete()
          flag=1
      
      elif(reaction.emoji == '🆔'and reaction.message.id==text.id):
        if(user.id!=client.user.id and user.id!= message.author.id):
          await message.channel.send(f" {user.mention} has accepted the challenge. {message.author.mention}'s ID is {PES_ID}")
          await text.delete()
          flag=1    
  
  
  elif(message.content.startswith('-pulliconic') or message.content.startswith('-pullim') or message.content.startswith('-pull im') or message.content.startswith('-pull iconic') or message.content.startswith('-pack iconic') or message.content.startswith('-packiconic') or message.content.startswith('-packim') or message.content.startswith('-pack im')):
    IM_index=random.randint(1,143)
    IM_Name=ref3.get()[IM_index].get('Name')
    IM_Position=ref3.get()[IM_index].get('Position')
    IM_Rating=ref3.get()[IM_index].get('Rating')
    IM_Image=ref3.get()[IM_index].get('Image_URL')
    IM_Link=ref3.get()[IM_index].get('Player_URL')
    text=await message.reply(f'https://imgur.com/a/QfG4DbN')
    embedVar=discord.Embed(title=f'{message.author.display_name}, you packed:',
    description=f'**{IM_Name}**\nPosition: **{IM_Position}**\nRating: **{IM_Rating}**\n**[Link]({IM_Link})**\n', color=0xf1c40f)
    embedVar.set_image(url=IM_Image)
    embedVar.set_thumbnail(url=f'https://media.discordapp.net/attachments/723015304439136316/836309933317685319/iconic1.gif')
    await asyncio.sleep(7)
    await text.delete()
    await message.channel.send(embed=embedVar)

  elif(message.content.startswith('-pulllegend') or message.content.startswith('-pull legend') or message.content.startswith('-pack legend') or message.content.startswith('-packlegend')):
    legend_index=random.randint(1,87)
    legend_Name=ref4.get()[legend_index].get('Name')
    legend_Position=ref4.get()[legend_index].get('Position')
    legend_Rating=ref4.get()[legend_index].get('Rating')
    legend_Image=ref4.get()[legend_index].get('Image_URL')
    legend_Link=ref4.get()[legend_index].get('Player_URL')
    text=await message.reply(f'https://imgur.com/a/vUBZap7')
    embedVar=discord.Embed(title=f'{message.author.display_name}, you packed:',
    description=f'**{legend_Name}**\nPosition: **{legend_Position}**\nRating: **{legend_Rating}**\n**[Link]({legend_Link})**\n', color=0xf1c40f)
    embedVar.set_image(url=legend_Image)
    embedVar.set_thumbnail(url=f'https://media.discordapp.net/attachments/788705918589468674/836131117861437450/legends_gif.gif?width=406&height=406')
    await asyncio.sleep(7)
    await text.delete()
    await message.channel.send(embed=embedVar)    
  
  elif(message.content.startswith('-pull') or message.content.startswith('-pack')):
    index=random.randint(1,100)
    if(index<13): 
      packref=ref3
      index=random.randint(1,143)
      text=await message.reply(f'https://imgur.com/a/QfG4DbN')
      thumbnail=f'https://media.discordapp.net/attachments/723015304439136316/836309933317685319/iconic1.gif'
      t=7
    elif(index<21): 
      packref=ref4
      index=random.randint(1,87)
      text=await message.reply(f'https://imgur.com/a/vUBZap7')
      thumbnail=f'https://media.discordapp.net/attachments/788705918589468674/836131117861437450/legends_gif.gif?width=406&height=406'
      t=7
    elif(index<36): 
      index=random.randint(1,133)
      if(index<65):       packref=ref_base1
      elif(index<129):    
        packref=ref_base2
        index=str(index)
      else:               
        index=str(index)
        packref=ref_base11
      #index=str(index)  
      text=await message.reply(f'https://imgur.com/a/AC0hCTj')
      thumbnail=f'https://media.discordapp.net/attachments/733550157970538586/835481532336046130/black_ball_gif.gif'
      t=5.8
    elif(index<61):
      index=random.randint(134,698)
      if(index<293):      packref=ref_base3
      elif(index<457):    
        index=str(index)
        packref=ref_base4
      elif(index<621):    
        index=str(index)
        packref=ref_base5
      elif(index<699):    
        index=str(index)
        packref=ref_base11
      
      text=await message.reply(f'https://imgur.com/a/AC0hCTj')
      thumbnail=f'https://media.discordapp.net/attachments/733550157970538586/835481532336046130/black_ball_gif.gif'
      t=5.8
    else: 
      index=random.randint(699, 2801)
      if(index<1019):     packref=ref_base6
      elif(index<1417):   packref=ref_base7
      elif(index<1815):   packref=ref_base8
      elif(index<2213):   packref=ref_base9
      elif(index<2611):   packref=ref_base10
      elif(index<2802):   packref=ref_base11

      index=str(index)
      text=await message.reply(f'https://imgur.com/a/AC0hCTj')
      thumbnail=f'https://media.discordapp.net/attachments/733550157970538586/835481532336046130/black_ball_gif.gif'
      t=5.8
    print(index)
    Name=packref.get()[index].get('Name')
    Position=packref.get()[index].get('Position')
    Rating=packref.get()[index].get('Rating')
    Image=packref.get()[index].get('Image_URL')
    Link=packref.get()[index].get('Player_URL')
    
    embedVar=discord.Embed(title=f'{message.author.display_name}, you packed:',
    description=f'**{Name}**\nPosition: **{Position}**\nRating: **{Rating}**\n**[Link]({Link})**\n', color=0xf1c40f)
    embedVar.set_image(url=Image)
    embedVar.set_thumbnail(url=thumbnail)
    await asyncio.sleep(t)
    await text.delete()
    await message.channel.send(embed=embedVar)

  elif(message.content.startswith('-scout')):
    name=message.content[7:].replace('scouts', 'scout')

    player_name, player_pos, player_ovr, img_link, scoutlist=scouts(name)
    count=0
    flag=0
    print(len(scoutlist))
    pagecount=((len(scoutlist) + 9) // 10)
    timeout = 60   # [seconds]
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
      if(flag==1): break
      desc=''
      endlist=count*10 + 10
      if(count==pagecount-1): endlist=count*10+ len(scoutlist)%10
      print(endlist, pagecount, count)
      for x in range(count*10, endlist):
        desc+=f'{scoutlist[x][0]}    {scoutlist[x][1]} {scoutlist[x][2]} {scoutlist[x][3]} \n'
      embedVar=discord.Embed(title=f'{player_name}, {player_pos}, {player_ovr}', color=0xf1c40f)
      for x in range(count*10, endlist):
        embedVar.add_field(name=f'{scoutlist[x][0]}    {scoutlist[x][1]} {scoutlist[x][2]} {scoutlist[x][3]}', value='\u200b', inline=True)
      
      #embedVar.add_field(name=desc, value='\a', inline=True)
      embedVar.set_thumbnail(url=img_link)
      embedVar.set_footer(text=f'Page {count+1} of {pagecount}')
      text=await message.channel.send(embed=embedVar)
      await text.add_reaction('⏮️')
      await text.add_reaction('◀️')
      await text.add_reaction('▶️')
      await text.add_reaction('⏭️')
      while time.time() < timeout_start + timeout:
        try:
          if(flag==1): break
          text = await text.channel.fetch_message(text.id)
          count_n, count_p, count_nn, count_pp, count_this=0, 0, 0, 0, 0
          for reaction in text.reactions:
            if(reaction.emoji == '◀️'):
              count_n=reaction.count-1
            elif(reaction.emoji == '▶️'):
              count_p=reaction.count-1
            elif(reaction.emoji == '⏮️'):
              count_nn=reaction.count-1
            elif(reaction.emoji == '⏭️'):
              count_pp=reaction.count-1
            if(count_n==1 and count!=0): 
              await text.delete()
              timeout_start = time.time()
              count-=1
              break
            elif(count_p==1 and count!=pagecount-1): 
              await text.delete()
              timeout_start = time.time()
              print('+++++++++++++')
              count+=1
              break
            elif(count_nn==1): 
              await text.delete()
              timeout_start = time.time()
              count=0
              break
            elif(count_pp==1): 
              await text.delete()
              timeout_start = time.time()
              count=pagecount-1
              break
        except: break
    await text.remove_reaction('◀️', client.get_user(text.author.id))  
    await text.remove_reaction('▶️', client.get_user(text.author.id))
    await text.remove_reaction('⏮️', client.get_user(text.author.id))
    await text.remove_reaction('⏭️', client.get_user(text.author.id))
    
TOKEN="ENTER TOKEN HERE"
client.run(TOKEN)
