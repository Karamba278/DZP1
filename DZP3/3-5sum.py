
def sumEl (counts):
    counts=counts.split()
    counts_list=[]
    for i in counts:
        i=int(i)
        counts_list.append(i)
    return sum(counts_list)
i=0
x_list_str=[]
sum_vseh=0
while i!=1:
    x_str=input('Введите числа в строку через пробел  ')
    if x_str=='Стоп':
        break
    else:
        sum_vseh= sum_vseh+sumEl(x_str)
        print ('Сумма всех введенных чисел = ', sum_vseh)



