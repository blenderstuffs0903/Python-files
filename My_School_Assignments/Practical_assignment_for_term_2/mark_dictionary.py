Dict = {}
students = int(input("How many students attended the exam?\n"))

for num in range(students):
    print("Enter the name of student", num+1)
    name = input()
    roll_no = input("Enter the student's roll number\n")
    marks = int(input("Enter the student's marks\n"))
    Dict[name] = [roll_no, marks]
    print()
print(Dict, end="\n\n")

print("Students below scored more than 75 percent")
for student in Dict:
    if Dict[student][1] > 74:
        print(student)