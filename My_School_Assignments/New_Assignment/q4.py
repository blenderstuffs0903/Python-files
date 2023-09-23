# Q: WAP to read a file txt1.txt and count the number of vowels ( a, e,i,o,u ) from the file.

file = open('txt1.txt', 'r')
text = file.read()

count = 0

for char in text:
    if char.lower() in ('a', 'e', 'i', 'o', 'u'):
        count += 1

print(f'The number of vowels: {count}')
file.close()
