print("Welcome to Treasure Island. \n Your mission is to find the treasure")

direction = input("You want to go left or right, choose L for left and R for right!").upper()


if direction == "R":
    print("You fell into a hole. Game Over!")
elif direction == "L":
    second_choice = input("You want to swim or wait, write S for swim and W for waiting!").upper()
    if second_choice == "S":
        print("You are attacked by trout. Game over!")
    if second_choice == "W":
        third_choice = input("You see three doors, which one do you choose? red, yellow or blue?").lower()
        if third_choice == "red":
            print("You are burned by fire. Game Over!")
        elif third_choice == "yellow":
            print("YOU WIN, CONGRATULATIONS NIGGAA!")
        elif third_choice == "blue":
            print("You are eaten by beasts. game Over!")
        else:
            print("You chose a door that doesn't exist. Game Over!")
    else:
        print("You chose a wrong option. Game Over!")
else:
    print("You chose a wrong option. Game Over!")
