import random
from art import logo

def number_generation():
    return random.randrange(1,101) 

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty_selection = input("Choose a difficulty. Type 'easy' or 'hard': ")

def number_of_lives(answer):
    if answer == "easy":
        return 10
    else:
        return 5

lives = number_of_lives(answer=difficulty_selection)
number = number_generation()

while lives != 0:
    print(f"You have {lives} attempts remaining to guess the number")
    user_guess = int(input("Make a guess: "))
    if user_guess > number:
        print("Too high.")
        lives -= 1
        if lives != 0:
            print("Guess again.")
        if lives == 0:
            print(f"You've run out of guesses, you lose. The answer was {number}.")
        print("")
    elif user_guess < number:
        print("Too low.")
        lives -= 1
        if lives != 0:
            print("Guess again.")
        if lives == 0:
            print(f"You've run out of guesses, you lose. The answer was {number}.")
        print("")
    elif user_guess == number:
        print(f"You got it! The answer was {number}.")
        lives = 0
        
