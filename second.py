time = int (input ('Введите время в секундах '))

time_hour=time // 3600

time_min=(time - time_hour*3600) // 60

time_sec=time - (time_hour * 3600 + time_min * 60)

if time_hour<10:
    time_hour=(f'0{time_hour}')

if time_min<10:
    time_min=(f'0{time_min}')

if time_sec<10:
    time_sec=(f'0{time_sec}')

print(f'Ваше время составляет  {time_hour}:{time_min}:{time_sec}')

