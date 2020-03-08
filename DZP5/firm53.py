with open ('firm.txt', 'r', encoding='ANSI') as f:
    textread=f.readlines()
#print(textread)
textlist=[]
sumOkl=[]
for i in range(len(textread)):
    textlist.append(textread[i].split())
    x=textlist[i]
    if int(x[1])<20000:
        print (f'У {x[0]}а оклад меньше 20000 рублей и составляет {x[1]}')
    sumOkl.append(int(x[1]))
#print(textlist)
print('Средний оклад по фирме составляет', sum(sumOkl)/len(textread))
