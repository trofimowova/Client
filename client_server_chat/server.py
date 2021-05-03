import socket

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

server.bind( # дать адресс неизменный, забиндить.
    ("127.0.0.1",1234)
)
#---------------------------------------------------------------------#
server.listen(5)

while True:
    user_socket, adress = server.accept()

    user_socket.send("You connected".encode("utf-8"))
