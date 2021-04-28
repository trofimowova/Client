develop = 'разработка'
socket = 'сокет'
dec = 'декоратор'

print(develop,socket,dec)
print(type(develop))
print(type(socket))
print(type(dec))


unic = [b'\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
b'\u0441\u043e\u043a\u0435\u0442',
b'\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

for deus in unic:
    print(type(deus))

#___________________________________________________________

klass = b'class'
function = b'function'
method = b'method'

print(klass,function,method)
print(type(klass),len(klass))
print(type(function),len(function))
print(type(method),len(method))



a = b'attribute'
#b = b'класс' - ---bytes can only contain ASCII literal characters
#c = b'функция'-----bytes can only contain ASCII literal characters
d = b'type'

print(type(a))
print(type(b))
print(type(c))
print(type(d))


dev='разработка'
admin = 'администрирование'
prot = 'protocol'
std = 'standard'

print(type(dev))
dev_b = dev.encode('utf-8')
print(dev_b)
print(type(dev_b))
dev = dev_b.decode('utf-8')
print(type(dev))
#маленькая проверка для себя

admin_b = admin.encode('utf-8')
admin = admin_b.decode('utf-8')


prot_b = prot.encode('utf-8')
prot = prot_b.decode('utf-8')


std_b = std.encode('utf-8')
std = std_b.decode('utf-8')

#___________________________________________________________
import subprocess

ping_ls = [['ping', 'yandex.ru'],['ping', 'youtube.com']]

for ping_res in ping_ls:
 
    ping_process = subprocess.Popen(ping_res, stdout=subprocess.PIPE)

    
    i=0

    for line in ping_process.stdout:
 
        if i<5:
            print(line)
            line = line.decode('cp866').encode('utf-8')
            print(line.decode('utf-8'))
            i += 1
        else:
            print('-'*30)
            break

#___________________________________________________________

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



