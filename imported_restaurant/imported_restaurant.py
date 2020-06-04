from module1 import Restaurant, IceCreamStand

my_restaurant = Restaurant('nimi', 'ruoka')
my_restaurant.set_number_served(5)
print(my_restaurant.describe_restaurant())
print(my_restaurant.open_restaurant())
print(my_restaurant.read_customer())

my_icecream = IceCreamStand('joku', 'paska')
print(my_icecream.tell_flavors())

