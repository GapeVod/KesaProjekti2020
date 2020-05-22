number = input("Enter a number and the program will see if it's a multiple of ten: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is multiple of ten.")
else:
    print(f"\nThe number {number} aint multiple of ten.")
