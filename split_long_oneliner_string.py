#!/bin/env python3
# Split super long string (e.g. payloads) into multiple lines in exploit style
import sys
__author__ = "oats"

if(len(sys.argv) < 2):
    sys.exit(0)

input = sys.argv[1]

if(len(input) < 1):
    sys.exit(0)

index = 0
step = 64
#seed_string = ""
#seed_string = "buf=\"{}\""
seed_string = "Str = Str + \"{}\""

# Note: 
# Str = "powershell.exe -nop -w hidden -e "

while(index + step < len(input)):
    print(seed_string.format(input[index:index + step]))
    index = index + step

if(index < len(input)):
    print(seed_string.format(input[index:len(input)]))
