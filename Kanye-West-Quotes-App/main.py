from tkinter import *
import requests


def get_quote():
    data_from_api = requests.get(url = "https://api.kanye.rest/")
    data_from_api.raise_for_status()
    json_data = data_from_api.json()["quote"]
    print(json_data)
    final_quote =canvas.itemconfig(quote_text, text = json_data, width = 250, font = ("Arial", 24, "bold"))
    return final_quote



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)


canvas = Canvas(width = 300, height = 414)
background_image = PhotoImage(file = "background.png")
canvas.create_image(150, 207, image=background_image)
canvas.grid(row=0, column=0)


quote_text = canvas.create_text(150, 207, text="Kanye Says:", font=("Arial", 24, "bold"))
canvas.grid(row=0, column=0)


kanye_img = PhotoImage(file = "kanye.png")
kanye_button = Button(image = kanye_img, highlightthickness=0, command = get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()
