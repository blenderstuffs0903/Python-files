from json import dump
List = input("Enter a list of strings\n").split()
Dict_1 = {

}
for word in List:
    if word not in Dict_1:
        Dict_1[word] = List.count(word)

print(dump(Dict_1, indent=4))


