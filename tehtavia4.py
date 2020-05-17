#4-1
pizza = ['pizza1', 'pizza2', 'pizza3']

for pizzas in pizza:
	print(f"I like {pizzas.title()}!")

print("I really love pizza!")

#4-2
animals = ['cat', 'dog', 'squirrel']

for animal in animals:
	print(f"{animal.title()} would make a great pet.")

print("Any of these animals would make a great pet!")

#4-3
numbers20 = [value + 1 for value in range (0, 20)]
print(numbers20)

#4-4
numbersMil = [value + 1 for value in range(0,1000000)]
#print(numbersMil)

#4-5
numbersMil2 = [value + 1 for value in range(0,1000000)]
print(min(numbersMil2))
print(max(numbersMil2))
print(sum(numbersMil2))

#4-6
odd_numbers = list(range(1, 21, 2))

for odd_number in odd_numbers:
	print(odd_number)

#4-7
threes = []

for value in range(3, 31):
	threes.append(value*3)
	#print(threes)

for i in threes:
	print(i)

#4-8
cubes = []

for value in range(1, 11):
	cubes.append(value**3)
	#print(cubes)

for i in cubes:
	print(i)

#4-9

cubes = [value ** 3 for value in range(1, 11)]

for i in cubes:
	print(i)

#4-10
print("The first items in this lsit are:")
print(cubes[:3])

print("Three items from the middle of the lsit are:")
print(cubes[4:7])

print("The last three items in this list are:")
print(cubes[-3:])

#4-11
pizza = ['pizza1', 'pizza2', 'pizza3']
friends_pizza = pizza[:]

pizza.append('pizza4')
friends_pizza.append('pizza5')

print("My favourite pizzas are:")
for pizzas in pizza:
	print(pizzas)

print("Friends favourite pizzas are:")
for fpizza in friends_pizza:
	print(fpizza)

#4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
#This doesen't work:
friend_foods = my_foods
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
for food in my_foods:
	print(food)

print("\nMy friend's favourite foods are:")
for foodF in friend_foods:
	print(foodF)

#4-13
restaurant_foods = ('food1', 'food2', 'food3', 'food4', 'food5')
for restaurant_food in restaurant_foods:
	print(restaurant_food)

#this is for the intended negative reaction from tuple
#restaurant_foods[1] = ('food7')

restaurant_foods = ('food8', 'food2', 'food3', 'food4', 'food9')
for restaurant_food in restaurant_foods:
	print(restaurant_food)