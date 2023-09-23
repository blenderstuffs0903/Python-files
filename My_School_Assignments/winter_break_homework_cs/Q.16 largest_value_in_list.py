List = input("Enter a list of numbers separated by ','(comma)\n")
List = List.replace(' ', '').split(",")
for i in range(len(List)):
    List[i] = int(List[i])
s = 0
for num in List:
    if num > s:
        s = num

print(f"{s} is the greatest value in the given list.")
#
print(max(List))

