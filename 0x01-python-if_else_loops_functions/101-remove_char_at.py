#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        str[n] = ""
        return str
    else:
        return str
