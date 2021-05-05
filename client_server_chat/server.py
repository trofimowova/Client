from Socket import Socket
import threading

class Server(Socket):
    def __init__(self):
        super(Server,self).__init__()
        #self.listen(5) #---can accept
        print("Server is listening")
        self.users =[]

    def set_up(self):
        self.bind(("127.0.0.1",8000))
        self.listen(5)
        self.accept_sockets()

    def send_data(self,data):
        for user in self.users:
            user.send(data) 

    def listen_socket(self,listened_socket=None):
        print("Listening user...")

        while True:
            data = listened_socket.recv(2048)
            print(f"User send{data}")
            self.send_data(data)
            

    def accept_sockets(self):
        while True:
            user_socket, adress = self.accept()#--------------------accepts tuple(socket,adress)
            print(f"User {adress[0]} connected")
            
            self.users.append(user_socket)

            listen_accepted_user=threading.Thread(
                target=self.listen_socket,
                args=(user_socket,)
                )
            listen_accepted_user.start()
        

    
if __name__ == "__main__":
    server = Server()
    server.set_up()