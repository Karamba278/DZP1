
class Organic:

    def __init__(self, param_1):
        self.param_1 = param_1

    def __add__(self, other):
        print('Суммарное количество клеток - ', end='')
        for el in range(self.param_1 + other.param_1):
            print('* ', end='')
        print('')
        return Organic(self.param_1 + other.param_1)

    def __sub__(self, other):
        print('Разница в клетках 1-ой и 2-ой пробирки составляет - ', end='')
        for el in range(abs(self.param_1 - other.param_1)):
            print('* ', end='')
        print('')
        return Organic(abs(self.param_1 - other.param_1))

    def __mul__(self, other):
        print('Количество клеток в первой пробирке умноженное на количество клеток во второй пробирке составляет - ', end='')
        for el in range(self.param_1 * other.param_1):
            print('* ', end='')
        print('')
        return Organic(self.param_1 * other.param_1)

    def __truediv__(self, other):
        print('Количество клеток в одной пробирке при целочисленном делении на количество клеток в другой составит - ', end='')
        parammax=max(self.param_1, other.param_1)
        parammin=min(self.param_1, other.param_1)
        for el in range(parammax//parammin):
            print('* ', end='')
        print('')
        return Organic(parammax//parammin)

    def __str__(self):
        return str(self.param_1)


a=int(input('Укажите количество клеток в первой пробирке '))
b=int(input('Укажите количество клеток во второй пробирке '))
mc = Organic(a)
mc2= Organic(b)
print('a+b =',mc+mc2)
if a-b!=0:
    print('abs(a-b) =',mc-mc2)
else:
    print('Количество клеток в пробирках одинаковое')
print('a*b =',mc*mc2)
print('max(a,b)//(min(a,b) =',mc/mc2)


