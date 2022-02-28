import csv
import difflib
from PIL import Image, ImageDraw, ImageFont
import random
import time
import os
import asyncio
import discord
import requests
from bs4 import BeautifulSoup
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import re
from datetime import date
import json
import time
import unidecode
import difflib

cred_obj1 = firebase_admin.credentials.Certificate('FB_json.json')
app1 = firebase_admin.initialize_app(cred_obj1, {'databaseURL':'Enter Database URL here'})
ref1=db.reference('/')

cred_obj3 = firebase_admin.credentials.Certificate('IM.json')
app3 = firebase_admin.initialize_app(cred_obj3, {'databaseURL':'Enter Database URL here'}, name='app3')
ref3=db.reference('/', app3)

cred_obj4 = firebase_admin.credentials.Certificate('legend.json')
app4 = firebase_admin.initialize_app(cred_obj4, {'databaseURL':'Enter Database URL here'}, name='app4')
ref4=db.reference('/', app4)

cred_obj_backup= firebase_admin.credentials.Certificate('manager-27.json')
app_backup = firebase_admin.initialize_app(cred_obj_backup, {'databaseURL':'Enter Database URL here'}, name='app_backup')
ref_backup=db.reference('/', app_backup)

cred_obj_base1 = firebase_admin.credentials.Certificate('base1.json')
app_base1 = firebase_admin.initialize_app(cred_obj_base1, {'databaseURL':'Enter Database URL here'}, name='app_base1')
ref_base1=db.reference('/', app_base1)

cred_obj_base2 = firebase_admin.credentials.Certificate('base2.json')
app_base2 = firebase_admin.initialize_app(cred_obj_base2, {'databaseURL':'Enter Database URL here'}, name='app_base2')
ref_base2=db.reference('/', app_base2)

cred_obj_base3 = firebase_admin.credentials.Certificate('base3.json')
app_base3 = firebase_admin.initialize_app(cred_obj_base3, {'databaseURL':'Enter Database URL here'}, name='app_base3')
ref_base3=db.reference('/', app_base3)

cred_obj_base4 = firebase_admin.credentials.Certificate('base4.json')
app_base4 = firebase_admin.initialize_app(cred_obj_base4, {'databaseURL':'Enter Database URL here'}, name='app_base4')
ref_base4=db.reference('/', app_base4)

cred_obj_base5 = firebase_admin.credentials.Certificate('base5.json')
app_base5 = firebase_admin.initialize_app(cred_obj_base5, {'databaseURL':'Enter Database URL here'}, name='app_base5')
ref_base5=db.reference('/', app_base5)

cred_obj_base6 = firebase_admin.credentials.Certificate('base6.json')
app_base6 = firebase_admin.initialize_app(cred_obj_base6, {'databaseURL':'Enter Database URL here'}, name='app_base6')
ref_base6=db.reference('/', app_base6)

cred_obj_base7 = firebase_admin.credentials.Certificate('base7.json')
app_base7 = firebase_admin.initialize_app(cred_obj_base7, {'databaseURL':'Enter Database URL here'}, name='app_base7')
ref_base7=db.reference('/', app_base7)

cred_obj_base8 = firebase_admin.credentials.Certificate('base8.json')
app_base8 = firebase_admin.initialize_app(cred_obj_base8, {'databaseURL':'Enter Database URL here'}, name='app_base8')
ref_base8=db.reference('/', app_base8)

cred_obj_base9 = firebase_admin.credentials.Certificate('base9.json')
app_base9 = firebase_admin.initialize_app(cred_obj_base9, {'databaseURL':'Enter Database URL here'}, name='app_base9')
ref_base9=db.reference('/', app_base9)

cred_obj_base10 = firebase_admin.credentials.Certificate('base10.json')
app_base10 = firebase_admin.initialize_app(cred_obj_base10, {'databaseURL':'Enter Database URL here'}, name='app_base10')
ref_base10=db.reference('/', app_base10)

cred_obj_base11 = firebase_admin.credentials.Certificate('base11.json')
app_base11 = firebase_admin.initialize_app(cred_obj_base11, {'databaseURL':'Enter Database URL here'}, name='app_base11')
ref_base11=db.reference('/', app_base10)

