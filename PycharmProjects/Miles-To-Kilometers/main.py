from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Labels
miles_label = Label(text="Miles", )
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=10, pady=10)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)
kilometer_label.config(padx=10, pady=10)

output_value_label = Label(text="0")
output_value_label.grid(column=1, row=1)

# Input Entry
input_entry = Entry(width=7)
input_entry.insert(END, string="0")
input_entry.focus()
input_entry.grid(column=1, row=0)


# Calculate Button
def miles_to_km():
    input_value = input_entry.get()
    output_value = round(float(input_value) * 1.609, 1)
    output_value_label.config(text=f"{output_value}")


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
