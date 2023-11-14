import math
import tkinter as tk


# todo 1.1 LB to KG = 0.453592, make it equal to 0.5
def convert(weight: float, conversion_info: list):
    # conversion_info = {"Kg to Lb": 2.20462}
    """
    Converts the weight value entered by the user based on the selected conversion type.
    The converted weight is returned.
    """

    def round_num(converted_weight, round_to_decimal_pos):
        converted_unit = conversion_info[0].split(" ")[-1]
        return f"{format(round(converted_weight, round_to_decimal_pos), ',')} {converted_unit}"

    conversion_constant = conversion_info[1]
    converted_weight = float(weight) * conversion_constant

    if converted_weight < 1:
        return round_num(converted_weight, 4)
    elif converted_weight < 10:
        return round_num(converted_weight, 3)
    elif converted_weight < 100:
        return round_num(converted_weight, 2)


def main():
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
    choice = tk.StringVar(window)
    choice.set(options[0])
    options = tk.OptionMenu(window, choice, *options)

    # Whenever the value of clicked changes, delete all the text from the value Entry widget
    choice.trace("w", lambda *args: value.delete(0, tk.END))

    # Data entry panel
    value = tk.Entry(width=10)

    # Convert button
    def convert_and_insert():
        weight = value.get()
        conversion_info = (choice.get(), conversions[choice.get()])

        result = convert(weight, conversion_info)

        value.delete(0, tk.END)
        value.insert(0, result)

    convert_button = tk.Button(text="Convert", command=convert_and_insert)

    # Layout
    # colum o
    converter_text.grid(column=0, row=1)

    # colum 2
    value.grid(column=1, row=1, pady=10, padx=10)

    # colum 3
    options.grid(column=0, row=3, columnspan=2)
    convert_button.grid(column=0, row=4, columnspan=2)

    window.mainloop()


if __name__ == "__main__":
    main()
