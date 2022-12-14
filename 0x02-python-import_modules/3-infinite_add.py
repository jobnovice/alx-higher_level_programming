#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    res = 0
    if num == 1:
        print("0")
    elif num == 2:
        print("{}".format(int(sys.argv[1])))
    else:
        for i in range(1, num + 1):
            res += int(sys.argv[i])
        print("{}".format(res))