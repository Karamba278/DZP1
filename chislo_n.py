n= int(input('Введите любое целое число   '))

if n < 0:
    znak = 1
    n = n - n - n
else:
    znak = 0

i = 0

n_count = n

while n_count > 0:

    n_count = n_count// 10

    i = i + 1

n3 = n*(10**(i+i)) + n*(10**i) + n

n2 = n*10**i + n

n_sum = n + n2 + n3

if znak==0:
    print('nnn + nn + n = ', n3, '+', n2, '+', n, '= ', n_sum )

if znak==1:
    print('nnn + nn + n = ', '(',-n3,')', '+', '(',-n2,')', '+', '(',-n,')', '= ', -n_sum )
