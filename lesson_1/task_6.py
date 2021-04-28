import locale

origin_str = ['сетевое программирование', 'сокет', 'декоратор']

with open('resurs.txt', 'w+') as f_n:
    for i in origin_str:
        f_n.write(i + '\n')
    f_n.seek(0)

print(f_n)
#name='resurs.txt' mode='w+' encoding='UTF-8'>

file_coding = locale.getpreferredencoding()

with open('resurs.txt', 'r', encoding=file_coding) as f_n:
    for i in f_n:
        print(i)


