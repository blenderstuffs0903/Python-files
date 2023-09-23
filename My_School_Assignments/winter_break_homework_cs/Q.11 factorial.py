number = int(input("Enter the number"))
multiplicand = 1
factorial = 1
while multiplicand <= number:
    factorial *= multiplicand
    multiplicand += 1
print(factorial)
