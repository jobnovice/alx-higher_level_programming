#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv)) == 1:
        print("0 arguments")
    elif (len(sys.argv) == 2):
        print("{} argumnet\n1: {}".format(len(sys.argv) - 1, str(sys.argv[1])))
    else:
        for i in range (len(sys.argv)):
            print("{} argumnets\n{}: {}".format(len(sys.argv),i + 1, str(sys.argv[i])))
