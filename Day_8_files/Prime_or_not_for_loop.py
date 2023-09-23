num = int(input("Enter the number\n"))
is_prime = True
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False

    if not is_prime:
        print(num, "is a composite number")
    else:
        print(num, "is a prime number")
else:
    print(num, "is neither prime nor composite")
