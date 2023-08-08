# Imports, pygame is a library allowing for a windowed game to be played
# Functions is a file with the functions within this program making it easier to navigate
# Constants and lists and dictonaries is where lists, constants and dictonaries are stored
import pygame
from functions import *
from constants_lists_dict import *
import time
from player import *

# Sets up pygame within the program, screen is the screen size for the program pulling from constants..., fills background colour
pygame.init()
pygame.display.update()


# Main Routine
while not quit_game:
  movement()

# Play Again


# Quit Game

