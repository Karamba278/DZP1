
def my_func(x, y):
    y=abs(y)
    x_izn=x
    for i in range(y):
        if i==0:
            x=x
        else:
            x=x*x_izn

    x = 1 / x
    return x

number1=int(input('Введите целое положительное число '))
number2=int(input('Введите целое отрицательное число '))
result= lambda number1, number2: number1**number2
print (f'{number1} в степени {number2} в варианте использования ** =', (lambda n1, n2: pow(n1, n2))(number1, number2) )
print (f'{number1} в степени {number2} в варианте использования цикла = {my_func(number1, number2)}')