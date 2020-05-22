age = input("\nPlease enter your age to know the price of the ticket ")
age = int(age)

if age < 3:
    print("The ticket is free")
elif age <= 12:
    print("The ticket costs $10")
else:
    print("The ticket costs $15")
