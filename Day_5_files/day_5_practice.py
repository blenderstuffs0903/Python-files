# sum of n natural terms
# way 1
sum = 0
for n in range(0, 101):
    if n % 2 == 0:
        sum += n
print(sum)

# way 2
sum = 0
for n in range(2, 101, 2):
    sum += n
print(sum)


# Fizz_buzz code
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)

