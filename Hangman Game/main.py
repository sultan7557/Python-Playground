import random

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "ximenia", "yellow", "zucchini"]

random_word = random.choice(words)
print(random_word)  # For debugging purposes, you can remove this line in the final version

# Initialize the placeholder with underscores
placeholder = ""
for letter in random_word:
    placeholder += "_"

print(" ".join(placeholder))

correct_letters = []
game_over = False
lives = 6


hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]
while not game_over:



















    user_input = input("Guess a letter: ").lower()
    display = ""
    
    # Update the placeholder with the guessed letter in the correct positions
    if user_input in random_word:
        for i in range(len(random_word)):
            if random_word[i] == user_input:
                display += user_input
            elif random_word[i] in correct_letters:
                display += random_word[i]
            else:
                display += "_"
        correct_letters.append(user_input)
    else:
        lives -= 1
        display = placeholder  # Keep the placeholder unchanged if the guess is wrong
        print(f"Wrong guess! You have {lives} lives left.")
        print(hangman_stages[6 - lives])

    print(" ".join(display))
    
    # Check if the game is over
    if "_" not in display:
        game_over = True
        print("Congratulations! You've guessed the word.")
    elif lives == 0:
        game_over = True
        print("Game over! The word was:", random_word)
        print(hangman_stages[6])
