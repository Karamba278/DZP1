class Worker:
    name = 'Name'
    surname = 'Surname'
    position = 'Position'
    _income = {'wage': 0, 'bonus': 0}

class Position(Worker):
    def get_full_name(self):
        print(f'Товарищ {Worker.surname} {Worker.name} работает в должности {Worker.position}')
    def get_total_income(self, inc):
        Worker._income=inc
        print (f'Доход {Worker.surname}а {Worker.name}а (оклад+премия) составляет {sum(Worker._income.values())} рублей')

Worker.name=input('Введите имя работника ')
Worker.surname=input('Введите фамилию работника ')
Worker.position=input('Введите должность работника ')
a=Position()
a.get_full_name()
wage=int(input('Введите оклад сотрудника '))
bonus=int(input('Введите премию сотрудника '))
wb={'wage': wage, 'bonus': bonus}
a.get_total_income(wb)