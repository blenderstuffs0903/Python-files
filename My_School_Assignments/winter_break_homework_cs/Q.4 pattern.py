# For loop
for num_1 in range(4, 9, 2):
    for num_2 in range(4, 9, 2):
        if num_2 <= num_1:
            print(num_2, end='')
        else:
            break
    print()

# While loop
a = 4
while a <= 8:
    j = 4
    while j <= a:
        print(j, end='')
        j += 2
    print()
    a += 2
