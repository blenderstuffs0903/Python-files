# Q: WAP to write 10 students record(Roll_no,name,marks) in a text file std.txt and then read all record from the file and display them.

file = open('std.txt', 'w')
std_dict = {}
for num in range(10):
    name = input("Enter the name of the student: ")
    roll_no = int(input("Enter the Roll no.: "))
    marks = int(input('Enter the marks of the student: '))
    std_dict[roll_no] = [name, marks]

file.write(str(std_dict))
file.close()

file = open('std.txt', 'r')
dct = eval(file.read())

for data in dct:
    print(f'Roll no. : {data}, Name: {dct[data][0]}, Marks: {dct[data][1]}')

file.close()

