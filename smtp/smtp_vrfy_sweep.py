#!/usr/bin/env python3
import socket
from threading import Thread
__author__ = "oats"

#testuser = "root"
testuser = "test"
ip_static = "10.0.0."
start = 1
end = 254
timeout = 20.0
hosts_enabled = []

def check_vrfy(host):
    target = ip_static + str(host)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        connect = s.connect((target, 25))

        # receive banner
        banner = s.recv(1024)

        # send VRFY
        message = 'VRFY ' + testuser + '\r\n'
        s.send(message.encode())

        # receive response
        result = s.recv(1024)
        print('[?] {}: {}'.format(target, result))

        result_decoded = result.decode()
        if(result_decoded.startswith("25") or result_decoded.startswith("55")):
            print('[+] {}: host has VRFY enabled'.format(target))
            hosts_enabled.append(target)

        s.close()
    except socket.timeout:
        print('[-] {}: connection timed out'.format(target))
    except:
        print('[-] {}: connection failed or refused'.format(target))

threads = []
for current in range(start, (end + 1)):
    t = Thread(target=check_vrfy, args=(current,))
    threads.append(t)
    t.start()

for thread in threads:
    thread.join()

print ("[*] Hosts with VRFY enabled:")
for result in sorted(hosts_enabled):
    print(result)

print("[*] done")
