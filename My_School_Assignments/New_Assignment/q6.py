# Q: WAP to read a file txt1.txt and replace all vowels ( a, e,i,o,u ) into '*'.

file = open('txt2.txt', 'r+')
txt = file.read()
# txt = txt
print(f'OLD TEXT\n{txt}', end='\n\n')

for vowel in ['a', 'e', 'i', 'o', 'u']:
    txt = txt.replace(vowel, '*')

file.seek(0)
file.truncate(0)
file.write(txt)
file.close()
file = open('txt2.txt', 'r')
new_txt = file.read()
print(f'NEW TEXT\n{new_txt}')

file.close()
