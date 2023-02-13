from tkinter import *

window = Tk()

#####Km to Miles converter#####
# window.title("Km to Mile Converter")
# window.minsize(width=250, height=100)
# window.config(padx=20, pady=20)

# my_label =Label(text= "is equal to", font=("Arial", 10, "normal"))
# my_label.grid(column=1, row=3)

# km_label =Label(text= "Km", font=("Arial", 10, "normal"))
# km_label.grid(column=7, row=2)

# miles_label =Label(text= "Miles", font=("Arial", 10, "normal"))
# miles_label.grid(column=7, row=3)

# mile_resut_label = Label(text = "0")
# mile_resut_label.grid(column=6, row=3)

# def km_to_miles():
#     km = float(input.get())
#     miles = round(km * 0.621371) ## round is used to round up instead of decimal
#     mile_resut_label.config(text = f"{miles}")

# button = Button(text="Calculate", command=km_to_miles)
# button.grid(column=6, row=5)

# #Entry
# input = Entry(width = 5)
# input.grid(column=6, row=2)
# input.get()




####LBs to KG converter########
window.title("Lbs to Kg Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

my_label =Label(text= "is equal to", font=("Arial", 10, "normal"))
my_label.grid(column=1, row=3)

lbs_label =Label(text= "Lbs", font=("Arial", 10, "normal"))
lbs_label.grid(column=7, row=2)

kg_label =Label(text= "Kg", font=("Arial", 10, "normal"))
kg_label.grid(column=7, row=3)

kg_result_label = Label(text = "0")
kg_result_label.grid(column=6, row=3)

def km_to_miles():
    lbs = float(input.get())
    kg = round(lbs * 0.453592) ## round is used to round up instead of decimal
    kg_result_label.config(text = f"{kg}")

button = Button(text="Calculate", command=km_to_miles)
button.grid(column=6, row=5)

#Entry
input = Entry(width = 5)
input.grid(column=6, row=2)
input.get()









window.mainloop()