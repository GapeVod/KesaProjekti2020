import json


favourite_number = input("Write your fav number. ")

filename = 'favourite_number.json'
with open(filename, 'w') as f:
    json.dump(favourite_number, f)
    print(f"Your fav number is {favourite_number}!")
