from sys import argv

script_name, hours_param, stavka_param, premiya_param = argv

print("Имя скрипта: ", script_name)
try:
    hours_param=float(hours_param)
    print("Выработка в часах: ", hours_param)
except ValueError:
    print('Необходимо ввести числовое значение выработки в часах')
try:
    stavka_param=int(stavka_param)
    print("Ставка за час, руб: ", stavka_param)
except ValueError:
    print('Необходимо ввести числовое значение ставки за час в рублях')
try:
    premiya_param=int(premiya_param)
    print("Премия, руб: ", premiya_param)
except ValueError:
    print('Необходимо ввести числовое значение премии в рублях')
try:
    print("Итого зарплата, руб: ", premiya_param + hours_param*stavka_param)
except:
    print('Необходимо ввести числовые значения')