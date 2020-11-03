#!/usr/bin/env python3
import os
static_ip = "10.0.0."

for current in range(0, 256):
    target = static_ip + str(current)
    response = os.system("ping -c 3 -n -q " + target + " > /dev/null")

    if(response == 0):
        print("[UP] " + target )
    else:
        print("[DOWN] " + target )
