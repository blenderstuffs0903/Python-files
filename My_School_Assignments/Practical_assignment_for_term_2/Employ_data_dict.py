N = int(input("How many employees data you want to store?\n"))

Dict = {}

for num in range(N):
    print("Enter the name of employee", num+1)
    employee = input()
    Dict[employee] = int(input("Enter his salary\n"))

for employee in Dict:
    print("Name:", employee, ",", "Salary:", Dict[employee])
