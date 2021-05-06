from Socket import Socket
import asyncio

class Client(Socket):
    def __init__(self):
        super(Client,self).__init__()
    def set_up(self):
        self.socket.connect(("127.0.0.1",8000))
        self.socket.setblocking(False)


    async def listen_socket(self,listened_socket=None):
        while True:
            data =  await self.main_loop.sock_recv(self.socket,2048)
            print(data.decode("utf-8"))
        
    async def send_data(self,data=None):
        while True:
            data=self.main_loop.run_in_executor(None, input, "...")
            await self.main_loop.sock_sendall(self.socket, data.encode("utf-8"))

    async def main(self):
       await asyncio.gather(
            self.main_loop.create_task(self.listen_socket()),
            self.main_loop.create_task(self.send_data())
           )



if __name__ == "__main__":
    client = Client()
    client.set_up()
    client.start_loop()
