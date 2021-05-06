import socket
import time
import pickle 


server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

server.bind( # дать адресс неизменный, забиндить.
    ("127.0.0.1",1234)
)
#---------------------------------------------------------------------#
server.listen(5) #---can accept
print("Server is listening")

while True:
    user_socket, adress = server.accept()#--------------------accepts tuple(socket,adress)

    print(f"User {user_socket} connected")

    data = user_socket.recv(1024)
    print(pickle.loads(data))
    response = {
    "response": 200,
    "alert":"Необязательное сообщение/уведомление"
    }
    user_socket.send(pickle.dumps(response))
    user_socket.close()

    
    print(pickle.loads(data))
