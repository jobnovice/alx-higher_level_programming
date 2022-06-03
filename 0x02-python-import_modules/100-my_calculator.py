#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if str(sys.argv[2]) != "+" or  "-" or "*" or "/":
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            x=int(sys.argv[1])
            y=int(sys.argv[2])
            if (str(sys.argv[2]) == "+"):
                print(f"{sys.argv[1]} + {sys.argv[3]} = {add(x, y)}")
            elif (str(sys.argv[2]) == "-"):
                print(f"{sys.argv[1]} + {sys.argv[3]} = {sub(x, y)}")
            elif (str(sys.argv[2]) == "*"):
                print(f"{sys.argv[1]} + {sys.argv[3]} = {mul(x, y)}")
            else:
                print(f"{sys.argv[1]} + {sys.argv[3]} = {div(x, y)}")