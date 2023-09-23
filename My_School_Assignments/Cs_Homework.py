Dict = {}

# Getting details of students
for num in range(1):
    print("Enter name of student", num + 1)
    stu_name = input()
    print("Enter", stu_name+"'s roll number")
    roll_num = int(input())
    print("Enter", stu_name+"'s birth date")
    DOB = input()
    print("\n")

    # Getting the marks
    cs = int(input("Enter marks of C.S\n"))
    eng = int(input("Enter marks of English\n"))
    chem = int(input("Enter marks of chemistry\n"))
    phy = int(input("Enter marks of physics\n"))
    math = int(input("Enter marks of maths\n"))

    # Creating a dict of marks
    marks = {
        "English": eng,
        "Chemistry": chem,
        "Physics": phy,
        "maths": math,
        "CS": cs
    }

    # Getting the sum of the marks
    total = sum(marks.values())
    marks["Total"] = total

    # Appending Total to marks
    Dict[roll_num] = [stu_name, DOB, marks]
    print()

print(Dict, end="\n\n")

# Checking if the total is more than 200.
for data in Dict:
    if Dict[data][2]["Total"] > 100:
        print(Dict[data])

