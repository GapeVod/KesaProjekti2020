seats = input("How many people are in your dinenr group? ")
seats = int(seats)
if seats > 8:
    print("\nYou'll have to wait for a table.")
else:
    print(f"\nYour table for {seats} is ready")
