#!/usr/bin/env python3
import threading
from socket import *

target_ip = "127.0.0.1"
tcp_top20 = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 
            443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
tcp_full = [*range(65535, 0, -1)]
num_threads = 8

ports = tcp_full

def worker():
    while True:
        try:
            port = ports.pop()
            s = socket(AF_INET, SOCK_STREAM)
            conn = s.connect_ex((target_ip, port))
            if(conn == 0) :
                print('Port {p:5d} OPEN'.format(p=port))
            s.close()
        except IndexError:
            break # stop when ports list empty

for _ in range(num_threads):
    threading.Thread(target=worker).start()
