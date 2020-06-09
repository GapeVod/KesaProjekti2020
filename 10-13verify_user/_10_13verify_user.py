import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username




def get_new_username():
    """Prompt for new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet user by name."""
    username = get_stored_username()
    while True:
        query = input(f"Is {username} your username? (y/n)")
        fl = query[0].lower()
        if query == '' or not fl in ['y', 'n']:
            print("Please aswer with yes or no!")
        else:
            break
    if fl == 'y':
        print(f"Welcome back, {username}!")
    if fl == 'n':
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
    else:
        print("Please enter y or n")



greet_user()
