# Q18. Write a program to enter list of integers and display the smallest and second smallest number
List = input("Enter a list of numbers separated by ','(comma)\n").replace(" ", "").split(",")
for i in range(len(List)):
    List[i] = int(List[i])
smallest = List[0]
for num in List:
    if smallest > num:
        smallest = num
print(f"The smallest number in the list is {smallest}")
List.pop(List.index(smallest))

second_smallest = List[0]
for num in List:
    if second_smallest > num:
        second_smallest = num
print(f"The second smallest number in the list is {second_smallest}")
