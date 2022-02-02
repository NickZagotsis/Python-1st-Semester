import requests
import json
import string
r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()
lastround=data["round"] #pairnoyme to teleytaio round

num=[]
for cround in range(lastround,lastround-100,-1): # apo to teleftaio mexri -100
    r = requests.get('https://drand.cloudflare.com/public/%d'%(cround), headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    num.append(data["randomness"])
#metatroph apo hex se binary
for i in range(len(num)):
    num[i]="0x"+num[i]
    num[i]=str(bin(int(num[i],base=16)))
    num[i]=num[i][2:]
temp=''.join(num) # ta ennonoume se 1
max1=0
max0=0
t0,t1=0,0
for i in range(len(temp)): #metrhtes gia akolouthies
    if temp[i]=='0':
        t0+=1
    else:
        if t0>max0:
            max0=t0
        t0=0
    if temp[i]=="1":
        t1+=1
    else:
        if t1>max1:
            max1=t1
        t1=0
print("max series of 0:",max0)
print("max series of 1:",max1)
