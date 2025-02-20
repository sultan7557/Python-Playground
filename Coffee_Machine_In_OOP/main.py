from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
menu = Menu()

game_on = True
while game_on:
    
    user_choice = input(f"What would you like? ({menu.get_items()}): ")
    drink = menu.find_drink(user_choice)
    if user_choice == "off":
        game_on = False
    elif user_choice == "report":
        print(coffeemaker.report(), moneymachine.report())
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        if coffeemaker.is_resource_sufficient(drink):
            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
        

        
