rivers = {'nile': 'egypt', 'thames': 'UK', 'ganges': 'India'}

for key, value in rivers.items():
	print(f"The {key.title()} runs through {value.title()}.")

for key in rivers.keys():
	print(key.title())

for value in rivers:
	river = rivers[value].title()
	print(river)