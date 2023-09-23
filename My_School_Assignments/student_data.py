print("WELCOME STUDENT MANAGER!\n")
students_dict = {}

# Asking the user that how many student's data he wanna enter
students = int(input("How many student's data you wanna enter?\n"))

for num in range(students):
    print("Enter the admission number of the student", num + 1)
    admin_no = input()
    students_dict[admin_no] = [
        input("Enter the student's name"),
        input("Enter Roll number: "),
        input("Enter Class: "),
        input("Enter Contact number:")
    ]
    print()

# Displaying the data of all students
for admin_no in students_dict:
    print("ADMISSION NUMBER:", admin_no)
    print(
        "Name:", students_dict[admin_no][0],
        "Roll_no:", students_dict[admin_no][1],
        "Class:", students_dict[admin_no][2],
        "Contact:", students_dict[admin_no][3]
    )
print()

# Ask the user if he wants any modification in the data
print("Do you want to perform any modification to students data?")
to_modify = input("Enter 'y' for yes or 'n' for no\n").lower()
print()
if to_modify == 'y':
    to_modify = True
else:
    to_modify = False

# Looping modification process
while to_modify:
    print("Which type of modification do you want to perform?")
    print('''Enter '1' to add a new student's data.
Enter '2' to remove a student's data.
Enter '3' to edit a student's data''')
    modification = int(input())
    print()

    # Add a student's data
    if modification == 1:
        new_stu = int(input("How many student's data you wanna enter?\n"))
        for num1 in range(new_stu):
            print("Enter the admission number of the student", num1 + 1)
            admin_no = input()
            students_dict.update({admin_no: [
                input("Enter the student's name"),
                input("Enter Roll number: "),
                input("Enter Class: "),
                input("Enter Contact number: ")
            ]})
            print()

        # Displaying the data of all students
        for admin_no in students_dict:
            print("ADMISSION NUMBER:", admin_no)
            print(
                "Name:", students_dict[admin_no][0], ",",
                "Roll_no:", students_dict[admin_no][1], ",",
                "Class:", students_dict[admin_no][2], ",",
                "Contact:", students_dict[admin_no][3]
            )
            print()

    # Removing a student's data
    elif modification == 2:
        removed_stu = int(input("How many student's data you wanna remove?\n"))
        for num2 in range(removed_stu):

            # Displaying the data of all students
            for admin_no in students_dict:
                print("ADMISSION NUMBER:", admin_no)
                print(
                    "Name:", students_dict[admin_no][0], ",",
                    "Roll_no:", students_dict[admin_no][1], ",",
                    "Class:", students_dict[admin_no][2], ",",
                    "Contact:", students_dict[admin_no][3]
                )
                print()

            print("Enter the admission number of the student you wanna delete", num2 + 1)
            admin_no = input()
            if admin_no in students_dict:
                students_dict.pop(admin_no)
            else:
                print("No record of the student with admission number", admin_no)
            print()

    #elif modification == 3:


    # Asking the user if he wants further modifications
    print("Do you want to perform any further modification?")
    to_modify = input("Enter 'y' for yes or 'n' for no\n").lower()
    # Terminating the loop if no modifications are needed
    if to_modify == 'n':
        to_modify = False


# Displaying the data of all students
for admin_no in students_dict:
    print("ADMISSION NUMBER:", admin_no)
    print(
        "Name:", students_dict[admin_no][0], ",",
        "Roll_no:", students_dict[admin_no][1], ",",
        "Class:", students_dict[admin_no][2], ",",
        "Contact:", students_dict[admin_no][3],
    )
    print()
    print(
        '''Enter 1 to find a students data,
Enter 2 
        ''')
