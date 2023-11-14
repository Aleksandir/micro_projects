from random import randint

die_face = {
    1: (
        "-----",
        "|   |",
        "| o |",
        "|   |",
        "-----",
    ),
    2: (
        "-----",
        "|o  |",
        "|   |",
        "|  o|",
        "-----",
    ),
    3: (
        "-----",
        "|o  |",
        "| o |",
        "|  o|",
        "-----",
    ),
    4: (
        "-----",
        "|o o|",
        "|   |",
        "|o o|",
        "-----",
    ),
    5: (
        "-----",
        "|o o|",
        "| o |",
        "|o o|",
        "-----",
    ),
    6: (
        "-----",
        "|o o|",
        "|o o|",
        "|o o|",
        "-----",
    ),
}
DIE_HEIGHT = len(die_face[1])
DIE_WIDTH = len(die_face[1][0])
DIE_FACE_SEPARATOR = " "


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
