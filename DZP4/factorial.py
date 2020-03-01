import math

# вариант , факториал считается после создания генератора
def fibo_gen (n1):
    for el in range(1, n1+1):
        yield el

n=int(input('Введите число, факториал которого вы хотите найти '))
for el in fibo_gen(n):
    print (f'факториал числа {el} = {el}! = {math.factorial(el)}')
print(type(fibo_gen(n)))

# вариант 2, факториал считается внутри функции и записывается сразу в генератор

def fibo_gen2 (n2):
    for el in range(1, n2+1):
        yield math.factorial(el)

for el in fibo_gen2(n):
    print (el)
print(type(fibo_gen2(n)))

