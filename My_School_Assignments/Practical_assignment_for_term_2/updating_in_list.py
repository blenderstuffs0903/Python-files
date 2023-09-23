# Q.4
Avengers = ["iron man", "captain america", "thor", "hulk", "hawkeye",
            "black widow", "spider man", "vision", "scarlett witch"]
print(Avengers)
print("Below is a list of avengers follow"
      " the instructions below to make changes to it\n")

updating = True

while updating:
    print('''Enter 1 to add a new avenger.
Enter 2 to remove an avenger.
Enter 3 to proceed.''')
    choice = int(input())

    if choice == 1:
        add_ons = int(input("How many avengers are you adding"))
        for num in range(add_ons):
            print("Enter the avenger", num + 1)
            Avengers.append(input())

    elif choice == 2:
        removes = int(input("How many people are you removing from avengers initiative"))
        for num1 in range(removes):
            print("Enter his/her name", num1 + 1)
            Avengers.remove(input())

    elif choice == 3:
        updating = False

    else:
        updating = False

print("Do you want to search for an avenger, enter 'y' for yes or 'n' for no.")
to_search = input().lower()

if to_search[0] == "y":
    search = input("Enter the avenger you are searching for\n").lower()

    if search in Avengers:
        print(search, "is an Avenger with index number", Avengers.index(search))
    else:
        print(search, "is not an avenger.")
