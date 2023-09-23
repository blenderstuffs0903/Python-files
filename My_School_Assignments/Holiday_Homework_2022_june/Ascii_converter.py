while True:
    print("""Enter 1 to convert character to Ascii code
Enter 2 to convert Ascii code to character""")
    choice = int(input())
    while choice not in (1, 2):
        choice = int(input("Your choice was invalid, enter again\n"))

    if choice == 1:
        char = input("Enter a character\n")
        print("The Ascii code of", char, "is", ord(char))
    elif choice == 2:
        A_code = int(input("Enter a Ascii code\n"))
        print("The Ascii code of", A_code, "is", chr(A_code))

    to_continue = input("Enter 'c' to continue, 'e' to exit\n")
    if to_continue == 'e':
        break
