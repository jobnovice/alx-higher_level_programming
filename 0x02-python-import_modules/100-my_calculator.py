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
            if (str(sys.argv[2]) == "+"):
                print(f"{argv[1]} + {argv[3]} = {add(int(sys.argv[1]), int(sys.argv[2]))}")
            elif (str(sys.argv[2]) == "-"):
                print(f"{argv[1]} + {argv[3]} = {sub(int(sys.argv[1]), int(sys.argv[2]))}")
            elif (str(sys.argv[2]) == "*"):
                print(f"{argv[1]} + {argv[3]} = {mul(int(sys.argv[1]), int(sys.argv[2]))}")
            else:
                print(f"{argv[1]} + {argv[3]} = {div(int(sys.argv[1]), int(sys.argv[2]))}")