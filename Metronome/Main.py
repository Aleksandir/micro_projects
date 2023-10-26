from time import sleep
from subprocess import Popen
import keyboard
import os


class Metronome:
    def __init__(self, bpm):
        self.bpm = bpm
        self.loop_interval = 60 / bpm
        self.action = ""
        self.sound = ["afplay", "Metronome/beep.mp3"]

        # Register the callback function for the space key
        keyboard.on_press_key("space", self.on_space_pressed)

    # Define a callback function that is called when the space key is pressed
    def on_space_pressed(self, event):
        self.action = "stop"

    def play_metronome(self):
        while True:
            # Check if the space key has been pressed
            if self.action == "stop":
                break

            # Play the sound
            Popen(self.sound)

            # Wait for the remaining time in the loop interval
            sleep(self.loop_interval)


def get_bpm():
    while True:
        bpm_str = input("Enter the BPM (or q to quit): ")
        # checking if in string due to extra space when first checked
        if "q" in bpm_str.lower():
            return None
        try:
            bpm = int(bpm_str)
            return bpm
        except ValueError:
            print("Invalid input. Please enter a valid integer or q to quit.")


def main():
    os.system("clear")
    while True:
        bpm = get_bpm()
        if bpm is None:
            break

        print(f"BPM set: {bpm}\nPress space to stop the metronome.")

        metronome = Metronome(bpm)
        metronome.play_metronome()

        os.system("clear")


main()
