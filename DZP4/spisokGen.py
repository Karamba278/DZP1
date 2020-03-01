from random import randint

spisok1 = [randint(0, 100) for el in range(20)]
print (spisok1)
spisok2=[]
for el in range(0, len(spisok1)-1):
    if spisok1[el + 1] > spisok1[el]:
        spisok2.append(spisok1[el+1])
print(spisok2)
