# https://thepythoncode.com/article/make-a-drawing-program-with-python

import ctypes
import sys

import pygame

# Increase Dots Per inch so that the program can look sharp
ctypes.windll.user32.SetProcessDPIAware(True)

# Pygame Configuration
pygame.init()
fps = 300
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
font = pygame.font.SysFont("Arial", 20)

# Variables
# Our Buttons will append themself to this list
objects = []
# Initial color
drawColor = [0, 0, 0]
# Initial brush size
brushSize = 30
brushSizeSteps = 3
# Drawing Area Size
canvasSize = [800, 800]


# Button Class
class Button:
    ...


# Handler Functions
# Changing the Color
def changeColor(color):
    global drawColor
    drawColor = color


# Changing the Brush Size
def changebrushSize(dir):
    global brushSize
    if dir == "greater":
        brushSize += brushSizeSteps
    else:
        brushSize -= brushSizeSteps


# Save the surface to the Disk
def save():
    pygame.image.save(canvas, "canvas.png")


# Button Variables.
buttonWidth = 120
buttonHeight = 35

# Buttons and their respective functions.
buttons = [
    ["Black", lambda: changeColor([0, 0, 0])],
    ["White", lambda: changeColor([255, 255, 255])],
    ["Blue", lambda: changeColor([0, 0, 255])],
    ["Green", lambda: changeColor([0, 255, 0])],
    ["Brush Larger", lambda: changebrushSize("greater")],
    ["Brush Smaller", lambda: changebrushSize("smaller")],
    ["Save", save],
]

# Making the buttons
for index, buttonName in enumerate(buttons):
    Button(
        index * (buttonWidth + 10) + 10,
        10,
        buttonWidth,
        buttonHeight,
        buttonName[0],
        buttonName[1],
    )

# Canvas
canvas = pygame.Surface(canvasSize)
canvas.fill((255, 255, 255))

# Game loop.
while True:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Drawing the Buttons
    for object in objects:
        object.process()

    # Draw the Canvas at the center of the screen
    x, y = screen.get_size()
    screen.blit(canvas, [x / 2 - canvasSize[0] / 2, y / 2 - canvasSize[1] / 2])
