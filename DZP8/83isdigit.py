class MyError(ValueError):
    def __init__(self, param):
        self.param = param

number_list=[]
print('Введите список чисел по одному. Для остановки напишите stop')
text='start'
while text != 'stop':
    text=input('Введите число ')
    if text=='stop':
        break
    try:
        if text.isdigit()==False:
            raise MyError('Вы ввели не число')
        else: number_list.append(int(text))
    except MyError as err:
        print (err)
print('Ваш список чисел: ', number_list)
