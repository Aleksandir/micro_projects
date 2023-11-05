import threading
import time
import tkinter as tk


class timer:
    def __init__(self, time):
        self.time = time
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run)
            self.thread.start()

    def _run(self):
        while self.running:
            self.time -= 1
            print(self.time)
            time.sleep(1)
            if self.time == 0:
                self.running = False

    def stop(self):
        self.running = False

    def reset(self):
        self.time = 0


# start/stop should be able to start the timer, and press again to pause
# reset should reset the timer to the original time and stop the timer

# create timer object


# create a window

window = tk.Tk()
window.title("Countdown Timer")
window.resizable(False, False)

# create a data entry panel
time_entry = tk.Entry(window, width=15)
time_entry.grid(row=0, column=0, columnspan=2, padx=10)

# create a start/stop button
start_stop_button = tk.Button(window, text="Start")
start_stop_button.grid(row=1, column=0, padx=10)

# create a reset button
reset_button = tk.Button(window, text="Reset")
reset_button.grid(row=1, column=1, padx=10)

# create a label to display the timer
display_label = tk.Label(window, text="00:00:00")
display_label.grid(row=2, column=0, columnspan=2, padx=10)


window.mainloop()
