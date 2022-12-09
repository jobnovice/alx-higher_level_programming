#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(str[i]) >= 97 and ord(str[i]) <= 123:
            str[i] += 32
        print("{}".format(str[i]))
    print("{}".format())