with open ('file56.txt', 'r', encoding='ANSI') as f:
    textread=f.readlines()
print(textread)
textlist=[]
textsum=[]
textname=[]
for i in range(len(textread)):
    textread[i]=textread[i].replace('(л)','')
    textread[i]=textread[i].replace('(пр)','')
    textread[i]=textread[i].replace('(лаб).','')
    textread[i]=textread[i].replace('(лаб)','')
    textread[i] = textread[i].replace('—', '0')
    textread[i] = textread[i].replace(':', '')
    textlist.append(textread[i].split())
    tlprom = textlist[i]
    textnum = []
    for el in range(len(tlprom)):
        try:
            textnum.append(int(tlprom[el]))
        except:
            textname.append(tlprom[el])
    textsum.append(sum(textnum))
my_dict= dict ()
for i in range(len(textsum)):
    my_dict.update({textname[i]: textsum[i]})
#print(textlist)
#print(textsum)
print(my_dict)