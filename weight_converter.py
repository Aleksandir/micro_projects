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

converter_text = tk.Label(text="Weight:")
kg_button = tk.Button(text="Pounds", command=lb_to_kg)
lb_button = tk.Button(text="Kilograms", command=kg_to_lb)

value = tk.Entry()

converter_text.grid(column=0, row=1)
value.grid(column=1, row=1, pady=10, padx=10)

kg_button.grid(column=0, row=2)
lb_button.grid(column=1, row=2)


# lb_text = tk.Label(text="Enter the weight in pounds: ")
# lb_text.pack()

# lb_value = tk.Entry()
# lb_value.pack()

# # lb_button = tk.Button(text="Convert to kilograms", command=kg_to_lb)
# lb_button.pack()

window.mainloop()
