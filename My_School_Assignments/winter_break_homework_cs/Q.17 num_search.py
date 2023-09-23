# Q17. Write a program to enter list of integers and search a number in it.
List = input("Enter a list of numbers separated by ','(comma)\n").replace(" ", "").split(",")
for i in range(len(List)):
    List[i] = int(List[i])
