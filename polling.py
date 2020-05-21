favourite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
}

for name in favourite_languages.keys():
	print(f"{name.title()}, thank you for taking the poll.")

if 'erin' not in favourite_languages.keys():
	print("Erin, please take our poll!")

if 'erin2' not in favourite_languages.keys():
	print("Erin2, please take our poll!")

if 'erin3' not in favourite_languages.keys():
	print("Erin3, please take our poll!")