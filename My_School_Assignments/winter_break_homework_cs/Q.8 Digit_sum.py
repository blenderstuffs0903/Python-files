num = int(input("Enter the number"))
digit_sum = 0
while num > 0:
    digit_sum += num % 10
    num //= 10
print(digit_sum)

num = input("Enter the number")
digit_sum = 0
for digit in num:
    digit_sum += int(digit)
print(digit_sum)
