x1 = [123, '123', (123, '123'), frozenset('123'), dict ( k1 = '1234', k2 = 15), bool(35), b'text',
        type(None), ]
print('Список -', x1)
print('Тип x1 - ', type(x1))
for i in range(len(x1)):
    print (f'Тип элемента {i+1}  в списке x1 - ', type(x1[i]))

