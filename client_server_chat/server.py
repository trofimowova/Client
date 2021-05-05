import socket
import threading

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

users =[]



def listen_user(user):
    print("Listening user...")

    while True:
        data = user.recv(2048)
        print(f"User send{data}")
        
        send_to_all(data)
        

def send_to_all(data):
    for user in users:
       user.send(data)           
       

def start_server():
    while True:
        user_socket, adress = server.accept()#--------------------accepts tuple(socket,adress)
        print(f"User {adress[0]} connected")
        
        users.append(user_socket)

        listen_accepted_user=threading.Thread(
            target=listen_user,
            args=(user_socket,)
            )
        listen_accepted_user.start()

    
if __name__ == "__main__":
    start_server()