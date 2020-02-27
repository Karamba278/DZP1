def my_func1(a,b,c):
    min1=min(a,b,c)
    maxS=a+b+c-min1
    print('Сумма двух наибольших чисел (вариант 1) = ', maxS)

def my_func2(a,b,c):
    max1=max(a,b,c)
    if max1==a:
        max2=max(b,c)
    elif max1==b:
        max2=max(a,c)
    else:
        max2=max(a,b)
    print('Сумма двух наибольших чисел (вариант 2) = ', max1+max2)

x1=int(input('Введите первое число '))
x2=int(input('Введите первое число '))
x3=int(input('Введите первое число '))

#вариант 1
my_func1(x1,x2,x3)
# вариант 2
my_func2(x1,x2,x3)
