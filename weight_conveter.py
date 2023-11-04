import tkinter as tk

CONVERT_TO_KG = 0.45359237
CONVERT_TO_LB = 2.2046226218
choice = None


def lb_to_kb(weight):
    converted_weight = float(weight) * CONVERT_TO_KG
    lb_text.insert(0, f"The weight in kilograms is {round(converted_weight, 1)}")


def kg_to_lb(weight):
    converted_weight = float(weight) * CONVERT_TO_LB
    kg_text.insert(0, f"The weight in pounds is {round(converted_weight, 1)}")


window = tk.Tk()
window.resizable(width=False, height=False)


greeting = tk.Label(text="Welcome to the weight converter!")
greeting.pack(padx=10, pady=10)

kg_text = tk.Label(text="Enter the weight in kilograms: ")
kg_text.pack()

kg_value = tk.Entry()
kg_value.pack()

kg_button = tk.Button(text="Convert to pounds", command=lb_to_kb(kg_value.get()))
kg_button.pack()


lb_text = tk.Label(text="Enter the weight in pounds: ")
lb_text.pack()

lb_value = tk.Entry()
lb_value.pack()

lb_button = tk.Button(text="Convert to kilograms", command=kg_to_lb(lb_value.get()))
lb_button.pack()

window.mainloop()

# if :
#     kg_text = kg_value.get()
#     kg_text.insert(0, f"The weight in pounds is {round(kg_to_lb(weight), 1)}")


# while True:
#     if choice == "1":
#         weight = float(input("Enter the weight in pounds: "))
#         print(f"The weight in kilograms is {round(lb_to_kb(weight), 1)}")
#     elif choice == "2":
#         weight = float(input("Enter the weight in kilograms: "))
#         print(f"The weight in pounds is {round(kg_to_lb(weight), 1)}")
#     elif choice == "3":
#         print("Thanks for using the weight converter!")
#         break
