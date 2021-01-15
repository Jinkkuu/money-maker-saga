from random import randint
import time
import os
import requests
appversion=1.2
appname='Money Maker Saga'
space=' '
appcversion=3
print(str(appname)+str(space)+str(appversion))
print('Checking Version')
os.system('wget https://raw.githubusercontent.com/mojeg/money-maker-saga/main/updatechk -q')
f=open('updatechk','r')
f=f.read()
f=f.rstrip("\n")
request = requests.get('https://raw.githubusercontent.com/mojeg/money-maker-saga/main/moneymaker.py')
if request.status_code == 200:
  if int(f) > int(appcversion):
    print('UPDATE IS AVALABLE')
    print('Creating Backup')
    os.system('cp moneymaker.py moneymaker.py.bk')
    os.system('rm updatechk')
    os.system('wget https://raw.githubusercontent.com/mojeg/money-maker-saga/main/moneymaker.py --output-document=moneymaker.py')
    os.execv(__file__,'moneymaker.py')
  else:
    print('No updates UTD')
    os.system('rm updatechk')
    print('Skipping')
else:
  print('The Server is down please check back later')
  exit()


if os.path.exists("save.sav") == True:
  save=open('save.sav')
  save=save.read()
  save=save.rstrip(" \n")
  a=str(save)
else:
  a=0
os.system('clear')
#time.sleep(5)








while True:
  os.system('clear')
  print('Money:'+str('$')+str(a))
  print('Welcome!\nWhat do you want to Do?\n1.Manuel Lottery\n2.Steal\n3.Donate\n4.Auto Lottery\n5.Shop')
  ans=input()
  if ans == '4':
    while True:
      os.system('clear')
      number=str(randint(1,10))
      prize=randint(1,int(a))
      print(str(number))
      print(str('Prize:')+str(prize)+str('!'))
      if ans == str(number):
        a= int(a) + prize
        save=open('save.sav','w')
        save.write(str(a))
        print(str(a))
      else:
        print(str(a))
      time.sleep(0.05)
      
  if ans == '1':
    os.system('clear')
    number=str(randint(1,10))
    prize=randint(1,100000)
    print(str(number))
    print(str('Prize:')+str(prize)+str('!'))
    print('Pick a number:[1-10]')
    ans=input()
    if ans == str(number):
      a= int(a) + prize
      save=open('save.sav','w')
      save.write(str(a))
      print('WINNER!')
      time.sleep(1)
    else:
      print('LOST!')
      time.sleep(1)
  if ans == '2':
    os.system('clear')
    stealrate=str(randint(1,2))
    print('You:I got the money-')
    time.sleep(1)
    print('GO! GO! GO!')
    time.sleep(1)
    print('*You ran*')
    time.sleep(1)
    if stealrate == '1':
      print("*and you didn't get caught Congrats!*")
      l=randint(1,10000)
      a= int(a) + l
      print(str('+')+str(l))
      save=open('save.sav','w')
      save.write(str(a))
      input('Press enter to Continue')
    else:    
      print("*and you got caught*")
      if int(a) == 0:
        print('*You gone to jail and after that you gone back home*')
      else:
        a= int(a) - randint(1,int(a))
        save=open('save.sav','w')
        save.write(str(a))
      input('Press enter to Continue')
  
  if ans == '3':
       os.system('clear')
       endre=randint(1,int(a))
       sh='iPhone 2G ($'
       amount=str(int(endre))
       sh2=')'
       sh3=str(sh)+str(amount)+str(sh2)
       print(sh3)
       time.sleep(3)
       a= int(a) - int(endre)
       save=open('save.sav','w')
       save.write(str(a))
   
  if ans == 'reset':
    os.system('rm save.sav')
    print('Completed the game will close')
    time.sleep(3)
    exit()
        
  if ans == '5':
       sh='iPhone 2G ($'
       amount=str(randint(1,int(a)))
       sh2=')'
       sh3=str(sh)+str(amount)+str(sh2)
       print(sh3)
       input()
      
    
