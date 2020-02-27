def fio_f1(info):
    print('Данные пользователя: ',', '.join(info))

def fio_f2(x1, x2, x3, x4, x5, x6):
    print(f'Данные пользователя: {x1}, {x2}, {x3}, {x4}, {x5}, {x6}'  )

fio= []
print ('Введите Имя, Фамилию, год рождения, город проживания, электронную почту и телефон (через Enter)')
for i in range(6):
    fio.append(input())

# вариант 1
fio_f1(fio)

# вариант 2, через именованные параметры
fio_f2(x1=fio[0], x2=fio[1], x3=fio[2], x4=fio[3], x5=fio[4], x6=fio[5])
