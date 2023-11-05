import tkinter as tk
from subprocess import Popen
from time import sleep


class Metronome:
    def __init__(self, bpm):
        self.bpm = bpm
        self.loop_interval = 60 / bpm
        self.action = ""
        self.sound = ["afplay", "Metronome/beep.mp3"]

    def play_metronome(self):
        while True:
            # Check if the stop action has been triggered
            if self.action == "stop":
                self.action = ""  # Reset the action attribute
                break

            # Play the sound
            Popen(self.sound)

            # Wait for the remaining time in the loop interval
            sleep(self.loop_interval)

    @property
    def bpm(self):
        return self._bpm

    @bpm.setter
    def bpm(self, value):
        self._bpm = value
        self.loop_interval = 60 / value


window = tk.Tk()

# GUI design
bpm = tk.Entry(width=10)
start = tk.Button(text="Start")
stop = tk.Button(text="Stop")

# Layout
window.title("Metronome")
window.resizable(width=False, height=False)
bpm.grid(column=0, row=0, columnspan=2)
start.grid(column=0, row=1)
stop.grid(column=1, row=1)

# def get_bpm():
#     while True:
#         bpm_str = input("Enter the BPM (or q to quit): ")
#         # checking if in string due to extra space when first checked
#         if "q" in bpm_str.lower():
#             return None
#         try:
#             bpm = int(bpm_str)
#             return bpm
#         except ValueError:
#             print("Invalid input. Please enter a valid integer or q to quit.")


#! currently wont quit or change bpm after being called
def main():
    metronome = Metronome(0)
    window.mainloop()
    while True:
        bpm = bpm.get()
        if start:
            metronome.bpm = bpm
            metronome.loop_interval = 60 / bpm
            metronome.play_metronome()
        elif stop:
            metronome.action = "stop"


# main()
