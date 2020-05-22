prompt = "\nWrite the topping you want on your pizza."
prompt += "\n(Write 'quit' to exit program.) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to pizza")
