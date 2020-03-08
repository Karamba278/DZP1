import time
import keyboard

class TrafficLight:
    # атрибуты класса
    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        i = 0
        while i!=4:
            if keyboard.is_pressed('Esc'):
                break
            else:
                print(f'\r{TrafficLight.__color[i]}', end='')
                if i==1:
                    time.sleep(1)
                else:
                    time.sleep(2)
                if i==2:
                    i=0
                    TrafficLight.__color.reverse()
                i+=1

a = TrafficLight()
a.running()
print('\rThe End')
