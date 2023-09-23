# Q13. Write a program using Python to display prime numbers from 2 to 50.

for i in range(1, 51):
    is_prime = True
    for n in range(2, i):
        if i % n == 0:
            is_prime = False
            break
    if is_prime:
        print(i)




