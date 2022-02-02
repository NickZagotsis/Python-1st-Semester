from hashlib import new
from re import L
import string
def toBinary(a):
    l,m=[],[]
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append((bin(i)[2:]))
    return m
with open("two_cities.txt",'r') as f:
    str=f.read()
f.close

list=(toBinary(str))
for i in range(len(list)):
    if len(list[i])<7:#pairnoyme th lista h opoia periexei ta binary twn kathe grammatwn se 'string' kai an einai to megethos tous mikrotero tou 7 tote othoume 0 sthn arxh 
        for j in range(7-len(list[i])):
            list[i]="0"+list[i]

for i in range(len(list)):
    list[i]=list[i][0]+list[i][1]+list[i][5]+list[i][6]
for i in range(len(list)):
    if len(list[i])==3:
        list[i]+"0" # an exei  len 3 vazoyme ena 0 sto telos

newlist=[]
for i in range(0,len(list)-3,4):
    newlist.append(list[i]+list[i+1]+list[i+2]+list[i+3])

for i in range(len(newlist)):
    newlist[i]=int("0b"+newlist[i],base=0) #to metatrepoyme se binary morfh pali gia na ginei metatroph se arithmo

even=0 #zygoi (mod2=0)
d3=0 #mod3=0
d5=0 #mod5=0
d7=0 #mod7=0

for i in range(len(newlist)):
    if newlist[i]%2==0:
        even+=1
    if newlist[i]%3==0:
        d3+=1
    if newlist[i]%5==0:
        d5+=1
    if newlist[i]%7==0:
        d7+=0
if len(newlist)!=0: #peritos elegxos alla who knows
    even=(even*100)/len(newlist)
    d3=(d3*100)/len(newlist)
    d5=(d5*100)/len(newlist)
    d7=(even*100)/len(newlist)
    print("Percentage of Even numbers:",even,"%")
    print("Percentage of numbers divisible by 3:",d3,"%")
    print("Percentage of numbers divisible by 5:",d5,"%")
    print("Percentage of numbers divisible by 7:",d7,"%")
else:
    print("Error no data")
