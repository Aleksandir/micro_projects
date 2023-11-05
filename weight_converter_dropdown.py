import tkinter as tk


def convert():
    conversion_type = clicked.get()
    weight = float(value.get())
    conversion_value = conversions[conversion_type]
    converted_weight = weight * conversion_value
    value.delete(0, tk.END)

    if converted_weight < 1:
        value.insert(0, f"{round(converted_weight, 3)} {conversion_type[-2:]}")
    else:
        value.insert(0, f"{round(converted_weight, 1)} {conversion_type[-2:]}")


conversions = {
    "g to Kg": 0.001,
    "g to Lb": 0.00220462,
    "g to Oz": 0.035274,
    "Kg to G": 1000,
    "Kg to Lb": 2.20462,
    "Kg to Oz": 35.274,
    "Oz to Lb": 0.0625,
    "Oz to Kg": 0.0283495,
    "Lb to Kg": 0.453592,
    "Lb to Oz": 16,
}

options = list(conversions.keys())


window = tk.Tk()
window.resizable(width=False, height=False)
window.title("Weight Converter")

# label text
converter_text = tk.Label(text="Weight:")

# drop down menu
clicked = tk.StringVar(window)
clicked.set(options[0])
options = tk.OptionMenu(window, clicked, *options)

# if the user selects a new option, make the entry box blank
clicked.trace("w", lambda *args: value.delete(0, tk.END))

# Data entry panel
value = tk.Entry(width=10)

# convert button
convert_button = tk.Button(text="Convert", command=convert)

# Layout
# colum o
converter_text.grid(column=0, row=1)

# colum 2
value.grid(column=1, row=1, pady=10, padx=10)

# colum 3
options.grid(column=0, row=3, columnspan=2)
convert_button.grid(column=0, row=4, columnspan=2)


window.mainloop()
