km1 = int(input('Сколько километров пробежал спортсмен в первый день?  '))

km2 = int(input('К какому результату (в километрах) он должен стремиться  '))

i = 1

if km2 <= km1:
    print('Спортсмен достиг поставленного результата в первый день')
else:
    while km1 < km2:

        km1 = km1 * 1.1

        i = i + 1

print('Спортсмен достигнет нужного результата в ' , km2,  'км за ', i,  'дня(ей)')
