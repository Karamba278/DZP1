class Data:

    @classmethod
    def my_method(cls, param):
        return param.split('-')

    @staticmethod
    def data_control(param_1):
        try:
            if param_1[0].isdigit()==False or param_1[1].isdigit()==False or param_1[2].isdigit()==False:
                data_print='Вы ввели дату в неверном формате, необходимо вводить в цифровом виде'
            elif len(param_1)>3:
                data_print='Вы ввели неверный формат даты'
            elif int(param_1[0])>31 or int(param_1[0])<1:
                data_print='Вы ввели неверное число' # можно прописать отдельные условия для количества дней в каждом месяце, это несложно, но сильно увеличит программу, поэтому упустим.
            elif int(param_1[1])<1 or int(param_1[1])>12:
                data_print='Вы ввели неверный месяц'
            else:
                data_print=('\ '.join(param_1))
        except IndexError:
            data_print='Вы ввели неверный формат даты'
        return data_print


data_inp=input('Введите дату в формате dd-mm-yyyy ')
data_list=Data.my_method(data_inp)
print(Data.data_control(data_list))