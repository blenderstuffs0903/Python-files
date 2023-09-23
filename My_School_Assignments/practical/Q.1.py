def write_str():
    file = open('Para.txt', 'w')
    string = input('Enter a line of strings\n')
    file.write(string)
    file.close()
def search():
    file = open('Para.txt', 'r')
    search = input('Enter the word you want to search\n')
    string = file.read()
    word_list = string.split()
    if search in word_list:
        print("The word exists")
    else:
        print('No such word found')
    file.close()
def python_count():
    file = open('Para.txt', 'r')
    string = file.read()
    word_list = string.split()
    count = 0
    for word in word_list:
        if word.lower() == 'python':
            count += 1
    print("The frequency of the word 'python' is", count)
    file.close()
write_str()
search()
python_count()

