# Q: WAP to read a file txt1.txt and count number of lines available in the file.

file = open('txt1.txt', 'r')
text = file.read()

cnt = text.count('\n') + 1

print(f'The number of newlines: {cnt}')
file.close()
