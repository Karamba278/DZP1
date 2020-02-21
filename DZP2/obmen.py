l = []
count = int(input('Сколько элементов списка Вы хотите ввести? '))
for i in range(count):
    l.append(input((f'Введите элемент №{i+1} ')))
print ('Ваш список - ', l)
i = 0
if (len(l) % 2) == 1:
    k = len(l)-2
if (len(l) % 2) == 0:
    k = len(l)-1
while i < k:
    l[i], l[i+1]= l[i+1], l[i]
    i += 2
print('Список с перевернутыми соседними индексами - ', l)


