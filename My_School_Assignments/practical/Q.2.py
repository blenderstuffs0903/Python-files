def push_emp(stack):
    emp_num = int(input('How many employee data you want to enter?\n'))
    for n in range(emp_num):
        emp_id = int(input('Enter employee id\n'))
        emp_name = input('Enter employee name\n')
        emp_data = [emp_id, emp_name]
        stack.append(emp_data)


def pop_emp(stack):
    del_emp = stack.pop()
    print('Following data was deleted...')
    return del_emp


stk = []
push_emp(stk)
print(pop_emp(stk))
