#!/usr/bin/env python3
# this script is for checking which remote ports can be reached for a reverse shell if there is a restrictive firewall
# listen with netcat on the port to check
import socket
import sys
if len(sys.argv) < 3:
    print("missing args: <ip> <port>")
    sys.exit(1)
target_ip = sys.argv[1]
target_port = sys.argv[2]
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3.0)
    s.connect((target_ip, int(target_port)))
    s.send(b"hello\n")
    s.close()
except:
    print("Failed")
