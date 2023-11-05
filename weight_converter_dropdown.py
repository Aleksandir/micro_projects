import tkinter as tk


def converter(conversion_value, unit):
    weight = value.get()
    converted_weight = float(weight) * conversion_value
    value.delete(0, tk.END)
    value.insert(0, f"{round(converted_weight, 1)} {unit}")


def convert():
    conversion_type = option.get()
    weight = float(weight_entry.get())
    conversion_value = conversions[conversion_type]
    converted_weight = weight * conversion_value


conversions = {
    "Kg to Lb": 2.20462,
    "Lb to Kg": 0.453592,
    "Kg to Oz": 35.274,
    "Oz to Kg": 0.0283495,
    "Lb to Oz": 16,
    "Oz to Lb": 0.0625,
    "Kg to G": 1000,
    "G to Kg": 0.001,
    "G to Lb": 0.00220462,
    "G to Oz": 0.035274,
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

# Data entry panel
value = tk.Entry(width=10)

# Layout
# colum o
converter_text.grid(column=0, row=1)

# colum 2
value.grid(column=1, row=1, pady=10, padx=10)

# colum 3
options.grid(column=0, row=3, columnspan=2, pady=10, padx=10)

window.mainloop()
