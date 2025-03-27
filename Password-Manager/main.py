import tkinter as tk
from tkinter import messagebox
import random
import pyperclip


FONT_NAME = "poppins"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    #use list comprehension
    password_list = [random.choice(letters) for item in range(nr_letters)] + [random.choice(symbols) for item in range(nr_symbols)] + [random.choice(numbers) for item in range(nr_numbers)]
    random.shuffle(password_list)
    final_password = "".join(password_list)
    password_input.insert(0, final_password)
    pyperclip.copy(final_password)


# ----------------------SAVE THE DATA INTO FILE DATA.TXT WHEN USER CLICKS ON ADD -------------------- #
def save_data():
    website_input_data = website_input.get()
    email_input_data = email_input.get()
    password_input_data = password_input.get()

    if len(website_input_data) == 0 or len(password_input_data) == 0 or len(email_input_data) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website_input_data, message=f"These are the details entered: \nEmail: {email_input_data}\nPassword: {password_input_data}\nIs it okay to save?")
        if is_ok:
            with open("/Users/alisultan/Desktop/Python/Password-Manager/data.txt", "a") as file:
                file.write(f"{website_input_data} | {email_input_data} | {password_input_data}\n")
            website_input.delete(0, tk.END)
            password_input.delete(0, tk.END)
            website_input.focus()


#UI SETUP
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")


canvas = tk.Canvas(width=200, height=200,bg="white", highlightthickness=0)
logo_image = tk.PhotoImage(file = "/Users/alisultan/Desktop/python/Password-Manager/logo.png")
canvas.create_image(100, 100, image = logo_image)
canvas.grid(column=1, row=0, pady=20)



#Labels
website_label = tk.Label(text="Website:", highlightbackground="white",fg = "black", bg="white", font = (FONT_NAME, 12, "normal"))
website_label.grid(column=0, row= 1,sticky="w", columnspan=1, pady=3)

email_label = tk.Label(text="Email/Username:",highlightbackground="white",fg = "black", bg="white", font = (FONT_NAME, 12, "normal"))
email_label.grid(column=0, row= 2,sticky="w", pady=3, columnspan=1)

password_label = tk.Label(text="Password:", highlightbackground="white",fg = "black", bg="white", font = (FONT_NAME, 12, "normal"))
password_label.grid(column=0, row=3,sticky="w", pady=3, columnspan=1)

#Input fields

website_input = tk.Entry(width = 35, bg="white",fg="black", borderwidth=1, highlightbackground="gray", highlightcolor="blue", insertbackground="black", highlightthickness=1)
website_input.grid(column = 1, row=1, columnspan=2, sticky="ew")
website_input.focus()


email_input = tk.Entry(width = 35,bg="white",fg="black", borderwidth=1, highlightbackground="gray", highlightcolor="blue", insertbackground="black", highlightthickness=1)
email_input.grid(column = 1, row=2, columnspan=2, sticky="ew")
email_input.insert(0, "youremail@example.com")

password_input = tk.Entry(width = 21, bg="white",fg="black", borderwidth=1,highlightbackground="gray", highlightcolor="blue", insertbackground="black", highlightthickness=1)
password_input.grid(column = 1, row=3, sticky="ew")




#Buttons

generate_password_button = tk.Button(text="Generate Password", width=13, highlightthickness = 0, highlightbackground="white", command=generate_password)
generate_password_button.grid(column = 2, row = 3)



add_button = tk.Button(text = "Add", width=36,  highlightthickness = 0, highlightbackground="white", command=save_data) 
add_button.grid(column = 1, row=4, columnspan=2, pady=1)


window.mainloop()
