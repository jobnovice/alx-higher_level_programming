#!/usr/bin/pyhton3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [None] * list_length
    for i in range(0, list_length):
        try:
            my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            new_list[i] = my_list_1[i] / my_list_2[i]
    return new_list
