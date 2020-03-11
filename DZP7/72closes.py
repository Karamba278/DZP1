class MyClass:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1/6.5+0.5
        self.param_2 = param_2*2+0.3

    @property
    def my_method(self):
        return self.param_1+self.param_2

coat_v=56
suit_h=1.9
mc = MyClass(coat_v, suit_h)

print(f'Расход ткани на пальто составляет - {round(mc.param_1,2)}м')
print(f'Расход ткани на костюм составляет - {round(mc.param_2,2)}м')
print(f'Суммарный расходткани = {round(mc.my_method,2)}')