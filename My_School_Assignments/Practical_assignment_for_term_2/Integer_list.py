neg_list = []
pos_list = []
List = []

elements = int(input("Enter number of elements\n"))

for num in range(elements):
    print("Enter a integer", num+1)
    List.append(int(input()))

print(List, "\n\n")

for num in List:
    if num >= 0:
        pos_list.append(num)
    else:
        neg_list.append(num)

print("List of positive integers\n", pos_list, "\n")
print("List of negative integers\n", neg_list)
