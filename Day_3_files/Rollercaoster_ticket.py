print("Welcome to the rollercoaster!")
height = int(input("Enter your height"))
bill = 0
if height >= 120:
    print("You can ride")
    age = int(input("Enter your age"))
    if age < 12:
        bill = 4
        print("Please pay $4.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    elif 45 <= age <= 55:
        print("You don't have to pay on account of midlife crisis")
    else:
        bill = 12
        print("Please pay $12.")
    wants_photo = input("Do you want a photo, type 'y' or 'n'")
    if wants_photo == "y":
        bill += 3
    print(f"Your finale bill is {bill}")
else:
    print("You cannot ride")
