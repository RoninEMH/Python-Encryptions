import os
import random

def XOR(b1, b2):
    if b1 == b2:
        return '0'
    return '1'


def setKey():
    random.seed(0)
    key = bin(random.randint(1, 25))
    size = 7
    newKey = list(key)
    newKey.pop(0)
    newKey.pop(0)
    while len(newKey) < size:
        newKey.insert(0, '0')
    return "".join(newKey)


def encrypt(text):

    key = setKey()
    print("key = " + key)

    arr = []
    for ch in text:
        bits = bin(ord(ch))
        arr.append(bits[2:])

    res = []
    index = 0

    for ch in arr:
        newCH = []
        for bit in ch:
            if index == len(key):
                index = 0
            newCH.append(XOR(bit, key[index]))
            index += 1
        res.append("".join(newCH))

    newRes = []
    for ch in res:
        newRes.append(chr(int(ch, 2)))

    return "".join(newRes)

o = "abcd"
print(o)
s = encrypt(o)
print(s)
print(encrypt(s))
