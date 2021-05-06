import socket
import pickle

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

server.bind( # дать адресс неизменный, забиндить.
    ("127.0.0.1",1234)
)
server.listen(5) #---can accept
print("Server is listening")

users=[]


while True:
    user_socket, adress = server.accept()#--------------------accepts tuple(socket,adress)

    print(f"User {user_socket} connected")

    user_socket.send("You connected".encode("utf-8"))


#-----------------------------------------принимаем мэссагу
    data = user_socket.recv(2048)

    from_client=pickle.loads(data)
    print(from_client["message"])