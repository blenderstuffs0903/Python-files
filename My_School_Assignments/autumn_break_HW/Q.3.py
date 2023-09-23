file = open('file_1', 'r')
text = file.read()
words = text.split()
num = 0

for word in words:
    if word.isnumeric():
        num += 1

print("The number of digits ending with a:", num)
