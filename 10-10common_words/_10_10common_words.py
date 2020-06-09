filename = 'alice.txt'

def analyze_words(filename):
    """asd"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.lower().count('cat')
        print(words)

analyze_words(filename)
