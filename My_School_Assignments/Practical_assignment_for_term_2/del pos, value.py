List = [4, 5, 6, 7, 2, 8]
print(List)

pos_rem = int(input("Enter the index of the element\n"))
List.pop(pos_rem)
print(List, end="\n\n")

val_rem = int(input("Enter the value of the element\n"))
List.remove(val_rem)
print(List, end="\n\n")
