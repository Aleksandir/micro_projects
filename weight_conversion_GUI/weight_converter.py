import tkinter as tk


def converter(conversion_value, unit):
    weight = value.get()
    converted_weight = float(weight) * conversion_value
    value.delete(0, tk.END)
    value.insert(0, f"{round(converted_weight, 1)} {unit}")


window = tk.Tk()
window.resizable(width=False, height=False)
window.title("Weight Converter")

# label text
converter_text = tk.Label(text="Weight:")

# buttons
kg_button = tk.Button(text="Lb to Kg", command=lambda: converter(0.45359237, "kg"))
lb_button = tk.Button(text="Kg to Lb", command=lambda: converter(2.2046226218, "lb"))

# Data entry panel
value = tk.Entry(width=10)

# Layout
# colum o
converter_text.grid(column=0, row=1)
kg_button.grid(column=0, row=2)

# colum 2
value.grid(column=1, row=1, pady=10, padx=10)
lb_button.grid(column=1, row=2)

# row 3


window.mainloop()
