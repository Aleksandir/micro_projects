from art import die_face, DIE_HEIGHT, DIE_WIDTH, DIE_FACE_SEPARATOR
from random import randint
from os import system


class Die:
    def __init__(self):
        self.die_face = die_face
        self.die_height = DIE_HEIGHT
        self.die_width = DIE_WIDTH
        self.die_face_separator = DIE_FACE_SEPARATOR
        self.die_line_width = 10

    def roll(self, die_count: int):
        """
        Simulates rolling a die.

        Parameters:
        die_count (int): The number of dice to roll.

        Returns:
        int: The total value of the dice rolled.
        """
        count = 0
        dice_rolled = []
        for i in range(die_count):
            roll = randint(1, 6)
            dice_rolled.append(roll)

            count += roll
        self.print_die_face(dice_rolled)
        return count

    def print_die_face(self, dice_rolled: list):
        """
        Prints the ASCII art representation of the dice rolled.

        Parameters:
        dice_rolled (list): A list of integers representing the dice rolled.
        """
        # break the list into lists of 10
        die_rolled_list = []
        for row in range(0, len(dice_rolled), self.die_line_width):
            # append a list of 10 dice rolled to the list
            die_rolled_list.append(dice_rolled[row : row + self.die_line_width])

        # print the die face for each die rolled in the list
        # prints the die face line by line
        # once at end of first list, prints a newline and moves to next list
        for die_set in die_rolled_list:
            for row in range(self.die_height):
                for die in die_set:
                    print(self.die_face[die][row], end=self.die_face_separator)
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
