#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
result_for_letters = ""
for alphabet in range(nr_letters):
    alphabet = random.choice(letters)
    result_for_letters += alphabet

result_for_symbols = ""

for symbol in range(nr_symbols):
    symbol = random.choice(symbols)
    result_for_symbols += symbol
    
result_for_numbers = ""

for number in range(nr_numbers):
    number = random.choice(numbers)
    result_for_numbers += number

final_result = result_for_letters + result_for_symbols+result_for_numbers

list_final = list(final_result)
random.shuffle(list_final)

final_password = "".join(list_final)


print(f"your final password is {final_password}")

