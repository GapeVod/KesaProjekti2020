sandwich_orders = ['sandwich1', 'pastrami', 'sandwich2', 'pastrami', 'sandwich3', 'pastrami']
finished_sandwiches = []

print("We no have pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"Making your {sandwich}")
    finished_sandwiches.append(sandwich)

for sandwicher in finished_sandwiches:
    print(sandwicher)
