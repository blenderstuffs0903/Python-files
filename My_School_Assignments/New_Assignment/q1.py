# Q: WAP to write 10 student record(Roll_no,name,marks) in a binary file std.txt and then read all record from the file and display them.
import pickle
std_dict = {}


def wrt():
    file = open('bin.dat', 'ab')
    for num in range(10):
        name = input("Enter the name of the student: ")
        roll_no = int(input("Enter the Roll no.: "))
        marks = int(input('Enter the marks of the student: '))
        std_dict[roll_no] = [name, marks]

    pickle.dump(std_dict, file)

    file.close()


def rd():
    file = open('bin.dat', 'rb')
    dct = pickle.load(file)
    for data in dct.keys():
        print(f'Roll no. : {data}, Name: {dct[data][0]}, Marks: {dct[data][1]}')
    file.close()


# wrt()
rd()

