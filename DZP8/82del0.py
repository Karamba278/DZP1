class MyError(ZeroDivisionError):
    def __init__(self, param):
        self.param = param



try:
    a = int(input('Введите любое число '))
    b = int(input('Введите любое число (кроме 0) '))
    try:
        if b == 0:
            raise MyError('На ноль делить нельзя!')
        c = a / b

    except MyError as err:
        print(err)
    else:
        print('a/b =', round(c, 2))
except ValueError:
    print('Вы ввели не число')


