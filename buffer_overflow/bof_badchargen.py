# These are snippets copypaste the one you need
__author__ = "oats"

# python 2+ badchar generator for terminal copypaste
badchars = [ 0x00 ]
badtest = ""
for x in range(1,256):
    if(x not in badchars):
        badtest += "\\x" + '{:02x}'.format(x)


# python3 badchar in-code
badchars = [ 0x00 ]
badstring = b""
for x in range(1,256):
    if(x not in badchars):
        badstring += bytes([x])
print(badstring)


# write generated badchars to file for mona
f = open('badchars.bin', 'wb')
f.write(badstring)
f.close()
sys.exit()
