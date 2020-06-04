from random import randint

class Die:
    
    def __init__(self, sides):
        """asd"""
        self.sides = sides

    def roll_die(self):
        """asd"""
        i = 1
        while i < 10:
            print(f"the number is {randint(1, self.sides)} and the number of sides is {self.sides}")
            i += 1
        print("\n")

roll6 = Die(6)
roll6.roll_die()

roll10 = Die(10)
roll10.roll_die()

roll20 = Die(20)
roll20.roll_die()
