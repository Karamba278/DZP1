class ComplexNumber:

    def __init__(self, param_1):
        self.param_1 = param_1

    def __add__(self, other):
        return ComplexNumber(self.param_1 + other.param_1)

    def __mul__(self, other):
        return ComplexNumber(self.param_1 * other.param_1)

    def __str__(self):
        return str(self.param_1)


a = complex(1, 2)
b = complex(4, 6)
mc = ComplexNumber(a)
mc2 = ComplexNumber(b)
print('a+b =',mc+mc2)
print('a*b =',mc*mc2)