import pickle
import socket
import time

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

client.connect(
    ("127.0.0.1",1234)
)



while True:
    msg ={
        "action": "authenticate",
        "time": "<unix timestamp>",
        "user":{
                "account_name":  "C0deMaver1ck",
                "password":      "CorrectHorseBatteryStaple"
        }
        }
    
    client.send(pickle.dumps(msg))

    data = client.recv(1024)
    print(pickle.loads(data))
    
    #client.close()

    
