alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ceaser_cipher = """ 
 ██████╗███████╗ █████╗ ███████╗███████╗██████╗     
██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗    
██║     █████╗  ███████║███████╗█████╗  ██████╔╝    
██║     ██╔══╝  ██╔══██║╚════██║██╔══╝  ██╔══██╗    
╚██████╗███████╗██║  ██║███████║███████╗██║  ██║    
 ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝    
                                                    
 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗          
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗         
██║     ██║██████╔╝███████║█████╗  ██████╔╝         
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗         
╚██████╗██║██║     ██║  ██║███████╗██║  ██║         
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝         
                                                    
"""
print(f"Welcome to {ceaser_cipher}!")

game_over = False
while not game_over:
    user_wants = input("Type encode to encrypt and decode to decrypt\n").lower()
    
    if user_wants == "encode":
        text = input("Enter your text: ").lower()
        shift = int(input("Enter the shift amount:"))
    
        def encrypt(original_text, shift_amount):
            encrypted_text = ""
        
            for letter in original_text:
                if letter in alphabet:
                    position = (alphabet.index(letter) + shift_amount) % 26
                    encrypted_text += alphabet[position]
                elif letter not in alphabet:
                    encrypted_text += letter
            print(f"Your encoded text is {encrypted_text}")
            return encrypted_text
    
    # Store the returned encrypted text
        encrypted_text = encrypt(original_text=text, shift_amount=shift)
    
    
    
    elif user_wants == "decode":
        
        text = input("Enter your encrypted text: ").lower()
        shift = int(input("Enter the shift amount:"))
        
        
        def decrypt(encrypted_text, shift_amount):
            decrypted_text = ""
            for letter in encrypted_text:
                if letter in alphabet:
                    position1 = (alphabet.index(letter) - shift_amount) % 26
                    decrypted_text += alphabet[position1]
                elif letter not in alphabet:
                    decrypted_text += letter
            print(f"Your decoded text is {decrypted_text}")
            return decrypted_text
        
        # Pass the stored encrypted text to the decrypt function
        decrypt(encrypted_text=encrypted_text, shift_amount=shift)
        
    ask_user_again = input("do you wish to continue or not? type y for yes and n for no!")
    if ask_user_again == "y":
        game_over = False
    elif ask_user_again == "n":
        game_over = True
        break
    else:
        print("You entered an invalid response. Goodbye")
        game_over = True
        break
    





