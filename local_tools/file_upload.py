#!/usr/bin/python
# on your own machine start `nc -vlnp 4545 > outfile.txt`
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
f = open (filename, "rb")
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
s.close()
