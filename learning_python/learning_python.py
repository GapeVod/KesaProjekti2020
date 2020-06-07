filename = 'learning_p.txt'


with open(filename) as file_object:
    lines = file_object.readlines()

for value in range(1, 4):
    print("")
    for line in lines:
        print(line.strip())
