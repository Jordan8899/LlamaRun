# Imports
import pygame
import time

# Functions

# Movment Function
def movement(quit_game, player_location_height, player_y_change, player_jump, player_crouch):
  
  '''
  This function grabs the player's keybinds and the jump / crouch height, and then allows the user to jump or crouch as the game runs using the keybinds, these keybinds and values can be change in player.py
  '''
  jump_animation = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  while not quit_game:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit_game = True
      if event.type == pygame.KEYDOWN:
        if event.key == player_jump:
          #player_y_change = 10
          for i in jump_animation:
            player_y_change += 1
            
          print("Jumped")
          print(player_y_change)
          
        elif event.key == player_crouch:
          player_y_change = -10
          print("Crouched")
        elif event.key == pygame.K_ESCAPE:
          quit_game = True
          
    return player_y_change


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

# Sets up pygame within the program, screen is the screen size for the program pulling from constants..., fills background colour
pygame.init()

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

# Player Keybinds used for movement
player_jump = pygame.K_UP
player_crouch = pygame.K_DOWN

# Updates Background and Ground
pygame.display.update()

# Lists



# Main Routine

# Used for game loop and game death
quit_game = False
while not quit_game:

  # Movement Call
  llama_jump_crouch = 0
  llama_jump_crouch = movement(quit_game, player_location_height, player_y_change, player_jump, player_crouch)
  
  # Player Model
  player = pygame.draw.rect(screen, colours["red"], [player_location_width, (player_location_height + llama_jump_crouch), pixel_size, pixel_size])

  pygame.display.update()
  
# Play Again


# Quit Game
