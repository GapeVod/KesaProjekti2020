import json


filename = 'favourite_numbers.json'

try:
    with open(filename) as f:
        favourite_number = json.load(f)
except FileNotFoundError:
    favourite_number = input("Give your fav number. ")
    with open(filename, 'w') as f:
        json.dump(favourite_number, f)
        print(f"Your fav number is {favourite_number}.")
else:
    print(f"Your fav number is {favourite_number}")


