#!/usr/bin/python3
for i in range(122, 98, -1):
    print("{:c}".format(chr(i - 32) if i % 2 else i), end="")