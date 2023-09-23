import random

print("Welcome to the Number Guessing Game😀")
print("Select the hardness level\n'1' for ease\n'2' for hard\n'3' for infinitesimally hard")
hardness_level = input()

hardness_level = hardness_level.strip().lower()
if hardness_level == '1':
    lives = 10
    print(f"Lives\n{lives * '🖤'}")
    print("I'm guessing a number between 1 to 100, you'll have to find it out.")
    guessed_number = random.randint(1, 101)
elif hardness_level == '2':
    lives = 10
    print("I'm guessing a number between 1 to 1000, you'll have to find it out.")
    print(f"Lives\n{lives * '🖤'}")
    guessed_number = random.randint(1, 1001)
elif hardness_level == '3':
    lives = 15
    print("I'm guessing a number between 1 to 10000, you'll have to find it out.")
    print(f"Lives\n{lives * '🖤'}")
    guessed_number = random.randint(1, 10001)
else:
    print("Your input was invalid!")
    quit()


def life_manager():
    global lives
    lives -= 1
    print(f"Lives\n{lives * '🖤'}")


# print(guessed_number)

game_finished = False

while not game_finished:
    guess = input("Guess the number\n")
    if guess.isdigit():
        guess = int(guess)

    while type(guess) is not int:
        guess = input("Your input was invalid, enter a valid one.\n")
        if guess.isdigit():
            guess = int(guess)

    if guess == guessed_number:
        print("You won!")
        game_finished = True
    if guess > guessed_number:
        life_manager()
        if lives > 0:
            if guess - guessed_number <= 5:
                print(f"Bit high, you lose a life.")

            else:
                print("Too high, you lose a life")

    elif guess < guessed_number:
        if guessed_number - guess <= 5:
            print(f"Bit low, you lose a life")
            life_manager()
        else:
            print("Too low, you lose a life")
            life_manager()

    if lives == 0:
        print("You ran out of lives, you lose!")
        print(f"{guessed_number} was the number")
        game_finished = True

