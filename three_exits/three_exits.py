prompt = "\nWrite the topping you want on your pizza."
prompt += "\n(Write 'quit' to exit program.) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to pizza")

prompt = "\nWrite the topping you want on your pizza."
prompt += "\n(Write 'quit' to exit program.) "

#lisä exitit
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
