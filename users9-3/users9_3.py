class User:
    """asd"""
    def __init__(self, first_name, last_name):
        """asd"""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, how you doing?")

user = User('Ville', 'jestila')
user.describe_user()
user.greet_user()

user2 = User('Mikko', 'Mallikas')
user2.describe_user()
user2.greet_user()

user3 = User('Erkki', 'Sinahka')
user3.describe_user()
user3.greet_user()