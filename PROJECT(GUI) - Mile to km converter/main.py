from tkinter import *

window = Tk()
window.minsize(width=180, height=100)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def miles_to_km():
    miles = float(input_mile.get())
    km = round(miles * 1.609344)
    result_label["text"] = km


input_mile = Entry(width=10)
input_mile.grid(column=5, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=6, row=1)

is_eqaul_label = Label(text="is equal to")
is_eqaul_label.grid(column=1, row=2)

result_label = Label(text="0")
result_label.grid(column=5, row=2)

km_label = Label(text="Km")
km_label.grid(column=6, row=2)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=5, row=3)














window.mainloop()