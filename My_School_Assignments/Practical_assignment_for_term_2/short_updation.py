import os

List = [23, 43, 67, 23, 89, 32]

looping = True
print("_"*10)
while looping:
    print('''Enter '1' to add a new element
Enter '2' to delete an element
Enter '3' to search for an element
Enter '4' to exit.\n''')

    choice = int(input("->"))
    os.system("cls")
    if choice == 1:
        List.append(int(input("Enter the new element\n")))
        print(List)

    elif choice == 2:
        print(List)
        remove = int(input("Enter the element to bo removed"))
        if remove in List:
            List.remove(remove)
        else:
            print(remove, "is not in the list")
        print(List, end="\n\n")

    elif choice == 3:
        search = int(input("Enter the element you are searching for"))
        if search in List:
            print("Index number of", search, "is", List.index(search))
        else:
            print(search, "is not in the list.")

    else:
        print("program terminated")
        looping = False
