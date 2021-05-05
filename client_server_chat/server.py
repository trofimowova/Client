from Socket import Socket
import asyncio

class Server(Socket):
    def __init__(self):
        super(Server,self).__init__()
        self.users =[]

    def set_up(self):
        self.socket.bind(("127.0.0.1",8000))
        self.socket.listen(5)
        self.socket.setblocking(False)# socket works always/ unblocking condition
        print("Server is listening")

    async def send_data(self,data):
        for user in self.users:
            await self.main_loop.sock_sendall(user,data)

    async def listen_socket(self,listened_socket=None):
        print("Listening user...")
        if not listened_socket:
            return

        while True:
            data = self.main_loop.sock_recv(listened_socket,2048)
            print(f"User send{data}")
            await self.send_data(data)
            

    async def accept_sockets(self):
        while True:
            user_socket, adress = await self.main_loop.sock_accept(self.socket)#--------------------accepts tuple(socket,adress)
            print(f"User {adress[0]} connected")
            
            self.users.append(user_socket)
            self.main_loop.create_task(self.listen_socket(user_socket))

    async def main(self):
        await self.main_loop.create_task(self.accept_sockets())

    
if __name__ == "__main__":
    server = Server()
    server.set_up()
    server.start_loop()