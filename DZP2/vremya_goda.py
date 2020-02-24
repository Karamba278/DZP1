# решение через лист
vremya_goda = [(12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
print(type(vremya_goda))
mes = int(input('Введите номер месяца '))
for i in range(len(vremya_goda)):
    if vremya_goda[i].count(mes) == 1:
        break
if i == 0:
    print('Сейчас зима')
if i == 1:
    print('Сейчас весна')
if i == 2:
    print('Сейчас лето')
if i == 3:
    print('Сейчас осень')

# решение через словарь

vremya_goda = { 'зима': (12, 1, 2), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}
print(type(vremya_goda))
mes = int(input('Введите номер месяца '))
if mes in vremya_goda['зима']:
    print('Сейчас зима')
if mes in vremya_goda['весна']:
    print('Сейчас весна')
if mes in vremya_goda['лето']:
    print('Сейчас лето')
if mes in vremya_goda['осень']:
    print('Сейчас осень')


