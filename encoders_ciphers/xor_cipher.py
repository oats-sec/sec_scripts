#!/usr/bin/env python3
# Simple XOR cipher
# Maybe not the most efficient Python implementation, but easy to understand
# U+0A75

def xor_cipher(data, key):
    data = normalize_input(data)
    key = normalize_input(key)

    for i in range(len(data)):
        j = i % len(key) # rotate key bytes (modulo)
        data[i] = data[i] ^ key[j] # xor data with key, byte-wise

    return bytes(data)

def normalize_input(data, encoding="utf-8"):
    if type(data) is str:
        return bytearray(data, encoding)

    return bytearray(data)

# Example
input_str = "Hallo world, such a nice day"
password = "hunter2!#+"
print(input_str)

encrypted = xor_cipher(data=input_str, key=password)
print(encrypted, encrypted.hex())

decrypted = xor_cipher(data=encrypted, key=password)
print(decrypted)
print(decrypted.decode("utf-8"))
