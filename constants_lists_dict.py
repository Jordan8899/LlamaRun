import pygame
# Dictonaries

# Colours is a dictonary that holds all colour values for future use
colours = {
  "black": (0, 0, 0),
  "gray": (161, 161, 161),
  "white": (255, 255, 255),
  "red": (255, 20, 20)
}

# Constants

# These are the screen size variables, change these to change the screen size to prefered
screen_height = 1080
screen_width = 1920

# Used for game loop and game death
quit_game = False

# Pixel size, this indicates player size and object size
pixel_size = 25

# Location of Ground
ground_location_height = 500
ground_location_width = 0

ground_width = screen_width

# Location of Player
player_location_height = ground_location_height - pixel_size
player_location_width = 300

# Location of Obstacles
cactus_location_height = ground_location_height - pixel_size


# Game name and icon for the window
game_name = pygame.display.set_caption("  Llama Game")
game_icon = pygame.image.load("images/llama_icon.png")
pygame.display.set_icon(game_icon)

# Screen and background display and colour
screen = pygame.display.set_mode((screen_height, screen_width))
background_colour = screen.fill(colours["gray"])

# Ground that the character jumps on
ground = pygame.draw.rect(screen, colours["black"], [ground_location_width, ground_location_height, (ground_location_width + screen_width), pixel_size])

# Player vertical change for jumping and crouching
player_y_change = 0

# Player Model
player = pygame.draw.rect(screen, colours["red"], [player_location_width, player_location_height, pixel_size, pixel_size])


# Lists


