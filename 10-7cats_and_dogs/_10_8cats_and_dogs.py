filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print("File not found.")

