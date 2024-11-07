from convert import str_to_float
from typing import List

def gather_numbers() -> List[float]:
    numbers1 = []
    while True:
        user_input = input("Enter a number & type 'done' when finished: ")
        if user_input.lower() == "done":
            break
        number = str_to_float(user_input)
        if number is not None:
            numbers1.append(number)
    return numbers1

if __name__ == "__main__":
    numbers = gather_numbers()
    print("Sum:", sum(numbers))