pos_coordinates=[[66.14035087719299, 22.73972602739726, 30.4093567251462, 7.579908675799087], [55.49707602339181, 22.73972602739726, 30.4093567251462, 8.337899543378995], [55.49707602339181, 3.7899543378995433, 15.2046783625731, 18.949771689497716], [55.49707602339181, 56.84931506849315, 15.2046783625731, 18.949771689497716], [44.853801169590646, 22.73972602739726, 30.4093567251462, 8.337899543378995], [34.21052631578947, 22.73972602739726, 30.4093567251462, 8.337899543378995], [23.567251461988302, 3.7899543378995433, 15.2046783625731, 29.561643835616437], [23.567251461988302, 56.84931506849315, 15.2046783625731, 29.561643835616437], [23.567251461988302, 22.73972602739726, 30.4093567251462, 8.337899543378995], [2.280701754385965, 3.7899543378995433, 15.2046783625731, 18.949771689497716], [2.280701754385965, 56.84931506849315, 15.2046783625731, 18.949771689497716], [12.923976608187134, 22.73972602739726, 30.4093567251462, 8.337899543378995], [2.280701754385965, 22.73972602739726, 30.4093567251462, 8.337899543378995]]
pos_list=['GK', 'CB', 'LB', 'RB','DMF', 'CMF', 'LMF', 'RMF', 'AMF', 'LWF', 'RWF', 'SS', 'CF']


with open('csv_file.csv',errors="ignore", newline='') as csvfile:
    spamreader_manager = list(csv.reader(csvfile, delimiter=','))
    namelist_manager=[]
    for row in spamreader_manager[:-1]:
        namelist_manager.append(row[1].lower().replace(' ', '-').replace('.','-').replace('--', '-'))


with open('1a.csv',errors="ignore", newline='') as csvfile:
    spamreader = list(csv.reader(csvfile, delimiter=','))
    namelist=[]
    for row in spamreader[:-1]:
        namelist.append(row[1].lower().replace(' ', '-').replace('.','-').replace('--', '-'))


def get_manager(query, querytype=1):        #-manager, -offensive, -defensive, -formation
    temp=[]
    for row in spamreader_manager[:-1]:
        if query in row[querytype].lower().replace(' ', '-').replace('.','-').replace('--', '-'):
            temp.append(row[:-1])
    if(len(temp)==0):
        if(query.count('-')>0):
            return  get_manager(query[query.index('-')+1:], querytype)
        return  get_manager(difflib.get_close_matches(query, namelist)[0], querytype)
    temp.sort(key= lambda x: int(x[3]), reverse=True)
    return temp[0], bool(len(temp))

def get_random_name():
    name=''
    for x in range(20):
        name+=chr(random.randint(97, 122))
    print(name)
    return name

def get_colour(rating):
    if(rating>=95): return '#00ebff'
    elif(rating>=85): return '#22ff00'
    elif(rating>=75): return '#ffe600'
    elif(rating>=60): return '#ff9a00'
    else: return '#ff0000'


def get_pic_familiarity(position_rgb, pos_rating_list):
    print(type(pos_rating_list))
    temp_rgb=position_rgb.replace('[', '').replace(']', '').replace("'",'').replace(' ', '').split(",")
    position_rgb=[]
    for x in range(0, len(temp_rgb), 3):
        position_rgb.append(temp_rgb[x:x+3])
    pos_rating_list=pos_rating_list.replace('[', '').replace(']', '').replace("'",'').replace(' ', '').split(",")
    print(position_rgb)
    img = Image.open('pos_rating.png', 'r')
    print(img.size)
    basewidth = 130
    #img = Image.open('somepic.jpg')
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    print(basewidth, hsize, '------')
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    count=0
    for pos in position_rgb:
        draw =ImageDraw.Draw(img)
        #shape=[(pos_coordinates[count][1]*1.72)-2.5, pos_coordinates[count][0]*2.17, (pos_coordinates[count][2]+pos_coordinates[count][1])*1.72, (pos_coordinates[count][3]+pos_coordinates[count][0])*2.17]
        shape=[(pos_coordinates[count][1]*1.72)-2.5, pos_coordinates[count][0]*2.17, (pos_coordinates[count][2]+pos_coordinates[count][1])*1.72, (pos_coordinates[count][3]+pos_coordinates[count][0])*2.17]

        print(shape)
        draw.rectangle(shape, fill =(int(pos[0]), int(pos[1]), int(pos[2])), outline ='white')
        width, height = shape[2]+shape[0], shape[3]+shape[1]
        draw.rounded_rectangle([width/2-10, height/2-6,width/2+9, height/2+5], 2, fill ='black', outline ='black')
        draw.text((width/2, height/2+1.5), pos_rating_list[count], font=ImageFont.truetype("calibri.ttf", 13), fill=get_colour(int(pos_rating_list[count])), anchor="mm")
        count+=1
    temp_img_name=get_random_name()
    img.save(f'{temp_img_name}.png')
    print(temp_img_name)
    #img.save('efootball.png')
    #time.sleep(20)
    return temp_img_name


