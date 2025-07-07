from die import Die

class Game:
    # A game instance
    def __init__(self):
        self.greeting = "Welcome to Roll the Die!\n"
        self.farewell = "Goodbye! Thank you for playing!"
        self.separator = f"*"*40
        self.menu_items = ["Roll the Dice", \
                           "Choose how many dice you want", \
                           "Quit"]
        self.running = True

        # create an empty list of dice.
        self.dice = []


    def run(self):
        # The main loop of the game.
        print(self.greeting,'\n',self.separator)


        while self.running:
            if not self.is_dice():
                self.choose_number_of_dice()

            self.print_menu()
            user_input = self.get_input(": ")

            if '1' in user_input:
                self.roll_the_dice()
                self.print_after_rolling()

            elif '2' in user_input:
                self.delete_all_die()

            elif '3' in user_input:
                self.running = False
                print(self.farewell)
                
            else:
                print("User input error. Try again.")

    def choose_number_of_dice(self):
        # a method for selecting the number of dice.
        number_of_dice = self.get_input(\
            f"How many dice do you want to play with?: ")
        number_of_dice = int(number_of_dice)

        # delete all die before regenerating.
        self.delete_all_die()

        for die in range(0, number_of_dice):
            self.dice.append( Die() )

    def roll_the_dice(self):
        # a method for rolling all dice in the list.
        for die in self.dice:
            die.roll()

    def print_after_rolling(self):
        # a method for printing the results of rolling
        results = ''
        for die in self.dice:
            results += die.print_current_side() + ', '

        # strip off the last comma ,
        results = results.rstrip(', ')
        print(results)

    def delete_all_die(self):
        # removes all the die from the game list
        self.dice = []


    def is_dice(self):
        # check to see if there are any die in the list.
        if len(self.dice) == 0:
            return False
        else:
            return True
        

    def print_menu(self):
        # method to print the main menu.
        counter = 1
        print(self.separator)
        for menu_item in self.menu_items:
            print(f"{counter}. {menu_item}")
            counter += 1
        print(self.separator)

    def get_input(self, message):
        # method for getting input from the user.
        the_input = input(message)
        return the_input
        
### Main Program #########
if __name__ == '__main__':
    game = Game()  # create a Game instance.
    game.run() 
