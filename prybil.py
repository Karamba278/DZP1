n_v=int(input('Введите прибыль предприятия в рублях  '))

n_iz=int(input('Введите издержки предприятия в рублях  '))

if n_v > n_iz:

    print('Поздравляем! Фирма отработала год с прибылью в ', n_v-n_iz, 'руб.')

    rent= (n_v - n_iz) * 100 / n_v

    rent = ('%.2f' % (rent))

    print('Рентабельность составила', rent, '%')

    count=int(input('Сколько сотрудников трудится в вашей фирме?  '))

    rent = (n_v - n_iz) / count

    rent = ("%.2f" % (rent))

    print('Прибыль в расчете на одного сотрудника составила', rent, 'руб.' )

elif n_v < n_iz:

    print('Предприятие закончило этот год с убытком, сочувствуем.')

else:

    print('Фирма отработала этот год "в ноль".')


