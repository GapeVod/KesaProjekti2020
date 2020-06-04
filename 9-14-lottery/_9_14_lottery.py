from random import choice

lotto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
         'a', 'b', 'c', 'd', 'e']

winning_numbers = []

my_ticket = []

class Lottery:
    """asd"""
    def __init__(self):
        """asd"""
        #self.selection = selection

    def choose_ticket(self):
        """asd"""
        total_times = 0
        i = 1
        while i < 5:
            self.selection = choice(lotto)
            print(f"The winning number is {self.selection}")
            winning_numbers.append(self.selection)
            i += 1

        while my_ticket != winning_numbers:
            self.selection = choice(lotto)
            total_times += 1


lottery = Lottery()
lottery.choose_ticket()
print(winning_numbers)
print(total_times)