from random import randint

spisok1 = [randint(0, 20) for el in range(30)]
print(spisok1)
spisok2=[]
for el in range(0, len(spisok1)-1):
    if spisok1.count(spisok1[el])==1:
        spisok2.append(spisok1[el])
print(spisok2)

#для проверки
print ('Для удобной проверки:')
print('Сортированный список 1: ', sorted(spisok1))
print('Сортированный список 2: ', sorted(spisok2))