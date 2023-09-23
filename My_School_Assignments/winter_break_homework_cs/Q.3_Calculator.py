def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Dictionary of operators
operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = eval((input("What's the first number\n")).strip())
    should_continue = True

    while should_continue:
        for operator in operators:
            print(operator)

        operator_symbol = input("Select the operation symbol\n").strip()
        num2 = eval((input("What's the next number")).strip())

        operation_function = operators[operator_symbol]

        answer = operation_function(num1, num2)

        print(f"{num1} {operator_symbol} {num2} = {answer}")
        print("Enter 'y' to continue with the previous answer, or press 'n' for new start or enter 'e' to exit")
        invalid_input = False
        while not invalid_input:
            next_step = input().strip().lower()
            if next_step == 'y':
                invalid_input = True
                num1 = answer
            elif next_step == 'n':
                invalid_input = True
                should_continue = False
                calculator()
            elif next_step == 'e':
                invalid_input = True
                should_continue = False
            else:
                print("Your input was invalid, please type again")


calculator()
