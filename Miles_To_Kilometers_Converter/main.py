import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometres Converter!")
window.minsize(width=300, height=200)
window.config(padx=10, pady=10)

#label
label = tkinter.Label(text="Is Equal To!", font=("poppins", 12, "normal"))
label.grid(column=1, row=3)
#Input 
input_field = tkinter.Entry(width=10)
input_field.grid(column=3, row=0)

#Miles label 
miles_label = tkinter.Label(text="Miles", font=("poppins", 12, "normal"))
miles_label.grid(column=4, row=0)


#km label
km_label = tkinter.Label(text="Km", font=("poppins", 12, "normal"))
km_label.grid(column=4, row=3)


#NUMBER OF KILOMATRES LABEL
km_label_number = tkinter.Label(text="0", font=("poppins", 12, "normal"))
km_label_number.grid(column=3, row=3)

#BUTTON
def calculate():
    miles = float(input_field.get())
    miles = miles * 1.609
    km_label_number.config(text=f"{miles}")

button = tkinter.Button(text = "Calculate!", command= calculate)
button.grid(column=3, row=5)








window.mainloop()
