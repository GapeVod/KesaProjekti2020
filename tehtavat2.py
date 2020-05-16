first_name = "ville"
last_name = "jestila"
full_name = f"{first_name} {last_name}"
message = f"{full_name.title()}, would you liek to learn some Python today?"

print(message)

print({full_name.lower()})
print({full_name.upper()})
print({full_name.title()})

famous_f_name = "albert"
famous_l_name = "einstein"
famous_name = f"{famous_f_name} {famous_l_name}"
message2 = f'{famous_name.title()} once said, "A person who never made a mistake never tried anyting new"'

print(message2)

first_name2 = " mikko\n "
last_name2 = " \tmallikas "
full_name2 = f"{first_name2} {last_name2}"

print(full_name2)
print(full_name2.lstrip())
print(full_name2.rstrip())
print(full_name2.strip())

name = " mikko "

print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

print(5+3)
print(10-2)
print(2*4)
print(16/2)

#favouriteNumber = 9
favouriteNumber = f"{9}"
message3 = f"Ville's favourite number is {favouriteNumber}"
print(message3)