def sex():
    new_l=[]
    for x in pos_coordinates:
        #new_l.append([x[0]*0.584795, x[1]*0.58447489, x[2]*0.584795, x[3]*0.58447489])
        new_l.append([x[0]*130/171, x[1]*166/219, x[2]*130/171, x[3]*166/219])
    print(new_l)
#sex()

#By name:    query=query.lower().replace(' ', '-').replace('.','-').replace('--', '-')\
#By Format
def text_search(query, querytype=1):
    query=query.lower().replace(' ', '-').replace('.','-').replace('--', '-')
    temp=[]
    for row in spamreader[:-1]:
        if query in row[1].lower().replace(' ', '-').replace('.','-').replace('--', '-'):
            temp.append(row[:-1])
    if(len(temp)==0):
        if(query.count('-')>0):
            return text_search(query[query.index('-')+1:], querytype)
        return text_search(difflib.get_close_matches(query, namelist)[0], querytype)
    temp.sort(key= lambda x: int(x[7]), reverse=True)
    return temp, bool(len(temp))

client = discord.Client(activity=discord.Game(name="-peshelp"))



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
      manager_info=get_manager(name.lower().replace(' ', '-').replace('.','-').replace('--', '-'))
      manager_name=manager_info[1]
      formation_temp=manager_info[2].replace('--', '-')
      manager_skill=manager_info[3]
      manager_cost=manager_info[4]
      offensive_tactics=manager_info[5:17]
      defensive_tactics=manager_info[17:]
    else: 
      query, sum=str(),0 
      for x in message.content:
        if(x.isdigit()):
          query+=x+'-'
          sum+=int(x)   #4-3-3-     4-2-2-2-
      if(len(query)==6 or len(query)==8): 
        if(sum==10):  
          manager_info=get_manager(query[:-1], 2)
          manager_name=manager_info[1]
          formation_temp=manager_info[2].replace('--', '-')
          manager_skill=manager_info[3]
          manager_cost=manager_info[4]
          offensive_tactics=manager_info[5:17]
          defensive_tactics=manager_info[17:]
          embedVar=discord.Embed(title=f'Parent URL---{query[:-1]}', color=0xf1c40f)
          await message.reply(embed=embedVar)

  elif(message.content.startswith('-player')):
    plist, flag_ban=text_search(message.content[8:])            
    if(flag_ban==True):
      count=0
      flag=0
      timeout = 20   # [seconds]
      timeout_start = time.time()
      while time.time() < timeout_start + timeout:
        if(flag==1): break
        player_ID=plist[count][0]
        player_name=plist[count][1]
        print(player_name)
        player_ovr=plist[count][7]
        player_pos=plist[count][3]
        if(plist[count][2]=='Base'):
            img_link=f'https://novasoftwarestudio.online/peshub21/Images/Players/{player_ID}.png'  
        else:
            img_link=f'https://novasoftwarestudio.online/peshub21/Images/Players/{player_ID}_l.png'
        img_thumbnail=f'https://novasoftwarestudio.online/peshub21/Images/Players/{player_ID}.png'
        #url_player_name=player_name.lower().replace(' ', '-').replace('.','-').replace('--','-')
        #player_link=f'https://efootballhub.net/pes21/player/{player_ID}'
        #player_link=f'Parent URL{player_ID}'
        embedVar=discord.Embed(title=f'{count+1}.  {player_name}, {player_pos}, {player_ovr}', color=0xf1c40f)
        embedVar.set_image(url=img_link)
        text=await message.channel.send(embed=embedVar)
        if(count>0):
            await text.add_reaction('⏮️')
            await text.add_reaction('◀️')
        await text.add_reaction('⬛')
        if(count<len(plist)-1): 
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
                if(flag_ban==True):
                  await text.delete()
                  ##############SECOND MENU STARTS#########################
                  
                  count1=0
                  timeout1 = 60   # [seconds]
                  timeout_start1 = time.time()
                  while time.time() < timeout_start1 + timeout1:
                    print('siiiiiii')
                    print(count1)
                    if(count1==0):  
                      if(player_pos!='0'):  
                        embed2=discord.Embed(title=f'{player_name}, {player_pos}, {player_ovr}',
                        #description=f'{plist[count][17:38]} \n{player_link}', color=0xf1c40f)
                        description=f'**Attacking** \nOffensive Awareness: **{plist[count][15]}** \nBall Control: **{plist[count][16]}** \nDribbling: **{plist[count][17]}** \nTight Possession: **{plist[count][18]}**'
                        f'\nLow Pass: **{plist[count][19]}** \nLofted Pass: **{plist[count][20]}** \nFinishing: **{plist[count][21]}**  \nPlace Kicking: **{plist[count][23]}** \nCurl: **{plist[count][24]}**'
                        f'\nHeading: **{plist[count][22]}**\n\n**Athletiscism**\nSpeed: **{plist[count][37]}** \nAcceleration: **{plist[count][38]}** \nKicking Power: **{plist[count][39]}** \nJump: **{plist[count][34]}** \nPhysical Contact: **{plist[count][25]}**'
                        f'\nBalance: **{plist[count][35]}** \nStamina: **{plist[count][36]}** \n\n**Defending** \nDefensive Awareness: **{plist[count][26]}** \nBall Winning: **{plist[count][27]}** \nAggression: **{plist[count][28]}**', color=0xf1c40f)
                        embed2.set_thumbnail(url=img_thumbnail)
                      else:
                        embed2=discord.Embed(title=f'{player_name}, {player_pos}',
                        #description=f'{plist[count][38:42]} \n{player_link}', color=0xf1c40f) 
                        description=f'**GoalKeeeping** \nGK Awareness: **{plist[count][29]}** \nGK Catching: **{plist[count][30]}** \nGK Clearing: **{plist[count][31]}** \nGK Reflexes: **{plist[count][32]}** \nGK Reach: **{plist[count][33]}**', color=0xf1c40f) 
                        embed2.set_thumbnail(url=img_thumbnail)
                      text1=await message.channel.send(embed=embed2)
                        
                    elif(count1==1):
                      print('check0')
                      embed2=discord.Embed(title=f'{player_name}, {player_pos}, {player_ovr}', color=0xf1c40f)
                      print('check1') 
                      #embed2.add_field(name=f'\u200b\nNationality: {plist[count][2]}', value='\u200b', inline=True)
                      player_condition=plist[count][5]
                      #embed2.add_field(name=f"\u200b\nNationality: {CountryCode.get(plist[count][7])} \nStronger Foot: {['Right', 'Left'][int(plist[count][12])]} \nHeight: {plist[count][9]}cm \nCondition: {player_condition} \nWeak Foot Usage: {plist[count][53]} \nWeak Foot Acc: {plist[count][54]} \nForm: {plist[count][55]} \nInjury Resistance: {plist[count][56]}", value='\u200b', inline=True)
                      embed2.add_field(name=f'\u200b\nPlaying Style', value=plist[count][4], inline=True)
                      print('check3')
                      temp_skills=plist[count][11].replace(', ', '\n').replace("'", "").replace("[", "").replace("]", "")
                      skill_count=temp_skills.count('\n')+1
                      print('check4')
                      embed2.add_field(name=f"\u200b\nPlayer Skills- {skill_count}", value=temp_skills, inline=True)
                      COM_playing_styles=plist[count][12].replace(', ', '\n').replace("'", "").replace("[", "").replace("]", "")
                      skill_count=COM_playing_styles.count('\n')+1

                      embed2.add_field(name=f'\u200b\nCOM Playing Styles:', value=COM_playing_styles, inline=True)
                      #skill_counter=additional_info[1].count('\n')+1 if additional_info[1].count('\n')!=10 else 10
                      embed2.set_thumbnail(url=img_thumbnail)
                      
                      temp_img_name=get_pic_familiarity(plist[count][14], plist[count][13])
                      file = discord.File(f"{temp_img_name}.png", filename=f"{temp_img_name}.png")
                      embed2.set_image(url=f"attachment://{temp_img_name}.png")
                      print('check5')
                      print(temp_skills, skill_count)
                      text1=await message.channel.send(file=file, embed=embed2)
                    #os.remove(f'{temp_img_name}.png')
                    print('check6')
                    if(count1==1):   await text1.add_reaction('◀️')
                    if(count1==0):   await text1.add_reaction('▶️')
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
                            print('HELLLLLLLL') 
                            await text1.delete()
                            timeout_start1 = time.time()
                            print('here')
                            count1=1
                            break
                      except: break
                  if(count1==1):    await text1.remove_reaction('◀️', client.get_user(text1.author.id))
                  elif(count1==0):  await text1.remove_reaction('▶️', client.get_user(text1.author.id))       
                                              
                else:
                  err=client.get_channel(int(879789398235947049))
                  await err.send('<@694568372331085884> change {0.user}'.format(client))
                break
              if(count_n==1 and count!=0): 
                print('sexyy')
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
                print('sex')
                await text.delete()
                timeout_start = time.time()
                count=0
                break
              elif(count_pp==1): 
                print('sexx')
                await text.delete()
                timeout_start = time.time()
                count=len(plist)-1
                break
          except: break
      await text.delete()
      await message.reply(f'Oops, the bot timed out. Please respond within 20 seconds next time.')
    else: 
      err=client.get_channel(int(879789398235947049))
      await err.send('<@694568372331085884> change {0.user}'.format(client))
  
  elif(message.content.startswith('-featured') or message.content.startswith('-ft')):
    plist, flag_ban=latest_featured()
    if(flag_ban==True):
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
                dic, additional_info, flag_ban=get_player_stats(player_link)
                if(flag_ban==True):
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
                      embed2.add_field(name=f'\u200b\nNationality: {additional_info[3]} \nStronger Foot: {additional_info[4]} \nHeight: {additional_info[5]}cm \nCondition: {additional_info[6]} \nWeak Foot Usage: {additional_info[7]} \nWeak Foot Acc: {additional_info[8]} \nForm: {additional_info[9]} \nInjury Resistance: {additional_info[10]}', value='\u200b', inline=True)
                      embed2.add_field(name=f'Playing Style', value=additional_info[0], inline=True)
                      skill_counter=additional_info[1].count('\n')+1 if additional_info[1].count('\n')!=10 else 10
                      embed2.add_field(name=f'\u200b\nPlayer Skills- {skill_counter}', value=additional_info[1], inline=True)
                      embed2.add_field(name=f'\u200b\nCOM Playing Styles', value=additional_info[2], inline=True)
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
                else:
                  err=client.get_channel(int(879789398235947049))
                  await err.send('<@694568372331085884> change {0.user}'.format(client))                                 
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
    else:
      err=client.get_channel(int(879789398235947049))
      await err.send('<@694568372331085884> change {0.user}'.format(client))
      
  elif(message.content.startswith('-condition')): 
    name=message.content[11:]
    plist, flag_ban=text_search(name)
    if(flag_ban):
      await message.reply(f'**{plist[0][1]}** has condition {plist[0][5]} for this week')
  
  elif(message.content.startswith('-offensive') or message.content.startswith('-attacking')):
    name=message.content[11:]
    manager_info=get_manager(name.lower().replace(' ', '-').replace('.','-').replace('--', '-'))
    name, [Attacking_Style,Build_Up,Attacking_Area,Positioning,Support_Range, NumbersInAttack, Defensive_Style,Containment_Area,Pressuring,Defensive_Line,Compactness, NumbersInDefense]=manager_info[1], manager_info[5:17]
    if(Build_Up!=None): 
      embedVar=discord.Embed(title=f'Offensive tactics of `{name}` are:\n', description=
      f'\u200b\nAttacking Style:                     {Attacking_Style}'
      f'\nBuild Up:                                  {Build_Up}'
      f'\nAttacking Area:                     {Attacking_Area}'
      f'\nPositioning:                             {Positioning}'
      f'\nSupport Range:                      {Support_Range}'
      f'\nNumbers in Attack:              {NumbersInAttack}'
      f'\nDefensive Style:                     {Defensive_Style}'
      f'\nContainment Area:               {Containment_Area}'
      f'\nPressuring:                              {Pressuring}'
      f'\nDefensive Line:                      {Defensive_Line}'
      f'\nCompactness:                        {Compactness}'
      f'\nNumbers in Defence:           {NumbersInDefense}', color=0xf1c40f)
      await message.channel.send(embed=embedVar)
    
  
  elif(message.content.startswith('-defensive')):
    name=message.content[11:]
    manager_info=get_manager(name.lower().replace(' ', '-').replace('.','-').replace('--', '-'))
    name, [Attacking_Style,Build_Up,Attacking_Area,Positioning,Support_Range, NumbersInAttack, Defensive_Style,Containment_Area,Pressuring,Defensive_Line,Compactness, NumbersInDefense]=manager_info[1], manager_info[17:]
    if(Build_Up!=None): 
      embedVar=discord.Embed(title=f'Defensive tactics of `{name}` are:\n', description=
      f'\u200b\nAttacking Style:                     {Attacking_Style}'
      f'\nBuild Up:                                  {Build_Up}'
      f'\nAttacking Area:                     {Attacking_Area}'
      f'\nPositioning:                             {Positioning}'
      f'\nSupport Range:                      {Support_Range}'
      f'\nNumbers in Attack:              {NumbersInAttack}'
      f'\nDefensive Style:                     {Defensive_Style}'
      f'\nContainment Area:               {Containment_Area}'
      f'\nPressuring:                              {Pressuring}'
      f'\nDefensive Line:                      {Defensive_Line}'
      f'\nCompactness:                        {Compactness}'
      f'\nNumbers in Defence:           {NumbersInDefense}', color=0xf1c40f)
      await message.channel.send(embed=embedVar)

  elif(message.content.startswith('-formation')):
    name=message.content[11:]
    if(name.replace(' ','').replace('.','').isalpha()):
      print('test1')
      manager_info=get_manager(name.lower().replace(' ', '-').replace('.','-').replace('--', '-'))
      name, formation, skill= manager_info[1], manager_info[2].replace('--','-'), manager_info[3]
      print(name, formation, skill)
      if(formation!= None):
        await message.reply(f'Manager **{name}**({skill}) has formation **{formation}** this week')
    else: 
      query, sum=str(),0 
      for x in message.content:
        if(x.isdigit()):
          query+=x+'-'
          sum+=int(x)   #4-3-3-     4-2-2-2-
      if(len(query)==6 or len(query)==8): 
        if(sum==10):  
          manager_info=get_manager(query[:-1], 2)
          manager_name=manager_info[1]
          formation_temp=manager_info[2].replace('--', '-')
          manager_skill=manager_info[3]
          manager_cost=manager_info[4]
          offensive_tactics=manager_info[5:17]
          defensive_tactics=manager_info[17:]
          embedVar=discord.Embed(title=f'Parent URL---{query[:-1]}', color=0xf1c40f)
          await message.reply(embed=embedVar)


  #elif(message.content.startswith('-position')):
   # text=message.content[10:].replace(' ','')
    #card, pos, playstyle, card_type, pos_type, playstyle_type=advanced_search(text)
        #await message.reply('REDACTED🤬')
    #embedVar=discord.Embed(title=f'{message.author.display_name}, here are your search results',
    #description=f'Card Type: {card_type}\nPosition: {pos_type}\nPlaystyle: {playstyle_type}', color=0xf1c40f)
    #await message.reply(embed=embedVar)
    '''
    embedVar=discord.Embed(title=f'{message.author.display_name}, here are your search results',
    description=f'[Card Type: {card_type}\nPosition: {pos_type}\nPlaystyle: {playstyle_type}](https://www.pesmaster.com/pes-2021/search/?{card}{pos}{playstyle}sort=ovr&sort_order=desc)', color=0xf1c40f)
    await message.reply(embed=embedVar)'''

  #elif(message.content.startswith('-playstyle')):
   # text=message.content[11:].replace(' ','')
    #card, pos, playstyle, card_type, pos_type, playstyle_type=advanced_search(text)
        #await message.reply('REDACTED🤬')
    #embedVar=discord.Embed(title=f'{message.author.display_name}, here are your search results',
    #description=f'Card Type: {card_type}\nPosition: {pos_type}\nPlaystyle: {playstyle_type}', color=0xf1c40f)
    #await message.reply(embed=embedVar)
    '''embedVar=discord.Embed(title=f'{message.author.display_name}, here are your search results',
    description=f'[Card Type: {card_type}\nPosition: {pos_type}\nPlaystyle: {playstyle_type}](https://www.pesmaster.com/pes-2021/search/?{card}{pos}{playstyle}sort=ovr&sort_order=desc)', color=0xf1c40f)
    await message.reply(embed=embedVar)'''

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
    description='To get the formation of a manager, use **-formation**\n Example: **-formation Rossi**\n\nTo search for all managers with a particular formation, use **-formation**\n Example: **-formation 433**\n', color=0xf1c40f)
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
    'To get the formation of a manager, use -formation\n Example: **-formation Rossi**\n\nTo search for all managers with a particular formation, use **-formation**\n Example: **-formation 433**\n',
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
        embedVar.add_field(name="-invite \n-manager \n-formation \n-offensive \n-defensive \n-player \n-condition \n-position \n-playstyle \n-featured \n-scout \n-friendly \n-id get \n-id add \n-id update \n-id delete \n-pull IM \n-pull legend \n-pack", value='\u200b', inline=True)
        text=await message.channel.send(embed=embedVar)
      elif(count==1):
        embedVar = discord.Embed(title=f'_                       _ {help_title[1]}', color=0xf1c40f)
        embedVar.add_field(name=f'\n{help_commands[0]}', value=help_content[0], inline=True)
        embedVar.add_field(name=f'\u200b\n{help_commands[1]}', value=help_content[1], inline=True)
        embedVar.add_field(name=f'\u200b\n{help_commands[2]}', value=help_content[2], inline=True)
        text=await message.channel.send(embed=embedVar)
      elif(count==2):
        embedVar = discord.Embed(title=f'_                           _ {help_title[2]}', color=0xf1c40f)
        embedVar.add_field(name=f'\n{help_commands[3]}', value=help_content[3], inline=True)
        embedVar.add_field(name=f'\u200b\n{help_commands[4]}', value=help_content[4], inline=True)
        embedVar.add_field(name=f'\u200b\n{help_commands[5]}', value=help_content[5], inline=True)
        embedVar.add_field(name=f'\u200b\n{help_commands[6]}', value=help_content[6], inline=True)
        embedVar.add_field(name=f'\u200b\n{help_commands[7]}', value=help_content[7], inline=True)
        text=await message.channel.send(embed=embedVar)
      elif(count==3):
        embedVar = discord.Embed(title=f'_                              _ {help_title[3]}', color=0xf1c40f)
        embedVar.add_field(name=f'\n{help_commands[8]}', value=help_content[8], inline=True)
        embedVar.add_field(name=f'\u200b\n{help_commands[9]}', value=help_content[9], inline=True)
        embedVar.add_field(name=f'\u200b\n{help_commands[10]}', value=help_content[10], inline=True)
        embedVar.add_field(name=f'\u200b\n{help_commands[11]}', value=help_content[11], inline=True)
        embedVar.add_field(name=f'\u200b\n{help_commands[12]}', value=help_content[12], inline=True)
        text=await message.channel.send(embed=embedVar)
      elif(count==4):
        embedVar = discord.Embed(title=f'_                  _ {help_title[4]}', color=0xf1c40f)
        embedVar.add_field(name=f'\n{help_commands[13]}', value=help_content[13], inline=True)
        embedVar.add_field(name=f'\u200b\n{help_commands[14]}', value=help_content[14], inline=True)
        embedVar.add_field(name=f'\u200b\n{help_commands[15]}', value=help_content[15], inline=True)
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
      print(ref1.get().get(userid))
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
  
  elif(message.content.startswith('-id') or message.content.strip(' ').startswith('-idget')):
    if(message.content=='-id' or message.content.replace(' ','')=='-getid' or message.content.replace(' ','')=='-idget'): 
      userid=str(message.author.id)
      PES_ID=ref1.get().get(userid).get('PES_ID')
      await message.reply(PES_ID)
    else:  
      try:
        userid= re.findall(r"\d+", message.content)[0][:18]
        PES_ID=ref1.get().get(userid).get('PES_ID')
        await message.reply(PES_ID)
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
          await message.channel.send(f" {user.mention} has accepted the challenge. {message.author.mention}'s ID is: ") 
          await message.channel.send(PES_ID)
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
      
      #embedVar.add_field(name=desc, value='\u200b', inline=True)
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
