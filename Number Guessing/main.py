import random

# ASCII Art for the game
ascii_art = r"""
  _   _                 _                  _____                     
 | \ | |               | |                / ____|                    
 |  \| |      _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ 
 | . ` |/ _ \| '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __|
 | |\  | (_) | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \
 |_| \_|\___/|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/
                                                                     
                                                                     
"""

# INFORMATION ABOUT THE GAME!
print(ascii_art)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100!")

# Here we ask the user about the difficulty
difficulty = input("Type the difficulty as 'easy' or 'hard':\n").lower()

lives = 0

if difficulty == "easy":
    lives += 10
    print("You have 10 attempts remaining to guess the number.")
elif difficulty == "hard":
    lives += 5
    print("You have 5 attempts remaining to guess the number!")
else:
    print("INVALID DIFFICULTY! SWITCHING TO EASY")
    lives += 10
    print("You have 10 attempts remaining to guess the number.")

# Get a random number from 1 to 100
def random_number():
    number = random.randint(1, 101)
    return number

number = random_number()

# Define the logic of the game
def high_or_low(lives, number):
    game_over = False
    while not game_over:
        user_guess = int(input("Make a guess: "))
        if user_guess == number:
            print(f"YOU WON! The number {number} is correct.")
            game_over = True
            break
        elif user_guess > number:
            print("Too high!")
            lives -= 1
            print(f"You have {lives} lives remaining.")
            if lives == 0:
                print("Your lives are finished! You lost.")
                game_over = True
                break
        elif user_guess < number:
            print("Too low!")
            lives -= 1
            print(f"You have {lives} lives remaining.")
            if lives == 0:
                print("Your lives are finished! You lost.")
                game_over = True
                break

high_or_low(lives, number)
