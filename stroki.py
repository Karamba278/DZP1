text = 'Eto stroka'
number_int = 12
number_float = 12.123
print(text, '- ', type(text))
print('Это целое число ', number_int, '- ', type(number_int))
print('Это дробное число ', number_float, '- ', type(number_float))
x = int(input('Введите любое число  '))
if x < 100:
    print('Ваше число меньше 100')
elif x > 100:
    print('Ваше число больше 100')
else:
    print('Ваше число =', x)

