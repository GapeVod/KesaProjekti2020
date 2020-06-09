import json


filename = 'favourite_number.json'

with open(filename) as f:
    favourite_number = json.load(f)
    print(f"Your fav number is {favourite_number}!")
