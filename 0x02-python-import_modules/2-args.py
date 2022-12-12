#!/usr/bin/python3
if __import__ == "__main__":
    i = len(argv)
    if i == 0:
        print("0 arguments.")
    else:
        print("{:d} arguments:".format(i))
        for l in range(0, i):
            print("{}: {}".format((l + 1), argv[l]))