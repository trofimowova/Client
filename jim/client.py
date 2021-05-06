import socket
import pickle

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

client.connect(
    ("127.0.0.1",1234)
)
while True:
    data = client.recv(2048)
    print(data.decode('utf-8'))
    
    msg = {
    "action": "msg",
    "time": "<unix timestamp>",
    "to": "#room_name",
    "from": "account_name",
     "message": "Hello World"
    }
        
    client.send(pickle.dumps(msg))
    


