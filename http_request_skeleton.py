#!/usr/bin/env python3
import socket
__author__ = "oats"

target_ip = "10.0.2.70"
target_port = 3000

# handle large responses
def recvall(sock):
    BUFF_SIZE = 4096 # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        if not part: # no more data
            break
        data += part
    return data

payload = ""

req = ""
req += "POST / HTTP/1.0\r\n"
#req += "GET / HTTP/1.0\r\n"
req += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0\r\n"
req += "Content-Type: application/x-www-form-urlencoded\r\n"    # remove for GET
req += "Content-Length: {}\r\n".format(len(payload))            # remove for GET
req += "Connection: close\r\n"
req += "\r\n"
req += payload

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_ip, target_port))
s.send(req.encode())

response = recvall(s).decode()
print(response)
