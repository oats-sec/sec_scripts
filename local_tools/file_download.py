#!/usr/bin/python
# nc -q 0 -vlnp 4545 < somefile
import socket
import sys
if (len(sys.argv) < 2):
    print("params: <ip> <filename>")
    print("listen port is 4545")
    sys.exit(0)
target = sys.argv[1]
filename = sys.argv[2]
s = socket.socket()
s.connect((target, 4545))
f = open (filename, "ab")
res = s.recv(1024)
while (res):
    f.write(res)
    res = s.recv(1024) 
s.close()
