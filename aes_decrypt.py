#!/usr/bin/env python3
from Crypto.Cipher import AES
import Crypto.Cipher.AES
from binascii import hexlify, unhexlify
import base64

# input from hex
# unhexlify("FF9B1C73D66BCE31AC413EAE131B464F582F6CE2D1E1F3DA7E8D376B26394E5B")

# input from base64
# base64.b64decode("aGVsbG8gd29ybGQxMjMhPyQ=")

encrypted_bytes = unhexlify("FF9B1C73D66BCE31AC413EAE131B464F582F6CE2D1E1F3DA7E8D376B26394E5B")

key = b"\x06\x02\x00\x00\x00\xa4\x00\x00\x52\x53\x41\x31\x00\x04\x00\x00"
init_vector = b"\x01\x00\x01\x00\x67\x24\x4F\x43\x6E\x67\x62\xF2\x5E\xA8\xD7\x04"

decipher = AES.new(key, AES.MODE_CBC, init_vector)
plaintext_bytes = decipher.decrypt(encrypted_bytes)
print(plaintext_bytes)
print(plaintext_bytes.decode("utf-8"))
