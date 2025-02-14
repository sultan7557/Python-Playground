coffee_requirements = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "cost": 1.5
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.5
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 3.0
    }
}


ASCII_ART = """
    
 ______     ______     ______   ______   ______     ______        __    __     ______     ______     __  __     __     __   __     ______    
/\  ___\   /\  __ \   /\  ___\ /\  ___\ /\  ___\   /\  ___\      /\ "-./  \   /\  __ \   /\  ___\   /\ \_\ \   /\ \   /\ "-.\ \   /\  ___\   
\ \ \____  \ \ \/\ \  \ \  __\ \ \  __\ \ \  __\   \ \  __\      \ \ \-./\ \  \ \  __ \  \ \ \____  \ \  __ \  \ \ \  \ \ \-.  \  \ \  __\   
 \ \_____\  \ \_____\  \ \_\    \ \_\    \ \_____\  \ \_____\     \ \_\ \ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_\  \ \_\\"\_\  \ \_____\ 
  \/_____/   \/_____/   \/_/     \/_/     \/_____/   \/_____/      \/_/  \/_/   \/_/\/_/   \/_____/   \/_/\/_/   \/_/   \/_/ \/_/   \/_____/ 
                                                                                                                                             


"""
print(ASCII_ART)
game_off = False

# Initial resources
initial_water = 300
initial_milk = 200
initial_coffee = 100
initial_money = 0

# Processing of the money
penny = 0.01
nickel = 0.05
dime = 0.1
quarter = 0.25

# Print report
def print_report():
    print(f"Here is the complete report\n{initial_water}ml of water\n{initial_milk}ml of milk\n{initial_coffee}mg of coffee\n${initial_money} of money")

def calculate_money():
    """
    This function takes in the user input for the amount of money and then returns the total money that the user gave as final money
    """
    print("Please insert coins")
    user_quarters = int(input("How many quarters? ")) * 0.25
    user_dimes = int(input("How many dimes? ")) * 0.1
    user_nickels = int(input("How many nickels? ")) * 0.05
    user_pennies = int(input("How many pennies? ")) * 0.01
    final_money = round(user_quarters + user_dimes + user_nickels + user_pennies, 2)
    return final_money

def resources_required(user_input):
    """
    This function takes in the user_input and returns the resources required for making the users required coffee
    """
    ingredients = coffee_requirements[user_input]
    return ingredients

def check_resources(initial_water, initial_milk, initial_coffee, required_resources):
    if initial_water >= required_resources["water"] and initial_milk >= required_resources["milk"] and initial_coffee >= required_resources["coffee"]:
        return True
    else:
        print("You don't have enough resources")
        return False

def make_coffee(final_money, required_resources, user_input):
    global initial_water, initial_milk, initial_coffee, initial_money
    if final_money >= required_resources["cost"]:
        initial_water -= required_resources["water"]
        initial_milk -= required_resources["milk"]
        initial_coffee -= required_resources["coffee"]
        initial_money += required_resources["cost"]
        change = round(final_money - required_resources["cost"], 2)
        print(f"Here is your change: ${change}")
        print(f"Here is your {user_input}. Enjoy!")
    else:
        print(f"You don't have enough money. Here is your refund: ${final_money}")

game_over = False

while not game_over:
    user_input = input("What would you like? (espresso/latte/cappuccino/report): ").lower()
    if user_input == "off":
        print("Admin request confirmed. Goodbye!")
        game_over = True
    elif user_input == "report":
        print_report()
    elif user_input in coffee_requirements:
        required_resources = resources_required(user_input)
        if check_resources(initial_water, initial_milk, initial_coffee, required_resources):
            final_money = calculate_money()
            make_coffee(final_money, required_resources, user_input)
        else:
            print("Not enough resources to make the coffee.")
    else:
        print("Invalid input. Please choose from espresso, latte, cappuccino, report, or off.")
