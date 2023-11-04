# from tkinter import *

CONVERT_TO_KG = 0.45359237
CONVERT_TO_LB = 2.2046226218
choice = None


def lb_to_kb(weight):
    return weight * CONVERT_TO_KG


def kg_to_lb(weight):
    return weight * CONVERT_TO_LB


while True:
    print("\nWelcome to the weight converter!")
    print("1. Convert from pounds to kilograms.")
    print("2. Convert from kilograms to pounds.")
    print("3. Quit.\n")

    choice = input("Please enter your choice: ")

    while choice not in ["1", "2", "3"]:
        choice = input("Please enter your choice: ")

    if choice == "1":
        weight = float(input("Enter the weight in pounds: "))
        print(f"The weight in kilograms is {round(lb_to_kb(weight), 1)}")
    elif choice == "2":
        weight = float(input("Enter the weight in kilograms: "))
        print(f"The weight in pounds is {round(kg_to_lb(weight), 1)}")
    elif choice == "3":
        print("Thanks for using the weight converter!")
        break
