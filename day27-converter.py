from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 300, height = 200)
window.config(padx = 20, pady = 20)

def calculation():
    number_miles = int(miles_num.get())
    number_km = number_miles * 1.6093
    km_num.config(text = number_km)

is_equal_to = Label(text = "is equal to")
is_equal_to.grid(column = 0, row = 1)

km_num = Label(text = "0")
km_num.grid(column = 1, row = 1)

km = Label(text = "Km")
km.grid(column = 2, row = 1)

miles = Label(text = "Miles")
miles.grid(column = 2, row = 0)

calc_button = Button(text = "Calculate", command = calculation)
calc_button.grid(column = 1, row = 2)

miles_num = Entry()
miles_num.grid(column = 1, row = 0)

window.mainloop()
