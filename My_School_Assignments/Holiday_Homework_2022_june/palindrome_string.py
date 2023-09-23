Str = input("Enter a string\n")
rev_str = Str[::-1]

if Str == rev_str:
    print(Str, "is palindrome")
else:
    print(Str, "is not palindrome")
