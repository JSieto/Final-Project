import random

class Number_Game:
    
    def __init__(self):
        self.number = 0
        self.num_guesses = 0
        self.guess_data = {}

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
            return False
        return True

    def guess(self,guess_num):
        self.num_guesses += 1

        if guess_num > self.number:
            print("guess is too large")
            return False
        elif guess_num < self.number:
            print("guess is too small")
            return False
        else:
            print(f"You guessed it in {self.num_guesses} tries!")
            return True


game = Number_Game()

difficulty = input("Choose difficulty (easy, medium, hard): ")

valid_game = game.generate_number(difficulty)

if valid_game:
    correct = False

    while correct == False:
        user_input = input("Enter your guess: ")

        if user_input.isdigit():
            guess = int(user_input)
            correct = game.guess(guess)
        else:
            print("Please enter a valid number")
    
            