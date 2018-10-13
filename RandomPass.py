#Python 3
import sys
import random

newPass = ""

def num():
    n = "0123456789"
    global newPass
    newPass += n[random.randint(0, len(n) - 1)]
    return

def lower():
    lA = "abcdefghijklmnopqrstuvwxyz"
    global newPass
    newPass += lA[random.randint(0, len(lA) - 1)]
    return

def upper():
    uA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    global newPass
    newPass += uA[random.randint(0, len(uA) - 1)]
    return

def sym():
    s = "!@#$%^&*()-_+="
    global newPass
    newPass += s[random.randint(0, len(s) - 1)]
    return

def passwd():
    for i in range(0, 1):
        list = [num, lower, upper, sym]
        random.shuffle(list)
        for x in range(0, len(list)):
            r = list[x]
            r()
    return

for n in range(0, int(input("Input a number: "))):
    passwd()
print(newPass)

# crunch 8 8 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 | aircrack-ng -w - -b 70:18:8B:DE:5A:AB h-18.cap
