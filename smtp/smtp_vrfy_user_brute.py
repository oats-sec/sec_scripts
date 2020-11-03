#!/usr/bin/env python3
import socket
import sys
import time
__author__ = "oats"

if len(sys.argv) != 4:
    print("Usage: vrfy_user_brute.py <host> <wordlist> <skip>")
    print("Skipping lines in the wordlist allows you to do the VRFY bruteforce in several attempts")
    sys.exit(0)

target = sys.argv[1]
wordlist = sys.argv[2] # '/usr/share/seclists/Usernames/top-usernames-shortlist.txt'
skip = int(sys.argv[3])

email_ext = "" # e.g. @brainfuck

port = 25
timeout = 20.0
users = []

try:
    print("[*] Testing target: {}".format(target))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    connect = s.connect((target, port))
    # receive banner
    banner = s.recv(1024)
    counter = 0

    print('skipping lines: ' + str(skip))

    with open(wordlist, "r") as user_file:
        for line in user_file:
            username = line.rstrip()

            counter = counter + 1

            if(counter < skip):
                continue            

            # send VRFY
            message = 'VRFY ' + username + email_ext + '\r\n'
            s.send(message.encode())

            # receive response
            result = s.recv(1024)
            print('[?] {}: {}'.format(username, result))

            result_decoded = result.decode()
            if(result_decoded.startswith("25")):
                print('[+] ' + str(counter) + ' {}: user exists'.format(username))
                users.append(username)
            else:
                print('[-] ' + str(counter) + ' {}: user does not exists'.format(username))

            time.sleep(2)
            
    s.close()
except socket.timeout:
    print('[-] {}: connection timed out'.format(target))
except:
    print('[-] {}: connection failed or refused'.format(target))

print("[!] Users:")
for user in users:
    print(user)

print("[*] done")

