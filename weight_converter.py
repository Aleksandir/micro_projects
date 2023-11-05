import tkinter as tk

CONVERT_TO_KG = 0.45359237
CONVERT_TO_LB = 2.2046226218
choice = None


def lb_to_kg():
    weight = value.get()
    converted_weight = float(weight) * CONVERT_TO_KG
    value.delete(0, tk.END)
    value.insert(0, f"{round(converted_weight, 1)} Lb")


def kg_to_lb():
    weight = value.get()
    converted_weight = float(weight) * CONVERT_TO_LB
    value.delete(0, tk.END)
    value.insert(0, f"{round(converted_weight, 1)} Kg")


window = tk.Tk()
window.resizable(width=False, height=False)
window.title("Weight Converter")

# label text
converter_text = tk.Label(text="Weight:")

# buttons
kg_button = tk.Button(text="Lb to Kg", command=lb_to_kg)
lb_button = tk.Button(text="Kg to Lb", command=kg_to_lb)

# Data entry panel
value = tk.Entry(width=10)

# Layout
# row 1
converter_text.grid(column=0, row=1)
value.grid(column=1, row=1, pady=10, padx=10)

# row 2
kg_button.grid(column=0, row=2)
lb_button.grid(column=1, row=2)

# row 3


window.mainloop()
