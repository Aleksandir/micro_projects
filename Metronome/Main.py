from time import sleep
from subprocess import Popen
import keyboard
import os
import PySimpleGUI as sg


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


# GUI design
sg.theme("DarkAmber")
layout = [
    [sg.Text("Enter the BPM: ")],
    [sg.InputText(key="bpm")],
    [sg.Button("Start"), sg.Button("Stop")],
    [sg.Button("quit")],
]
window = sg.Window("Metronome", layout)


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


metronome = Metronome(60)


#! currently wont quit or change bpm after being called
def main():
    while True:
        event, values = window.read()
        bpm = int(values["bpm"])
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "Start":
            metronome.bpm = bpm
            metronome.play_metronome()
        elif event == "Stop":
            metronome.action = "stop"
        elif event == "quit":
            break


main()
