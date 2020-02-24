count = int(input('Информацию о скольки товарах Вы хотите ввести? '))
spisok = []
name = []
price = []
number = []
sht = []
for i in range(count):
    n1 = input('Введите название товара ')
    n2 = int(input('Введите цену товара '))
    n3 = int(input('Введите количество товара '))
    n4 = input('Введите единицу измерения товара ')
    spisok.append((i+1, {'название': n1, 'цена': n2, 'количество': n3, 'eд': n4}))
    print(spisok[i])
    name.append(n1)
    price.append(n2)
    number.append(n3)
    sht.append(n4)
analitics = {'название': name, 'цена': price, 'количество': number, 'ед': sht}
print(analitics)
