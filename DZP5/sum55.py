
textwrite=(input('Введителюбые числа через пробел  '))
 # т.к. в задании сказано что числа разделены пробелами, то  можно сделать вывод,
# что они записаны в одной строке.
with open ('file55.txt', 'w', encoding='ANSI') as f:
    f.write(textwrite)

with open ('file55.txt', 'r', encoding='ANSI') as f:
    textread=f.readlines()
textlist=textread[0].split()
#print(textread)
#print(textlist)
for i in range(len(textlist)):
    textlist[i]=int(textlist[i])
sumtext=sum(textlist)
print('Сумма чисел в файле = ', sumtext)