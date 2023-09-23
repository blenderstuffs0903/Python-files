file = open('file_1', 'r')
text = file.read()
file.close()
words = text.split()
a_num = 0

for word in words:
    if word[-1] == 'a':
        a_num += 1

print("The number of words ending with a:", a_num)



