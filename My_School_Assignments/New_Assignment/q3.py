# Q: WAP to read a file txt1.txt and count the number of 'this' and 'This' from the file.

file = open('txt1.txt', 'r')
text = file.read()
word_list = text.split()

count = 0

for word in word_list:
    if 'this' in word.lower():
        count += 1

print(f'The number of "this": {count}')
file.close()
