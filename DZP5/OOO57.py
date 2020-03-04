import json

with open ('file57.txt', 'r', encoding='ANSI') as f:
    textread=f.read()
print(textread)
with open ('file57.txt', 'r', encoding='ANSI') as f:
    textread=f.readlines()
#print(textread)
textlist=[]
firmname=[]
prib=[]
pribaver=[]
for i in range(len(textread)):
    textlist.append(textread[i].split())
    textprom=textlist[i]
    firmname.append(textprom[0])
    x=(int(textprom[2])-int(textprom[3])) # можно для подстраховки написать через try, но т.к. задача этого задания другая, то не будем усложнять программу.
    prib.append(x)
    if x>0:
        pribaver.append(x)

#print(textlist)
averprib=sum(pribaver)
my_dict1= dict ()
for i in range(len(firmname)):
    my_dict1.update({firmname[i]: prib[i]})
my_dict2= {'average profit': averprib}
finallist=[]
finallist.append(my_dict1)
finallist.append(my_dict2)
print(finallist)

with open('OOO57.json', "w") as write_f:
    json.dump(finallist, write_f)