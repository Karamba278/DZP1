from random import randint

class Car:
    speed = 0
    color = 'white'
    name = 'Lada'
    is_police = False # исходя из задания - этот атрибут все же лишний, т.к. есть еще 3 класса авто, для
# которых булевы атрибуты по условию не задаются. Но раз задан, то будет его использовать как есть.
    def go(self):
        print(f'{Car.name}, цвет {Car.color} поехала')
    def stop(self):
        print(f'{Car.name}, цвет {Car.color} остановилась')
    def turn(self):
        carturn=randint(0,2)
        if carturn==0:
            print(f'{Car.name}, цвет {Car.color} повернула направо')
        if carturn == 1:
            print(f'{Car.name}, цвет {Car.color} повернула налево')
    def speed_def(self):
        print(f'{Car.name}, цвет {Car.color} едет со скоростью {Car.speed} км/ч')

class TownCar(Car):
    def cartype(self):
        print('Ваша машина относится к городскому классу')
    def speed_def(self):
        print(f'{Car.name}, цвет {Car.color} едет со скоростью {Car.speed} км/ч')
        print('Максимальная скорость на данном участке дороги составляет 60 км/ч')
        if Car.speed>60:
            print(f'Превышение составило {Car.speed-60} км/ч')
        else:
            print('Вы едете с допустимой скоростью. Так держать!')

class SportCar(Car):
    def cartype(self):
        print('Ваша машина относится к спортивному классу')

class WorkCar(Car):
    def cartype(self):
        print('Ваша машина относится к классу служебных авто')
    def speed_def(self):
        print(f'{Car.name}, цвет {Car.color} едет со скоростью {Car.speed} км/ч')
        print('Максимальная скорость на данном участке дороги составляет 40 км/ч')
        if Car.speed > 40:
            print(f'Превышение составило {Car.speed - 40} км/ч')
        else:
            print('Вы едете с допустимой скоростью. Так держать!')

class PoliceCar(Car):
    def cartype(self):
        print('У Вас полицейская машина')

carclass=int(input('Введите класс вашей машины: 1- городская, 2 - спортивная, 3- рабочая, 4-полицейская '))
if carclass==4:
    Car.is_police=True # смысла нет это указывать, но раз в задании есть, то укажем.
Car.name=input('Введите имя авто ')
Car.color=input('Введите цвет авто ')
Car.speed=int(input('Введите скорость авто км/ч '))
c=Car()
pc=PoliceCar()
sc=SportCar()
tc=TownCar()
wk=WorkCar()
if carclass==1:
    tc.cartype()
    c.go()
    c.stop()
    c.turn()
    tc.speed_def()


if carclass==2:
    sc.cartype()
    c.go()
    c.stop()
    c.turn()
    c.speed_def()

if carclass==3:
    wk.cartype()
    c.go()
    c.stop()
    c.turn()
    wk.speed_def()

if Car.is_police:
    pc.cartype()
    c.go()
    c.stop()
    c.turn()
    c.speed_def()
