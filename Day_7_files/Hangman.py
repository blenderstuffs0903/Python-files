import random
from hangman_words import word_list, stages


def list_to_str(list1, str1):
    for char in list1:
        str1 += char + " "

    return str1[: -1]


# Selection of a random word
chosen_word = random.choice(word_list).lower()
# # temp
# print(chosen_word)

# display underscores = num of char in chosen_word
display = []
str2 = ""
display += "_" * len(chosen_word)
print(list_to_str(display, str2))


word_not_guessed = True
# assigning lives
lives = 6

# variable to store previously entered letters
pre_let = []


# looping till the word is completely guessed or the player has loosen
while word_not_guessed:
    # Asking the user to guess a letter to search for it in the chosen word
    guess = input("GUESS A LETTER\n").strip().lower()

    # checking if the guessed exists in the word and replacing it
    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess
    # checking that the letter is previously entered
    if guess in pre_let:
        # telling the user that the guessed word is in the word
        print("You entered it previously, enter again")
    elif guess in chosen_word:
        print(guess, "is in the word, you're leading")
    # taking 1 life if the guessed word is not in the chosen_word
    # elif guess not in chosen_word:
    else:
        if guess not in pre_let:
            lives -= 1
            print(stages[lives])
            if lives == 0:
                print("💔You ran out of lives, you lose")
                print("The correct word was", chosen_word)
                word_not_guessed = False
            else:
                print(guess, "is not in the word, you lose a live")
                if lives > 1:
                    print("❤" * lives)
                else:
                    print("Think! only one 💜 left.")

    pre_let += guess

    if "_" not in display:
        print("You got the word, you won!")
        word_not_guessed = False
    if word_not_guessed is True:
        print(list_to_str(display, str2))



