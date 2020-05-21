pet_0 = {'animal type': 'cat', 'owner': 'cat lady',}
pet_1 = {'animal type': 'dog', 'owner': 'snoop dogg',}
pet_2 = {'animal type': 'lizard', 'owner': 'lizzy',}

pets = [pet_0, pet_1, pet_2]

for animal in pets:
	print(f"\nAnimal type {animal['animal type']}")
	print(f"\tOwner: {animal['owner'].title()}")