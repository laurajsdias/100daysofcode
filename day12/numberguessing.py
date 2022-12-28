import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

random_number = random.randint(1, 100)

def guess():
    guess = int(input("Make a guess: "))
    return guess

def compare(new_guess):
    if new_guess > random_number:
        print("Too high.")
        print("Guess again.")
    elif new_guess < random_number:
        print("Too low.")
        print("Guess again.")
    else:
        print(f"You got it! The answer was {random_number}")

def play_game():
    if difficulty == "easy":
        num_attempts = 10
        guess = 0
        while guess != random_number:
            if num_attempts != 0:
                print(f"You have {num_attempts} attempts remaining to guess the number.")
                guess = int(input("Make a guess: "))
                compare(guess)
                num_attempts -= 1
            else:
                print("You've reached the maximum number of guesses!")
                return
    elif difficulty == "hard":
        num_attempts = 5
        guess = 0
        while guess != random_number:
            if num_attempts != 0:
                print(f"You have {num_attempts} attempts remaining to guess the number.")
                guess = int(input("Make a guess: "))
                compare(guess)
                num_attempts -= 1
            else:
                print("You reached the maximum number of guesses!")
                return


difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
play_game()

