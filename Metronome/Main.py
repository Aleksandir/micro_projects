from curses.ascii import isdigit
from time import sleep
from subprocess import Popen
import keyboard
from os import system


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


quit = ""
bpm = input("Enter the BPM: ")
while quit != "q":
    print("Press space to stop the metronome.")

    metronome = Metronome(int(bpm))
    metronome.play_metronome()

    quit = input("\nPress q to quit or the BPM to continue: ")
    if quit.isdigit():
        bpm = quit
    else:
        quit = str(quit)

    system("clear")
