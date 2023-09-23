import random
print("let's play rock paper scissor with computer")
choice = input("Enter you choice, enter '1' for rock, '2' for paper and '3' for scissor\n").strip()


# checking if the user passed a valid input
if choice == "1":
    choice = int(choice)
elif choice == "2":
    choice = int(choice)
elif choice == "3":
    choice = int(choice)


# Telling the user to pass a valid input
while type(choice) is str:
    correction = input("Your choice was invalid, choose a valid one").strip()
    if correction == "1":
        choice = int(correction)
    elif correction == "2":
        choice = int(correction)
    elif correction == "3":
        choice = int(correction)
    # else:
    #     pass


# computer's choice
comp_choice = random.randint(1, 3)


# printing user's choice
if choice == 1:
    print("You chose rock✊🏻")
elif choice == 2:
    print("You chose paper🖐🏻")
elif choice == 3:
    print("You chose scissor✌🏻")
else:
    print("Your selection is invalid, you lose!")


# printing computer's choice
if choice == comp_choice:
    if choice == 1:
        print("Computer also chose rock✊🏻")
    elif choice == 2:
        print("Computer also chose paper🖐🏻")
    elif choice == 3:
        print("Computer also chose scissor✌🏻")
elif comp_choice == 1:
    print("Computer chose rock✊🏻")
elif comp_choice == 2:
    print("Computer chose paper🖐🏻")
elif comp_choice == 3:
    print("Computer chose scissor✌🏻")


# defining the winner
if choice == 1 and comp_choice == 3:
    print("You win!")
elif choice == 2 and comp_choice == 1:
    print("You win!")
elif choice == 3 and comp_choice == 2:
    print("You win!")
elif choice == comp_choice:
    print("It's a draw!")
else:
    print("You lose😥")
