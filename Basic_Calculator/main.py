def inputs():
    n1 = float(input("What's the first number? "))
    print("\n+\n-\n*\n/\n")
    operation = input("Pick an operation: ")
    n2 = float(input("What's the second number? "))
    return n1, operation, n2

def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Error! Division by zero."

calculation_dictionary = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
}

calculator_art = """
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | * | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

print(calculator_art)
print("Welcome to the Basic Calculator!")

n1, operation, n2 = inputs()

result = calculation_dictionary[operation](n1, n2)
print(f"The result is: {result}")

game_over = False
while not game_over:
    should_continue = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ").lower()
    if should_continue == "y":
        n1 = result
        for symbol in calculation_dictionary:
            print(symbol)
        operation = input("Pick an operation: ")
        n2 = float(input("What's the next number? "))
        result = calculation_dictionary[operation](n1, n2)
        print(f"The result is: {result}")
    elif should_continue == "n":
        n1, operation, n2 = inputs()
        result = calculation_dictionary[operation](n1, n2)
        print(f"The result is: {result}")
    else:
        print("INVALID INPUT")
        game_over = True
