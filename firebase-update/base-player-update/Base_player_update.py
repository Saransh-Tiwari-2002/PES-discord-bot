# coding=utf8
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

cred_obj2 = firebase_admin.credentials.Certificate('baseplayer.json')
app2 = firebase_admin.initialize_app(cred_obj2, {'databaseURL':'https://base-player-database-default-rtdb.firebaseio.com/'})
ref2=db.reference('/')


flag=0
if(flag==0):
    a=''''''
name_list, pos_list, rating_list, img_list, url_list=[], [], [], [], []
list1=[m.start() for m in re.finditer('</a></td><td class="nontext" sorttable_customkey=', a)]
list2=[m.start() for m in re.finditer('span class="squad-table-pos squad-table-', a)]
list3=[m.start() for m in re.finditer("""</span></td>
				<td class="nontext squad-table-stat-col"><span class="stat_tier_""", a)]
list4=[m.start() for m in re.finditer(' src="https://pesmaster.fra1.cdn.digitaloceanspaces.com/players/pes-2021/player_', a)]
list5=[m.start() for m in re.finditer('<a target="_blank" class="namelink" href="', a)]

for x in list1:
    start=a[:x].rfind('>')+1
    name_list.append(a[start:x])

for x in list2:
    temp=a[x:]
    start=temp.find('>')+1
    end=temp.find('<')
    pos_list.append(temp[start:end])

for x in list3:
    temp=a[x:]
    start=temp.find('squad-table-stat">')+18
    end=start+2
    start2=start+98
    end2=temp[start2:].find('<')
    rating=temp[start:end]+' - '+temp[start2:end2+start2]
    rating_list.append(rating)
    #print(rating)

for x in list4:
    temp=a[x+6:]
    end=temp.find('.png')+4
    img_link=temp[:end]
    img_list.append(img_link)
    #print(img_link)

for x in list5:
    temp=a[x:]
    start=temp.find('/')
    end=temp.find('">')   
    url=f'https://www.pesmaster.com{temp[start:end]}'
    #print(url)
    url_list.append(url)

print(name_list[330], pos_list[330], rating_list[330], img_list[330], url_list[330])
for count in range(1, 2802):
    ref2.child(str(count)).update({'Name':name_list[count-1]})
    ref2.child(str(count)).update({'Position':pos_list[count-1]})
    ref2.child(str(count)).update({'Rating':rating_list[count-1]})
    ref2.child(str(count)).update({'Image_URL':img_list[count-1]})
    ref2.child(str(count)).update({'Player_URL':url_list[count-1]})