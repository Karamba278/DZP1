from functools import reduce

def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el

#вариант записи №1
spisok1 = [el for el in range(100, 1001) if el % 2 == 0]
print(spisok1)
#вариант записи №2
spisok2 = [el for el in range(100, 1001, 2)]
print(spisok2)

print('Произведение всех элементов списка 1: ', reduce(my_func, spisok1))
print('Произведение всех элементов списка 2: ', reduce(my_func, spisok2))