from os import system

from Dice import Die


def clear_screen():
    system("clear")

    print("Welcome to the die roll simulator!\n")


die = Die()
roll_again = "Y"
while roll_again == "Y":
    clear_screen()

    die_count = input("How many dice would you like to roll?: ")
    while not die_count.isdigit():
        clear_screen()
        die_count = input("Invalid input. Please enter a valid number: ")
    die_count = int(die_count)

    # print output
    print(f"You rolled {die.roll(die_count)}!")

    # https://calculator.academy/dice-average-calculator/
    # AV=((M+1)/2)∗N
    # Where AV is the average dice value
    # M is the max value of all dice
    # N is the total number of die
    print(
        f"Mathematically, the average total of all roll's is {int(die_count * 3.5)}.\n"
    )

    # ask to roll again
    roll_again = input("Would you like to roll again? (Y/N) ").upper()
    while roll_again not in ["Y", "N"]:
        roll_again = input("Invalid input. Please enter Y or N: ").upper()
