#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    if i == 1:
        print("0 arguments.")
    elif i == 2:
        print("{:d} argument:".format(i - 1))
        for l in range(1, i):
            print("{}: {}".format(l, sys.argv[l]))
    else:
        print("{:d} arguments".format(i - 1))
        for l in range(1, i):
            print("{}: {}".format(l, sys.argv[l]))
