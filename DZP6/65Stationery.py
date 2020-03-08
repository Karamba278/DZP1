class Stationery:
    title = 1
    def draw(self):
        print(f'Запуск отрисовки №{Stationery.title}  с неизвестным инструментом')

class Pen(Stationery):
    def draw(self, ins):
        print(f'Запуск отрисовки №{Stationery.title} при помощи {ins}')

class Pencil(Stationery):
    def draw(self, ins):
        print(f'Запуск отрисовки №{Stationery.title} при помощи {ins}')

class Handle(Stationery):
    def draw(self, ins):
        print(f'Запуск отрисовки №{Stationery.title} при помощи {ins}')

Stationery.title=input('Какой номер отрисовки вы запускаете? ')
instrument=int(input('Каким инструментом необходимо воспользоваться? 1-ручка, 2-карандаш, 3-маркер '))
s=Stationery()
p1=Pen()
p2=Pencil()
h=Handle()
if instrument==1:
    p1.draw('ручки')
elif instrument==2:
    p2.draw('карандаша')
elif instrument==3:
    h.draw('маркера')
else:
    s.draw()