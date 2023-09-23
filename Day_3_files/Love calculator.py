name1 = input("Enter your name: \n")
name2 = input("Enter their name: \n")

new_name1 = name1.upper()
new_name2 = name2.upper()

T = new_name1.count("T") + new_name2.count("T")
R = new_name1.count("R") + new_name2.count("R")
U = new_name1.count("U") + new_name2.count("U")
E = new_name1.count("E") + new_name2.count("E")

L = new_name1.count("L") + new_name2.count("L")
O = new_name1.count("O") + new_name2.count("O")
V = new_name1.count("V") + new_name2.count("V")
E = new_name1.count("E") + new_name2.count("E")

true = str(T + R + U + E)
love = str(L + O + V + E)

score = int(true + love)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(score)


