def get_user_number () -> float:
    """Ask user for a number
    :return: the user's number"""

    while True:
        try:
            number= float(input("Enter a number: "))
            return number
        except ValueError:
            print("Wrong input. Please enter a number.")

def get_operation () -> str:
    """Ask the user for an operation
    :return: the valid operation"""

    while True:
            operation = input("Enter a operation you prefer (+, -, *, /):")
            if operation in ["+", "-", "*", "/"]:
                return operation
            else:
                print("Invalid operation. You must enter a valid option")
