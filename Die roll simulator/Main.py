from curses.ascii import isdigit
from art import die_face
from random import randint
from os import system


class Die:
    def roll(self, die_count):
        for i in range(die_count):
            print(die_face[randint(1, 6)], end="")
        print()


die = Die()
roll_again = "Y"
while roll_again == "Y":
    system("clear")

    die_count = input("How many dice would you like to roll?: ")
    while not die_count.isdigit():
        die_count = input("Invalid input. Please enter a valid number: ")
    die_count = int(die_count)

    die.roll(die_count)

    roll_again = input("Would you like to roll again? (Y/N) ").upper()
    while roll_again not in ["Y", "N"]:
        roll_again = input("Invalid input. Please enter Y or N: ").upper()
