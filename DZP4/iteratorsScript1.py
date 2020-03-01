from sys import argv

the_end = argv

from itertools import count

def iter_func():
    el_end= int(the_end[1])
    spisok1=[]
    for el in count(el_end):
        if el > 20: 
            break
        else:
            spisok1.append(el)
            print(el, end=' ')
    print(' ')
    return spisok1
spisok2=iter_func()

if __name__ == '__main__':
    iter_func()