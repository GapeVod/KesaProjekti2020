from module1 import User

class Privileges:
    """asd"""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """asd"""
        print(self.privileges)

class Admin(User):
    def __init__(self, first_name, last_name):
        """asd"""
        super().__init__(first_name, last_name)
        #self.privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = Privileges()
