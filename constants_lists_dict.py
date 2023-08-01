import pygame

# Dictonaries

# Colours is a dictonary that holds all colour values for future use
colours = {
  "black": (0, 0, 0),
  "gray": (161, 161, 161),
  "white": (255, 255, 255)
}

# Constants

# These are the screen size variables, change these to change the screen size to prefered
screen_height = 1920
screen_width = 1080

quit_game = False

game_name = pygame.display.set_caption("  Llama Game")
game_icon = pygame.image.load("images/llama_icon.png")
pygame.display.set_icon(game_icon)

screen = pygame.display.set_mode((screen_height, screen_width))
background_colour = screen.fill(colours["gray"])

ground = pygame.draw.rect(screen, colours["black"], [screen_width / screen_width, screen_height / 3, 1925, 20])

# Lists


