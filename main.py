from calc import Calculator
import sys

if __name__ == "__main__":
    calc = Calculator()
    arg1 = int(sys.argv[2])
    arg2 = int(sys.argv[3])
    if sys.argv[1] == "add":
        result = calc.add(arg1, arg2)
    elif sys.argv[1] == "sub":
        result = calc.sub(arg1, arg2)
    elif sys.argv[1] == "mul":
        result = calc.mul(arg1, arg2)
    elif sys.argv[1] == "div":
        result = calc.div(arg1, arg2)
    else:
        print("Wrong command passed")
        result = None
    
    print(f"Result: {result}")
