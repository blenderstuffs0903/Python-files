sen = input("Please enter some sentences\n")

l_sen = sen.split()
word_num = len(l_sen)
char_num = len(sen)

alnum = 0
for char in sen:
    if char.isalnum():
        alnum += 1

alnum_per = round((alnum/char_num)*100, 2)

print(sen)

print(f"""Statistics
Number of words: {word_num}
Number of characters: {char_num}
Percentage of alpha numeric words: {alnum_per}%""")
