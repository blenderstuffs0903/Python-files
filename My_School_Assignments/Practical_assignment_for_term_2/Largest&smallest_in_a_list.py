# Q.2
List = [1, 4, 5, 8, 33, 78, 34, 25]
largest_num = smallest_num = List[0]
print(largest_num, smallest_num)

for num in List:
    if num > largest_num:
        largest_num = num
    else:
        smallest_num = num

print("The largest number within the list is", largest_num)
print("The smallest number within the list is", smallest_num)
