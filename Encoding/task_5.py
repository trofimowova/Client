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


