filename = 'guest.txt'

username = input("Give your name.")

with open(filename, 'w') as file_object:
    file_object.write(username)
