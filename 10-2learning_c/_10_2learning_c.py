filename = 'learning_p.txt'

with open(filename) as file_object:
    for line in file_object:
        newlines = line.replace('python', 'c')
        print(newlines)
