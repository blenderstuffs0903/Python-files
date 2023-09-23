file = open('file_1', 'r')
text = file.read()
lines = text.split('\n')
a_num = 0

for line in lines:
    if line[-1] == 'a':
        a_num += 1

print("The number of lines ending with a:", a_num)
