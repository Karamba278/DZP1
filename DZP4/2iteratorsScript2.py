from sys import argv

number = argv

from itertools import cycle

import iteratorsScript1
c=0
number1=int(number[2]) #при выполнении этого скрипта нужно задавать два параметра: 1. - число, с которого начинать
# генерацию чисел (участвует в скрипте iteratorsScript1) 2. - Число повторений cycle
for el2 in cycle(iteratorsScript1.spisok2):
    if c>number1:
        break
    iteratorsScript1.iter_func()
    print('и еще раз ')
    c += 1
