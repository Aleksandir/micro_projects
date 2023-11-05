import datetime
import threading
import time
import tkinter as tk


class Timer:
    def __init__(self, time):
        self.time = time
        self.running = False
        self.display = str(datetime.timedelta(seconds=self.time))

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run)
            self.thread.start()

    def _run(self):
        while self.running:
            self.time -= 1
            self.display = str(datetime.timedelta(seconds=self.time))
            display_label["text"] = self.display
            time.sleep(1)
            if self.time == 0:
                self.running = False

    def stop(self):
        self.running = False

    def reset(self):
        self.display
        self.time = 0


# Create the main window
window = tk.Tk()
window.title("Countdown Timer")
window.resizable(False, False)

# Create the Timer object
timer = Timer(0)

# Create the data entry panel
time_entry = tk.Entry(window, width=15)
time_entry.grid(row=0, column=1, columnspan=2, padx=10)


# Define the start/stop function
def start_stop():
    if start_stop_button["text"] == "Start":
        if timer.time == 0:
            timer.time = int(time_entry.get())
        start_stop_button["text"] = "Stop"
        timer.start()
    else:
        start_stop_button["text"] = "Start"
        timer.stop()


# Create the start/stop button
start_stop_button = tk.Button(window, width=5, text="Start", command=start_stop)
start_stop_button.grid(row=1, column=0, padx=10)


# Define the reset function
def reset():
    timer.reset()
    display_label["text"] = "00:00:00"
    start_stop_button["text"] = "Start"


# Create the reset button
reset_button = tk.Button(window, width=5, text="Reset", command=reset)
reset_button.grid(row=1, column=1, padx=10)


# Define the function to update the display label
def update_label():
    display_label["text"] = timer.time
    if timer.running:
        display_label.after(1, update_label)


# Create the display label
display_label = tk.Label(window, text="00:00:00")
display_label.grid(row=2, column=0, columnspan=2, padx=10)

# Create the heading label
heading_label = tk.Label(window, text="Time in seconds")
heading_label.grid(row=0, column=0, padx=10)

# Start the main loop
window.mainloop()
