import socket
from threading import Thread

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

client.connect(
    ("127.0.0.1",1234)
)



def listen_server():
    while True:
        data = client.recv(2048)
        print(data.decode('utf-8'))


def send_server():
    listen_thread = Thread(target=listen_server)#---------------------one thread listens
    listen_thread.start()#---------------------------inevitably  start!

    while True:
        client.send(input('...').encode("utf-8"))#--------------------second one sends




if __name__ == "__main__":
    send_server()