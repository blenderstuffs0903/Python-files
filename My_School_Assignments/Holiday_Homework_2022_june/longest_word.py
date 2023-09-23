words = int(input("How many words you wanna enter?\n"))
lst = []

for num in range(words):
    print("Enter word", num+1)
    word = input()
    lst.append(word)

L_word = lst[0]

for word in lst:
    if len(word) > len(L_word):
        L_word = word

print("The longest word is:", L_word)
