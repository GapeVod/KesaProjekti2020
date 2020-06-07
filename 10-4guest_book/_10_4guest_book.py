filename = 'guest_book.txt'

prompt = "\nGive us your name:"
prompt+= "\nEnter 'quit' anytime you want to end the program. "
name = ""
username = ""
while name != 'quit':
    name = input(prompt)

    if name != 'quit':
        with open(filename, 'a') as file_object:
            file_object.write(f"{name}\n")

