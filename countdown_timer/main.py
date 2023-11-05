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
# create a data entry panel
# create a start/stop button
# create a reset button
# create a label to display the timer
# create a layout

# count down pane in the middle top
# start button in the middle left and stop in the middle right

# window.mainloop()
