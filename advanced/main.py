from operations import add, subtract, multiply, divide
from utils import get_user_number, get_operation

number_1 = get_user_number()
number_2 = get_user_number()
operation = get_operation()

result = 0

if operation == "+":
    result = add(number_1, number_2)

elif operation == "-":
    result = subtract(number_1, number_2)

elif operation == "*":
    result = multiply(number_1, number_2)

elif operation == "/":
    if number_2 == 0:
        print("Cannot divide by zero. Please enter another number.")
        number_2 = get_user_number()

        while number_2 == 0:
            print("Cannot divide by zero. Try again.")
            number_2 = get_user_number()

    result = divide(number_1, number_2)

print("Result:", result)