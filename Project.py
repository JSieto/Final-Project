import random

class Number_Game:
    
    def __init__(self):
        self.number = 0
        self.num_guesses = 0

    def generate_number(self,difficulty):
        if difficulty == "easy":
            self.number = random.randint(1, 100)
        elif difficulty == "medium":
            self.number = random.randint(1, 1000)
        elif difficulty == "hard":
            self.number = random.randint(1, 10000)
        else:
            print("Please enter a valid difficulty")

    def guess(self,guess):
        correct = False

        ##while correct is False: