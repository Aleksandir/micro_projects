from time import time, sleep
from subprocess import Popen
import keyboard

sound = ["afplay", "Metronome/beep.mp3"]

# Set the desired number of loops per second
loops_per_second = 60

# Calculate the time interval between each loop
loop_interval = 60 / loops_per_second

# Define the action variable
action = ""


# Define a callback function that is called when the space key is pressed
def on_space_pressed(event):
    global action
    action = "stop"


# Register the callback function for the space key
keyboard.on_press_key("space", on_space_pressed)

# Start the loop
print("Press space to stop the metronome")
while True:
    # Check if the space key has been pressed
    if action == "stop":
        break

    # Play the sound
    Popen(sound)

    # Wait for the remaining time in the loop interval
    sleep(loop_interval)
