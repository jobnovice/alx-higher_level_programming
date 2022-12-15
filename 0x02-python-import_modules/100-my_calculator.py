#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    num = len(sys.argv)
    

    if num != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if sys.argv[2] == '+':
            print("{} + {} = {}".format(int(sys.argv[1]), int(sys.argv[3]), (int(sys.argv[1]) + int(sys.argv[3]))))
            exit(0)
        elif sys.argv[2] == '*':
            print("{} + {} = {}".format(int(sys.argv[1]), int(sys.argv[3]), (int(sys.argv[1]) * int(sys.argv[3]))))
            exit(0)
        elif sys.argv[2] == '-':
            print("{}".format(int(sys.argv[1]), int(sys.argv[3]), (int(sys.argv[1]) - int(sys.argv[3]))))
            exit(0)
        elif sys.argv[2] == '/':
            print("{}".format(int(sys.argv[1]), int(sys.argv[3]), (int(sys.argv[1]) / int(sys.argv[3]))))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)  