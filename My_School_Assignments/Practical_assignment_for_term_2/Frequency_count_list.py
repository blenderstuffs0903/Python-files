# Q.5
List = [1, 2, 3, 4, 5, 6, 2, 9, 2, '2']

freq_of = int(input("Enter the element\n"))
if freq_of in List:
    print("Frequency of", freq_of, "is", List.count(freq_of))
else:
    print("It doesn't have any occurrence in the list")
