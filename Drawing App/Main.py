# https://thepythoncode.com/article/make-a-drawing-program-with-python

import ctypes
import sys

import pygame

# Increase Dots Per inch so that the program can look sharp
ctypes.windll.user32.SetProcessDPIAware(True)
