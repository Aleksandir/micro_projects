from art import die_face
from random import randint
from os import system


class Die:
    def roll(self, die_count):
        count = 0
        for i in range(die_count):
            face = randint(1, 6)
            print(die_face[face], end="")
            count += face
        print()
        return count


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

    print(f"You rolled {die.roll(die_count)}!\n")

    roll_again = input("Would you like to roll again? (Y/N) ").upper()
    while roll_again not in ["Y", "N"]:
        roll_again = input("Invalid input. Please enter Y or N: ").upper()
