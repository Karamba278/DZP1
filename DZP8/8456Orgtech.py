class Sklad:
    name = 'Name'
    surname = 'Surname'
    position = 'Position'

    def get_full_name():
        print(f'Товарищ {Sklad.surname} {Sklad.name}, Вам в вашей должности - {Sklad.position} - доступ на склад разрешен')

    def in_case_of_mistake():
        print (f'Плохой из Вас {Sklad.position}, товарищ {Sklad.name} {Sklad.surname}!')

class Orgtech:
    def __init__(self, param_1):
        self.param_1 = sum(param_1)
        self.countdef=param_1
    def income(self):
        print(f'Вы собрались загрузить на склад {self.countdef[len(self.countdef)-1]} единиц(ы)  товара')
    def __str__(self):
        return str(self.param_1)
class Printer(Orgtech):
    def income(inc):
        print(f'Вы собрались загрузить на склад {inc} единиц(ы)  принтеров')
class Scaner(Orgtech):
    def income(inc):
        print(f'Вы собрались загрузить на склад {inc} единиц(ы)  сканеров')
class Xerox(Orgtech):
    def income(inc):
        print(f'Вы собрались загрузить на склад {inc} единиц(ы)  ксероксов')
class MyError(ValueError):
    def __init__(self, param):
        self.param = param

Sklad.name=input('Введите имя работника ')
Sklad.surname=input('Введите фамилию работника ')
Sklad.position=input('Введите должность работника ')
Sklad.get_full_name()
sumtech=[]
count=0
sumprint=0
sumscan=0
sumxer=0
i='asd'
while i!='да' or i!='нет':
    i=input('Хотите завести товар? (да/нет) ')
    if i=='да' or i=='нет':
        break
    try:
        if i!='да' or i!='нет':
            raise MyError('Нужно ввести ДА или НЕТ')  # аналогичные проверки можно ввести и в дальнейшем на верность ввода количества товаров
 # но т.к. они будут типовыми, а так же с учетом ограниченного времени и увеличения объема программы - давайте их упустим.
    except MyError as err:
        print (err)

while i=='да':
    sumtech.append(int(input('Введите количество товаров, которые Вы хотите завести ')))
    mc = Orgtech(sumtech)
    mc.income()
    printamount=int(input(f'Сколько из {sumtech[count]} товаров принтеров? ')) # как и условились выше - проверку на верность ввода не будем производить, она типовая.
    mc = Printer
    mc.income(printamount)
    sumprint=sumprint+printamount
#   for el in range(printamount): #заготовка для ввода наименований принтеров в словарь
    scanamount=int(input(f'Сколько из {sumtech[count]} товаров сканеров? '))
    mc = Scaner
    mc.income(scanamount)
    sumscan=sumscan+scanamount
    xeramount=int(input(f'Сколько из {sumtech[count]} товаров сканеров? '))
    mc = Xerox
    mc.income(xeramount)
    sumxer=sumxer+xeramount
    while i != 'да' or i != 'нет':
        i = input('Хотите завести еще товар? (да/нет) ')
        if i == 'да' or i == 'нет':
            break
        try:
            if i != 'да' or i != 'нет':
                raise MyError('Нужно ввести ДА или НЕТ')
        except MyError as err:
            print(err)
    count +=1
mc = Orgtech(sumtech)

print(f'общее количество товаров на складе - {mc} штук(и)')
if (sumprint+sumscan+sumxer)!= int(mc.param_1):
    Sklad.in_case_of_mistake()
    print(f'Инвентаризация показала, что на складе {sumprint+sumscan+sumxer} единиц товара. Ищите ошибку!')
print(f'из них принтеров: {sumprint}')
print(f'из них сканеров: {sumscan}')
print(f'из них ксероксов: {sumxer}')

# можно более широко раскрыть фукнционал, например добавив словари под каждый тип товаров (там указывать можно марки принтеров, сканеров и ксероксов, например)
# а так же можно продумать поиск ошибок по суммарному количеству.
# но сильно время ограничено, я извиняюсь, но просто не успел все это прописать.




