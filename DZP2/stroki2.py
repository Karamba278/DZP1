stroka = input('Введите любые слова ')
print(type(stroka))
new_list = stroka.split()
print(new_list)
print(type(new_list))
for i in range(len(new_list)):
    new_stroka = new_list[i]
    print(new_stroka[:10])

