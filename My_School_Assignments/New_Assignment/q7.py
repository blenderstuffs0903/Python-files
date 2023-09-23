# Q: WAP to read a file T1_file.txt and write all available digits into another file T2_file.txt.

file1 = open('T1_file.txt', 'r')
file2 = open('T2_file.txt', 'w')
digits = ''

file1_txt = file1.read()

for char in file1_txt:
    if char.isdigit():
        digits += char

file2.write(digits)

file1.close()
file2.close()
