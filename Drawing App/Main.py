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
