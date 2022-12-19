#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        j = 1
        for i in my_list:
            j += 1
        while i < x and i < j:
            print("{:d}".format(my_list[i]), end="")
            i += 1
    except Exception:
        pass
