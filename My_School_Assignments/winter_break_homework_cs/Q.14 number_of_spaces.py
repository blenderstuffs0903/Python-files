# Q14. Write a program using Python to enter a string and count number of spaces in string.
string = input("Enter a string")
# space_count = 0
# for char in string:
#     if char.isspace():
#         space_count += 1


space_count = string.count(" ")
#
if space_count == 0:
    print(f"'{string}' doesn't have any spaces in it.")
else:
    print(f"'{string}' contains {space_count} spaces.")


