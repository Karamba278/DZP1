#задание 1

filename=input('Введите имя файла в формате txt')
text=[]
print ('Введите строки, которые Вы хотите записать в файл')
with open (filename, 'w', encoding='utf-8') as f:
    for i in range(0, 100):
        textinp=input('')
        textinp2=textinp+'\n'
        text.append(textinp2)
        if textinp=='':
            break
        else:
            f.write(text[i])

#задание 2
with open (filename, 'r', encoding='utf-8') as f:
    textread=f.readlines()
print(f'В файле {filename} - {len(textread)} строк(а)')
for i in range(len(textread)):
    x=textread[i].split()
    print (f'В строке {i+1} - {len(x)} слова(о)')

print(textread)