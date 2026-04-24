import random

print('\nYou are about to play number guessing game.\nThis game has three difficulty levels:\n')
print('Easy allows you to have a maximum number of 15 guesses.\n')
print('Medium allows a maximum of 10 guesses.\n')
print('Hard allows only 5.\n')

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty.lower()
        self.max_number = 100   # set range
        self.set_difficulty()
        self.guesses = 0
        self.answer = random.randint(1, self.max_number)

    def set_difficulty(self): #set difficulty levels
        if self.difficulty == 'easy':
            self.max_guesses = 15
        elif self.difficulty == 'medium':
            self.max_guesses = 10
        elif self.difficulty == 'hard':
            self.max_guesses = 5
        else:
            print("Invalid difficulty. Defaulting to medium.")
            self.max_guesses = 10

    def play(self):
        print(f"\nDifficulty: {self.difficulty.capitalize()}")
        print(f"Guess a number between 1 and {self.max_number} (type q to quit)")

        while self.guesses < self.max_guesses:
            user_input = input('Your guess: ') #let user input their guesses

            if user_input.lower() == 'q':
                print('Game exited.')
                return

            try:
                my_guess = int(user_input)
        
            except ValueError:
                print('Enter a valid number.')
                continue

            self.guesses += 1

            if my_guess == self.answer:
                print(f'You won in {self.guesses} guesses!')
                return
            elif my_guess < self.answer:
                print('Too low')
            else:
                print('Too high')

            print(f"Guesses left: {self.max_guesses - self.guesses}")

        print(f'You ran out of guesses. The number was {self.answer}')


#Run the game
difficulty = input("Choose difficulty (easy / medium / hard): ")
game = GuessGame(difficulty)
game.play()











