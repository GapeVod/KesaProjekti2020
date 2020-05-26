class Restaurant:
    """the restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """asd"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """asd"""
        print(f"The name of the restaurant is {self.restaurant_name}")
        print(f"The restaurants cuisine is: {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is now open!")

restaurant3 = Restaurant('Ravintola3', 'ruokalaji3')
restaurant2 = Restaurant('Ravintola2', 'ruokalaji2')
restaurant = Restaurant('Ravintola', 'Kiinalainen')
print(f"Restaurants name: {restaurant.restaurant_name}")
print(f"Cuisine type: {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()