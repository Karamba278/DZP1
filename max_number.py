n= int(input('Введите целое положительное число '))
n_hist=n
if n < 10:
    print ('Вы ввели число с единственной цифрой')
else:
    n2 = n % 10

    n = n // 10

    while n > 0:

        if n % 10 > n2:
            n2 = n % 10

        n = n // 10

    print('Максимальная цифра в числе ', n_hist, '- ', n2)


