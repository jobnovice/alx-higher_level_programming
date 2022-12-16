#!/usr/bin/python3
def no_c(my_string):
    for i in range(0, len(my_string)):
        if chr(i) == 'c' or chr(i) == 'C':
            my_string[i] = ""
    return my_string
