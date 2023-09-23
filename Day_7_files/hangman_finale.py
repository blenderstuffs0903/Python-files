import random
import hangman_words
from hangman_words import stages, word_list

# Selection of a random word
chosen_word = random.choice(word_list)

# Display number of '_' equal to number of characters in chosen_word
display = []
num_of_underscores = "_" * len(chosen_word)
display += num_of_underscores

# Assigning lives
lives = 6

# temp
print(display)

# Checking if the word is completely guessed
word_not_guessed = True
previous_enter = []
while word_not_guessed:
    # Telling the user to guess a letter
    guess = input("GUESS A LETTER\n")
    # Checking if the letter entered by the user is in the chosen_word
    for position in range(len(chosen_word)):
        # And also replacing the guessed word with display indices
        if guess == chosen_word[position]:
            display[position] = guess

# Checking if the guess is previously entered
    if guess in previous_enter:
        print("You already entered the letter, enter again.")
    else:
        # Telling the user if the guessed letter is in chosen_word
        if display.count("_") == 0:
            if guess in chosen_word:
                print("You're amazing")
        elif guess in chosen_word:
            print(guess, "is in the word, you're leading")
        # Taking 1 life from the user when he guesses a wrong letter
        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                print("You ran out of lives, you lose")
                print("The correct word was", "'" + chosen_word + "'")
                word_not_guessed = False
            else:
                print(guess, "is not in the word, you lose a live")
                if lives > 1:
                    print(lives, "lives left out of six")
                elif lives == 1:
                    print("Think! only one life left")

    previous_enter += guess

    if "_" not in display:
        print("You won! Yeah it was", "'" + chosen_word + "'")
        word_not_guessed = False
    if word_not_guessed is True:
        print(display)
    print(stages[lives])
