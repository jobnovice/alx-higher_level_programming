#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            str[i] += 32
        print("{}".format(i))
    print("{}".format())