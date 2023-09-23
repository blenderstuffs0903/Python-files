num = int(input("Enter a number\n"))
rev_num = ""
ori_num = num

while num > 0:
    rev_num += str(num % 10)
    num //= 10

if int(rev_num) == ori_num:
    print("It's a palindrome number")
else:
    print("It's not a palindrome number")

