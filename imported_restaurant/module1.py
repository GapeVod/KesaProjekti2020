class Restaurant:
    """the restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """asd"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """asd"""
        print(f"The name of the restaurant is {self.restaurant_name}")
        print(f"The restaurants cuisine is: {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is now open!")

    def set_number_served(self, customers):
        """asd"""
        self.number_served = customers

    def increment_number_served(self, customer):
        """asd"""
        self.number_served += customer

    def read_customer(self):
        """asd"""
        print(f"The restaurant has had {self.number_served} customers.")

class IceCreamStand(Restaurant):
    """asd"""
    def __init__(self, restaurant_name, cuisine_type):
        """asd"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['flavor1', 'flavor2', 'flavor3']

    def tell_flavors(self):
        print("These are the ice cream flavors:")
        for flavor in self.flavors:
            print(f"\t\t\t\t{flavor}")
