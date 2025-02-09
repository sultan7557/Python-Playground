import random

blackjack_art = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n").lower()
if game_start == 'n':
    print("Goodbye!")
    exit()
elif game_start == 'y':
    print("Let's play Blackjack!")
    print(blackjack_art)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_card():
    return random.choice(cards)

comp_cards = []
user_cards = []

user_first_card = get_card()
user_second_card = get_card()

user_cards.append(user_first_card)
user_cards.append(user_second_card)
print(user_cards)

user_score = sum(user_cards)

comp_first_card = get_card()
comp_second_card = get_card()
comp_cards.append(comp_first_card)
comp_cards.append(comp_second_card)

comp_score = sum(comp_cards)

print(f"Your cards {user_cards}: Current score: {user_score}")
print(f"Computer's first card: {comp_first_card}")

if 11 in user_cards and len(user_cards) == 2 and user_score == 21:
    print("You have a blackjack so you automatically win!")
    game_over = True
else:
    game_over = False

while not game_over:
    want_to_hit = input("Type 'y' to get another card and type 'n' to stall\n").lower()
    
    if want_to_hit == 'y':
        user_third_card = get_card()
        user_cards.append(user_third_card)
        user_score = sum(user_cards)

        # Handle Ace logic
        if 11 in user_cards and user_score > 21:
            user_cards[user_cards.index(11)] = 1
            user_score = sum(user_cards)
        
        print(f"Your cards: {user_cards}: current score: {user_score}")
        if user_score > 21:
            print("You went over, so you lose!")
            game_over = True
            break
    
    elif want_to_hit == 'n':
        while comp_score < 17:
            comp_third_card = get_card()
            comp_cards.append(comp_third_card)
            comp_score = sum(comp_cards)

            # Handle Ace logic
            if 11 in comp_cards and comp_score > 21:
                comp_cards[comp_cards.index(11)] = 1
                comp_score = sum(comp_cards)
            
            print(f"Computers final hand {comp_cards} and final score: {comp_score}")
        
        if comp_score > 21:
            print(f"You win with your cards {user_cards} because the computer went over with cards {comp_cards}!")
            game_over = True
            break
        elif user_score == comp_score:
            print("It is a draw because you have the same cards!")
            game_over = True
            break
        elif user_score > comp_score and user_score <= 21:
            print(f"Your final cards {user_cards}: You win fairly because you had better cards and computer had {comp_cards}!")
            game_over = True
            break
        elif user_score < comp_score and comp_score <= 21:
            print(f"The computer wins because it had better cards {comp_cards}!")
            game_over = True
            break
