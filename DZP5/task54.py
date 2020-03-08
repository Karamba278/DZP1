with open ('file54.txt', 'r', encoding='ANSI') as f:
    textread=f.readlines()
print(textread)
textlist=[]
for i in range(len(textread)):
    x = textread[i].replace('One', 'Один')
    x = x.replace('Two','Два')
    x = x.replace('Three', 'Три')
    x = x.replace('Four', 'Четыре')
    textlist.append(x)
    print(x)
print(textlist)

with open ('file541.txt', 'w', encoding='ANSI') as f:
    for i in range(len(textlist)):
        f.write(textlist[i])