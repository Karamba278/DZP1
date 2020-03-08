
class Road:

    def mass_count (self, length, width):
        self._length = length
        self._width = width
        m_c= self._length * self._width * 25 * 5
        print (f'Масса асфальтовой дороги длинной {self._length}м и ширино {self._width}м составляет - {round(m_c/1000)} тонн')

l1=int(input('Введите длину дороги в метрах '))
w1=int(input('Введите ширину дороги в метрах '))
a=Road()
a.mass_count(l1, w1)