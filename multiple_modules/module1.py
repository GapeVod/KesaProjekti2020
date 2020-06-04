class User:
    """asd"""
    def __init__(self, first_name, last_name):
        """asd"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, how you doing?")

    def increment_login_attempts(self):
        """asd"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
