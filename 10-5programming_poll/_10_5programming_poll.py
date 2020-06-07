filename = 'programming_poll.txt'

prompt = "\nGive us the reason you liek code:"
prompt+= "\nEnter 'quit' anytime you want to end the program. "
reason = ""

while reason != 'quit':
    reason = input(prompt)

    if reason != 'quit':
        with open(filename, 'a') as file_object:
            file_object.write(f"{reason}\n")
