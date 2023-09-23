print("""MENU
SMALL PIZZA:      $15
MEDIUM PIZZA:   $20
LARGE PIZZA:      $25""")
bill = 0
order = input("Type 'S' small 'M' for medium 'L' for large pizza: ")
if order == "S":
    bill = 15
elif order == "M":
    bill = 20
else:
    bill = 25
print("""NOTE
PEPPERONI FOR SMALL PIZZA:                        +$2
PEPPERONI FOR MEDIUM OR LARGE PIZZA: +$3
Extra cheese for any size pizza:                        +$1""")
toppings = input("Do you need pepperoni? 'Y' or 'N'")
if toppings == "Y":
    if order == "M" or order == "L":
        bill += 3
    else:
        bill += 2
extras = input("Do you need extra cheese? 'Y' or 'N'")
if extras == "Y":
    bill += 1
bill = str(bill)
print("The grand total of the pizza is : $" + bill)
