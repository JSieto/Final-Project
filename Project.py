import random

class Number_Game:
    
    def __init__(self):
        self.number = 0
        self.num_guesses = 0

    def generate_number(self,difficulty):
        if difficulty == "easy":
            self.number = random.randint(1, 100)
            print("easy number generated")
        elif difficulty == "medium":
            self.number = random.randint(1, 1000)
            print("medium number generated")
        elif difficulty == "hard":
            self.number = random.randint(1, 10000)
            print("hard number generated")
        else:
            print("Please enter a valid difficulty")

    def guess(self,guess):
        correct = False
        
        if not int(guess):
            print ("please enter a valid guess")

        while correct is False:
            if guess > self.number:
                print("guess is too large")
                self.num_guesses +=1
            elif guess < self.number:
                print("guess is too small")
                self.num_guesses +=1
            else:
                print("you guessed the number")
                self.num_guesses +=1
            