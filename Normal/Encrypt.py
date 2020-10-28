import random

def setKey():
    random.seed(0)
    return random.randint(1, 25)


def encrypt(text):
    key = setKey()
    print(key)
    encryptText = list(text)
    for i in range(len(text)):
        if ord(text[i]) + key > ord('z'):
            r = ord(text[i]) + key - ord('z')
            encryptText[i] = chr(ord('a') + r - 1)
        else:
            encryptText[i] = chr(ord(text[i]) + key)

    return "".join(encryptText)

def decrypt(encryptText):
    key = setKey()
    print(key)
    text = list(encryptText)
    for i in range(len(encryptText)):
        if ord(text[i]) - key < ord('a'):
            r = ord(text[i]) - key - ord('a')
            text[i] = chr(ord('z') + r + 1)
        else:
            text[i] = chr(ord(encryptText[i]) - key)

    return "".join(text)

print("abcdxyz")
e = encrypt("abcdxyz")
print(e)
print(decrypt(e))
