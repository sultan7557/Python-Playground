import os

blind_auction = """
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
"""

print(blind_auction)
print("Welcome to the Silent Auction by Ali Sultan!")

bidding_dictionary = {}


name = input("What is your name?: ")


money = int(input("What is your bid?: $"))

bidding_dictionary[name] = money


game_over = False



while not game_over:
    second_input = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if second_input == "yes":
        os.system('clear')
        name = input("What is your name?: ")
        money = int(input("What is your bid?: $"))
        bidding_dictionary[name] = money


    elif second_input == "no":
        max_bid = 0
        winner = ""
        
        for person in bidding_dictionary:
            if bidding_dictionary[person] > max_bid:
                max_bid = bidding_dictionary[person]
                winner = person
        

        print(f"{person} is the winner with the bid of {max_bid}")
        game_over = True
        break

    



