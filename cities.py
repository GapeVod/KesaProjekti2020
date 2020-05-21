cities = {
	'city1': {
		'country': 'country1',
		'population': 1,
		'fact': 'number one city'
	},
	'city2': {
		'country': 'country2',
		'population': 2,
		'fact': 'number two city'
	},
	'city3': {
		'country': 'country3',
		'population': 3,
		'fact': 'number three city'
	},
}

for city_name, city_info in cities.items():
	print(f"\nCity name: {city_name}")
	country = city_info['country']
	pops = city_info['population']
	fact = city_info['fact']

	print(f"Country: {country.title()}")
	print(f"Population: {pops}")
	print(f"Fact: {fact}")
