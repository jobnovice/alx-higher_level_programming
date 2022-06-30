#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    
    for i in x:
        try:    
            print("{:d}".format(my_list[i]),end="")
        except (TypeError):
            continue
        except(IndexError, NameError):
            break  
    print()