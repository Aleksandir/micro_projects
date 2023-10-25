from art import die_face, DIE_HEIGHT, DIE_WIDTH, DIE_FACE_SEPARATOR
from random import randint
from os import system


class Die:
    def __init__(self):
        self.die_face = die_face
        self.die_height = DIE_HEIGHT
        self.die_width = DIE_WIDTH
        self.die_face_separator = DIE_FACE_SEPARATOR

    def roll(self, die_count):
        count = 0
        dice_rolled = []
        for i in range(die_count):
            roll = randint(1, 6)
            dice_rolled.append(roll)

            count += roll
        self.print_die_face(dice_rolled)
        return count

    def print_die_face(self, dice_rolled):
        # loop through the height of the die
        # print the top of each die face separated by the die face separator
        # when at the end of the row, print a newline and move on to the next line
        for i in range(self.die_height):
            for die in dice_rolled:
                print(self.die_face[die][i], end=self.die_face_separator)
            print()


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
