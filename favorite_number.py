favorite_numbers = {
	'person1': [1, 11],
	'person2': [2, 22],
	'person3': [3, 33],
	'person4': [4, 44],
	'person5': [5, 55],
}

for name, number in favorite_numbers.items():
	print(f"\n{name.title()}'s favorite numbers are:")
	for numbers in number:
		print(f"\t{numbers}")