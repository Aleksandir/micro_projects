import tkinter as tk


def converter(conversion_value, unit):
    weight = value.get()
    converted_weight = float(weight) * conversion_value
    value.delete(0, tk.END)
    value.insert(0, f"{round(converted_weight, 1)} {unit}")


options = [
    "Kg to Lb",
    "Lb to Kg",
    "Kg to Oz",
    "Oz to Kg",
    "Lb to Oz",
    "Oz to Lb",
    "Kg to G",
    "G to Kg",
    "G to Lb",
    "G to Oz",
]


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

# row 3
options.grid(column=0, row=3, columnspan=2, pady=10, padx=10)

window.mainloop()
