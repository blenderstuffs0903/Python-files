p = int(input("Enter the principle rate: "))
r = int(input("Enter the rate: "))
y = int(input("Enter the number of years: "))

A = p * ((1 + (r / 100)) ** y)
com_int = round(A - p, 2)

print("The compound interest is:", com_int)
