Dict = {}

# Asking the user that how many friend's number he wanna enter
num = int(input("How many friend's number you wanna enter?\n"))

for num in range(num):
    print("Enter the name of friend", num + 1)
    name = input().lower()
    print("Enter", name + "'s number")
    Dict[name] = input()
    print()

# Displaying the number of all friends
for friend in Dict:
    print(friend, Dict[friend])
print()

# Ask the user if he wants any modification in the data
print("Do you want to perform any modification in contacts?")
to_modify = input("Enter 'y' for yes or 'n' for no\n").lower()
print()
if to_modify == 'y':
    to_modify = True
else:
    to_modify = False

# Looping modification process
while to_modify:
    print("Which type of modification do you want to perform?")
    print('''Enter '1' to add a new friend's number.
Enter '2' to remove a friend.
Enter '3' to edit a friend's number.
Enter '4' to search a friend's number.''')
    modification = int(input("\n"))

    # Add a friend's name
    if modification == 1:
        print("Enter the name of new friend")
        name = input().lower()
        Dict[name] = input("Enter your friends number\n")
        print()

        # Displaying the number of all friends
        for friend in Dict:
            print(friend, Dict[friend])

    # Removing a student's data
    elif modification == 2:
        removed_frnd = input("Who's number you wanna remove?\n").lower()
        if removed_frnd in Dict:
            Dict.pop(removed_frnd)
        else:
            print("No record", removed_frnd)

        # Displaying the number of all friends
        for friend in Dict:
            print(friend, Dict[friend])

    elif modification == 3:
        frnd = input("Who's number you want to modify?\n").lower()
        if frnd in Dict:
            Dict[frnd] = input("Enter new number\n")
        else:
            print("No record of", frnd)
        print()

    elif modification == 4:
        search = input("Who's number you wanna see\n")
        if search in Dict:
            print(search + "'s number is", Dict[search], "\n")
        else:
            print("No record of", search)

    # Asking the user if he wants further modifications
    print("Do you want to perform any further modification?")
    to_modify = input("Enter 'y' for yes or 'n' for no\n").lower()
    # Terminating the loop if no modifications are needed
    if to_modify == 'n':
        to_modify = False

