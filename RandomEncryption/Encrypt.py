import random
import string


def createDictionary(filename):
    dic = {}
    characters = list(string.ascii_letters)

    arr = characters.copy()

    for ch in characters:
        element = random.choice(arr)
        dic[ch] = element
        arr.remove(element)

    f = open(filename, "w")

    for key in dic:
        f.write(key + ":" + dic[key])
        f.write("\n")

    f.close()
    return dic


def getDictionary(filename):
    dic = {}
    f = open(filename, "r")

    for line in f:
        dic[line[0]] = line[2]

    f.close()
    return dic


def encrypt(text, filename):
    createDictionary(filename)
    dic = getDictionary(filename)

    temp = list(text)

    for i in range(len(text)):
        if temp[i] not in list(string.ascii_letters):
            continue

        temp[i] = dic[text[i]]

    return "".join(temp)


def decrypt(etext, filename):
    dic = getDictionary(filename)
    otherDic = {}

    for key in dic:
        otherDic[dic[key]] = key

    temp = list(etext)

    for i in range(len(etext)):
        if temp[i] not in list(string.ascii_letters):
            continue

        temp[i] = otherDic[etext[i]]

    return "".join(temp)


