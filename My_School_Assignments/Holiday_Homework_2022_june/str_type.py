char = input("Enter a character\n")

if char.isalpha():
    print(char, "is an alphabet.")
elif char.isdigit():
    print(char, "is a number.")
else:
    print(char, "is a special character")
