people = {
	'person1': {
		'first': 'person1',
		'last': 'one',
		'age': '1',
		'location': 'location1',
	},
	'person2': {
		'first': 'person2',
		'last': 'two',
		'age': '2',
		'location': 'location2',
	},
	'person3': {
		'first': 'person3',
		'last': 'three',
		'age': '3',
		'location': 'location3',
	},
}

for name, person_info in people.items():
	print(f"\nName{name.title()}")

	full_name = f"{person_info['first']} {person_info['last']}"
	age = person_info['age']
	location = person_info['location']

	print(f"\tFull name: {full_name.title()}")
	print(f"\tAge: {age}")
	print(f"\tLocation: {location.title()}")
