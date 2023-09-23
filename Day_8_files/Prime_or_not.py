# Write your code below this line 👇
def prime_checker(number):
    count = 0
    i = 1
    if number > 1:
        while i <= n:
            if n % i == 0:
                count += 1
            i += 1
        if count == 2:
            print(number, "is a prime number")
        else:
            print(number, "is a composite number")
    else:
        print(number, "is neither prime nor composite")
# Write your code above this line 👆


# Do NOT change any of the code below👇
n = int(input("Check this number\n"))
prime_checker(number=n)
