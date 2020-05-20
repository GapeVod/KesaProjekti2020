#5-1
people = ['person1', 'person2', 'person3']
users = people[:]

if 'person1' in users:
	print("true")
else:
	print("false")

if 'person3' in people:
	print("true")
else:
	print("false")

if 'person2' in people and users:
	print("true")
else:
	print("false")

people.append('person4')

users.append('person5')

if 'person4' in users:
	print("true")
else:
	print("false")

if 'person5' in people:
	print("true")
else:
	print("false")

if 'person5' in people and users:
	print("true")
else:
	print("false")

if ('person5' in users) and ('person4' in people):
	print("true")
else:
	print("false")

del users[0]

if 'person1' in users:
	print("true")
else:
	print("false")

if 'person1' in people:
	print("true")
else:
	print("false")

if ('person1' in users) or ('person5' in people):
	print("true")
else:
	print("false")

#5-2
text1 = 'Much message'
text2 = 'Small message'

if text1 == text2:
	print("true")
else:
	print("false")

if text1 != text2:
	print("true")
else:
	print("false")

if text1.lower() == 'much message':
	print("true")
else:
	print("false")

if text2.lower() != 'small message':
	print("true")
else:
	print("false")

number1 = 15
number2 = 21

if number1 == number2:
	print("true")
else:
	print("false")

if number1 != number2:
	print("true")
else:
	print("false")

if number1 > number2:
	print("true")
else:
	print("false")

if number1 < number2:
	print("true")
else:
	print("false")

if number1 >= 15:
	print("true")
else:
	print("false")

if number2 <= number1:
	print("true")
else:
	print("false")

if number1 == 15 and number1 < number2:
	print("true")
else:
	print("false")

if number2 > 15 or number2 <= number1:
	print("true")
else:
	print("false")

if 'person3' in people:
	print("true")
else:
	print("false")

if 'person1' in users:
	print("true")
else:
	print("false")

if 'person1' not in users:
	print("true")
else:
	print("false")

if 'person1' not in people:
	print("true")
else:
	print("false")

#5-3
alien_color = 'green'

if alien_color == 'green':
	print("You just earned 5 points!")

alien_color = 'red'

if alien_color == 'green':
	print("You just earned 5 points!")

#5-4
alien_color = 'green'

if alien_color == 'green':
	print("You just earned 5 points!")
else:
	print("You just earned 10 points!")

alien_color = 'red'

if alien_color == 'green':
	print("You just earned 5 points!")
else:
	print("You just earned 10 points!")

#5-5
alien_color = 'green'

if alien_color == 'green':
	print("You just earned 5 points!")
elif alien_color == 'yellow':
	print("You just earned 10 points!")
else:
	print("You just earned 15 points!")

alien_color = 'yellow'

if alien_color == 'green':
	print("You just earned 5 points!")
elif alien_color == 'yellow':
	print("You just earned 10 points!")
else:
	print("You just earned 15 points!")

alien_color = 'red'

if alien_color == 'green':
	print("You just earned 5 points!")
elif alien_color == 'yellow':
	print("You just earned 10 points!")
else:
	print("You just earned 15 points!")

#5-6
age = 65

if age < 2:
	print("The person is a baby")
elif age >= 2 and age < 4:
	print("The person is a toddler")
elif age >= 4 and age < 13:
	print("The person is a kid")
elif age >= 13 and age < 20:
	print("The person is a teenager")
elif age >= 20 and age < 65:
	print("The person is an adult")
else:
	print("The person is an elder")

#5-7
favourite_fruits = ['fruit1', 'fruit2', 'fruit3']

if 'fruit1'  in favourite_fruits:
	print(f"You really like {favourite_fruits[0]}")

if 'fruit2' and 'fruit3' in favourite_fruits:
	print(f"you really like {favourite_fruits[1]} and {favourite_fruits[2]}")

if 'fruit4' in favourite_fruits:
	print(f"You really like {favourite_fruits[3]}")
else:
	print("thats not in the menu!")

if 'fruit4' or 'fruit3' in favourite_fruits:
	print(f"you really like {favourite_fruits[2]}")

if 'fruit2' and 'fruit4' in favourite_fruits:
	print(f"You really like fruits")
else:
	print("not in menu")

#5-8
user_name = 'admin'
user_list = ['name1', 'name2', 'name3', 'name4', 'admin']

if user_name == 'admin':
	print("hello admin")

for user in user_list:
	if user != 'admin':
		print(f"hello, {user}")

#5-9
user_list = ['name1', 'name2', 'name3', 'name4', 'admin']

for user in user_list:
	if user != 'admin':
		print(f"hello, {user}")
	else:
		print("userlist is empty")

#5-10
current_users = ['c_user1', 'c_user2', 'c_user3', 'c_user4', 'c_user5']

new_users = ['n_user1', 'n_user2', 'n_user3', 'c_user1', 'c_user2']

for new_user in new_users:
	if new_user in current_users:
		print(f"You have to find a new user name, {new_user}.")
	else:
		print(f"the user name, {new_user} is available.")

#5-11
num_list = [value + 1 for value in range (0, 9)]

for num in num_list:
	#print(num)
	if num == 1:
		print(f"{num}st")
	elif num == 2:
		print(f"{num}nd")
	elif num == 3:
		print(f"{num}rd")
	else:
		print(f"{num}th")



