import random
from hangman_words import word_list


chosen_word = random.choice(word_list)

print(chosen_word)

u_s = []
u_s += "_" * len(chosen_word)

u_s = " ".join(u_s)

print(u_s)
