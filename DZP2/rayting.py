my_list = [7, 5, 3, 3, 2]
print('Изначальный список', my_list)
i = 0
while i == 0:
    new = int(input('Введите натуральное число '))
    if new in my_list:
        ind = my_list.index(new)
        sort = my_list.count(new)
        my_list.insert((ind+sort), new)
        print('В качестве проверки напишем индекс добавленной переменной -', ind+sort)
    else:
        my_list.append(new)
        my_list = sorted(my_list, reverse=True)
    print(f'Пользователь ввел число - {new}, результат {my_list} ')
    nadoelo = input('Хотите добавить еще одно число? Да/нет ')
    if nadoelo == 'нет':
        break