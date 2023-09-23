student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grade = {}

for student in student_scores:
    if 90 < student_scores[student] < 101:
        student_grade[student] = "Outstanding"
    elif 80 < student_scores[student] < 91:
        student_grade[student] = "Exceeds Expectation"
    elif 70 < student_scores[student] < 81:
        student_grade[student] = "Acceptable"
    elif student_scores[student] < 71:
        student_grade[student] = "Fail"

print(student_grade)
