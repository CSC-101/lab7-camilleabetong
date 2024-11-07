import sys
from convert import str_to_float

if __name__ == "__main__":
    total = 0.0
    for arg in sys.argv[1:]:
        number = str_to_float(arg)
        if number is not None:
            total += number
    print("Sum:", total)
