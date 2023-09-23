import random
import re
names = input("Type every ones name, and separate them with ','\n")
name_list = names.split(',')
r = len(name_list)
ran = random.randint(0, r - 1)
payer = name_list[ran]
print(payer, "will pay the bill")


