def dollar_rupee_converter():
    print("""Enter '1' to convert dollar to rupee.
Enter '2' to convert rupee to dollar.""")
    choice = int(input())
    amt = int(input('Enter the amount\n'))
    exc = int(input('Enter the current dollar-rupee exchange\n'))
    if choice == 1:
        print(f'{amt} dollars = {amt*exc} rupees')
    elif choice == 2:
        print(f'{amt} rupees = {round(amt/exc, 2)} dollars')

dollar_rupee_converter()
