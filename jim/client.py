import socket
import pickle

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

client.connect(
    ("127.0.0.1",1234)
)
def start_up():   
    data = client.recv(2048)
    print(data.decode('utf-8'))
    send_data()


def send_data():
    while True:
        msg = {
        "action": "msg",
        "time": "<unix timestamp>",
        "to": "#room_name",
        "from": "account_name",
        "message": "Hello World"
        }
            
        client.send(pickle.dumps(msg))
        

if __name__=="__main__":
    start_up()

