import threading
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
        while self.action != "stop":
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


def start():
    if metronome.action == "start":
        return

    metronome.action = "start"
    metronome.bpm = int(bpm.get())
    metronome.loop_interval = 60 / metronome.bpm
    threading.Thread(target=metronome.play_metronome).start()


def stop():
    metronome.action = "stop"


metronome = Metronome(60)

window = tk.Tk()

# data entry panel
bpm = tk.Entry(width=10)

# buttons
start = tk.Button(text="Start", command=start)
stop = tk.Button(text="Stop", command=stop)

# Layout
window.title("Metronome")
window.resizable(width=False, height=False)
bpm.grid(column=0, row=0, columnspan=2)
start.grid(column=0, row=1)
stop.grid(column=1, row=1)

window.mainloop()
