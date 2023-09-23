para = input("Enter a paragraph\n")

word_list = para.split()

for word in word_list:
    word_list[word_list.index(word)] = word.capitalize()

cap_para = " ".join(word_list)
print(cap_para)
