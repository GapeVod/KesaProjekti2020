#Store information about pizza being ordered.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}

#Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza"
	" with the folowwing toppings:")

for topping in pizza['toppings']:
	print(f"\t{topping}")