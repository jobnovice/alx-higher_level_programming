#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        j = 0
        for l in my_list:
            j += 1
        while i < x and i < j:
            print("{}".format(my_list[i]), end="")
            i += 1
        print()
        return i
    except Exception:
        pass
