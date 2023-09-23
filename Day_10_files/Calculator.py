# Calculator


# addition
def add(n1, n2):
    return n1 + n2


# subtraction
def subtract(n1, n2):
    return n1 - n2


# Multiplication
def multiply(n1, n2):
    return n1 * n2


# division
def divide(n1, n2):
    return n1 / n2


# Dictionary of operations
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    num1 = eval(input("What's the first number?\n"))
    should_continue = True

    while should_continue:
        for operator in operations:
            print(operator)
        operation_symbol = input("Type the operation you want to perform").strip()

        num2 = eval(input("What's the second number?\n"))

        operation = operations[operation_symbol]

        answer = operation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        next_step = input(f"Enter 'y', to continue with previous answer, or enter 'n' to start new calculation or 'e' to exit")

        if next_step == 'y':
            num1 = answer
        elif next_step == "n":
            calculator()
            should_continue = False
        else:
            should_continue = False


calculator()
