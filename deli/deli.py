sandwich_orders = ['sandwich1', 'sandwich2', 'sandwich3']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"Making your {sandwich}")
    finished_sandwiches.append(sandwich)

for sandwicher in finished_sandwiches:
    print(sandwicher)
