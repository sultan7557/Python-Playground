import random
# ASCII Art for the game
ascii_art = r"""

  _   _ _       _                  ___         _                           
 | | | (_) __ _| |__   ___ _ __   / _ \ _ __  | |    _____      _____ _ __ 
 | |_| | |/ _` | '_ \ / _ | '__| | | | | '__| | |   / _ \ \ /\ / / _ | '__|
 |  _  | | (_| | | | |  __| |    | |_| | |    | |__| (_) \ V  V |  __| |   
 |_| |_|_|\__, |_| |_|\___|_|     \___/|_|    |_____\___/ \_/\_/ \___|_|   
          |___/                                                            

"""
print(ascii_art)
# Dictionary of data and platforms with their follower counts
data = {
    "data": {
        "Elon Musk": 100000000,
        "Barack Obama": 150000000,
        "Donald Trump": 200000000,
        "Justin Bieber": 250000000,
        "Cristiano Ronaldo": 300000000,
        "Ariana Grande": 350000000,
        "Taylor Swift": 400000000,
        "Katy Perry": 450000000,
        "Rihanna": 500000000,
        "Shakira": 550000000,
        "Selena Gomez": 600000000,
        "Kim Kardashian": 650000000,
        "Kylie Jenner": 700000000,
        "Lionel Messi": 750000000,
        "Neymar Jr": 800000000,
        "Zlatan Ibrahimovic": 850000000,
        "David Beckham": 900000000,
        "LeBron James": 950000000,
        "Kobe Bryant": 1000000000,
        "Michael Jordan": 1050000000,
        "Instagram": 1000000000,
        "Facebook": 1050000000,
        "Twitter": 1100000000,
        "Snapchat": 1150000000,
        "TikTok": 1200000000,
        "YouTube": 1250000000,
        "LinkedIn": 1300000000,
        "Pinterest": 1350000000,
        "Reddit": 1400000000,
    }
}

user_score = 0
game_over = False

while not game_over:
    get_data = list(data["data"])
    first_choice = random.choice(get_data)
    followers_first_choice= data["data"][first_choice]
    second_choice = random.choice(get_data)
    while first_choice == second_choice:
        second_choice = random.choice(get_data)
    followers_second_choice = data["data"][second_choice]
    
    user_choice = input(f"Compare A: {first_choice} with B {second_choice}, WHO has more followers: A or B!\n").lower()
    
    if user_choice == "a" and followers_first_choice > followers_second_choice:
        user_score += 1
        print(user_score)
    elif user_choice == "a" and followers_first_choice < followers_second_choice:
        print(f"You guessed wrong, LOSEEERR! Your final score is {user_score}")
        game_over = True
        break

    elif user_choice == "b" and followers_second_choice > followers_first_choice:
        user_score += 1
        print(user_score)

    elif user_choice == "b" and followers_second_choice < followers_first_choice:
        print(user_score)
        print(f"You guessed wrong, LOSEEERR! Your final score is {user_score}")
        game_over = True
        break

    else:
        print("You entered an invalid answer! Please type A or B")
