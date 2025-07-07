from random import randint

class Die:
    # A class that models a fair die.
    def __init__(self, num_of_sides=6):
        # initialize all the attributes.
        if num_of_sides <= 1:
            self.number_of_sides = num_of_sides
        else:
            self.number_of_sides = 6

        self.current_side = 1
    
    def roll(self):
        # A method that simulates the roll of a die.

        self.current_side = randint(1, self.number_of_sides)
        return self.current_side

    def print_current_side(self):
        return f"{self.current_side}"
