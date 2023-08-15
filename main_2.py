# Imports
import pygame
import time

# Functions

# Movment Function
def movement(quit_game, player_location_height, player_y_change, player_jump, player_crouch, has_jumped, has_crouched):
  
  '''
  This function grabs the player's keybinds and the jump / crouch height, and then allows the user to jump or crouch as the game runs using the keybinds, these keybinds and values can be change in player.py
  '''
  
  while not quit_game:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit_game = True
      if event.type == pygame.KEYDOWN:
        if event.key == player_jump and has_jumped == False:
          player_y_change = -10   
            
          print("Jumped")
          has_jumped = True
          
        elif event.key == player_crouch and has_crouched == False:
          player_y_change = 10
          
          print("Crouched")
          has_crouched = True
          
        elif event.key == pygame.K_ESCAPE:
          quit_game = True
          
    return player_y_change


# Game Reset
def game_reset(player_y, cactus_x, quit_game, play_again):
  for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_q:
          print("Quit Game")
          play_again = False
    
        elif event.key == pygame.K_r:
          print("Play Again")
          play_again = True
          
  return play_again

# Score counter
def score_counter(score):
  
  score += 1
  
  return score

# Text box on Display
def message(msg,txt_colour, bkgd_colour, is_score, is_highscore):
  
  """
  Message funtion (msg, txt_colour (colour['colour']), bkgd_colour (colour['colour']), is_score (bool), is_highscore (bool)
  """
  
  if is_score == True:
    txt = font.render(msg, True, txt_colour)
    text_box = txt.get_rect(center = ((screen_width / screen_width + 20), (screen_height / screen_height + 20)))

  elif is_highscore == True:
    txt = font.render(msg, True, txt_colour)
    text_box = txt.get_rect(center = ((screen_width - 185), (screen_height + 20)))
    
  else:
    txt = font.render(msg, True, txt_colour)
    text_box = txt.get_rect(center = ((screen_width / 2), (screen_height / 2)))
    
  screen.blit(txt, text_box)

# Highscore
def load_high_score(score):
    try:
      hi_score_file = open("Highscore.txt", "r")
    except:
      hi_score_file = open("Highscore.txt", "w")
      hi_score_file.write("0")
    hi_score_file = open("Highscore.txt", "r")
    value = hi_score_file.read()

    if score > int(value):
      hi_score_file = open("Highscore.txt", "w")
      hi_score_file.write(str(score))
      value = score
    
    hi_score_file.close()
    return value
  
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
player_y = ground_location_height - pixel_size
player_x = 300

# Location of Obstacles
cactus_y = ground_location_height - pixel_size
cactus_x = screen_width

# Obstacle Speed
speed = 10

# Score
score = 0
  
# Jump and Crouch Control
has_crouched = False
has_jumped = False


# Sets up pygame within the program, screen is the screen size for the program pulling from constants..., fills background colour
pygame.init()

# Fonts
font = pygame.font.Font("paul.ttf", 50)
#font = pygame.font.SysFont("arialblack", 50)

# Game name and icon for the window
game_name = pygame.display.set_caption("  Llama Game")
game_icon = pygame.image.load("images/llama_icon.png")
pygame.display.set_icon(game_icon)

# Screen and background display
screen = pygame.display.set_mode((screen_height, screen_width))

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
play_again = True
game_over = False
while not quit_game and play_again == True:
  while game_over == False:
    # Screen Background
    screen.fill(colours["gray"])
  
    # Ground that the character jumps on
    ground = pygame.draw.rect(screen, colours["black"], 
                              [ground_location_width, 
                               ground_location_height, 
                               (ground_location_width + screen_width),
                               pixel_size])
    
    # Movement Call
    player_y_change = movement(quit_game, player_y, player_y_change, player_jump, player_crouch, has_jumped, has_crouched)
    
    player_y += player_y_change
  
    # Player Jump Control Stops player from going to far up
    if player_y < ground_location_height - 200:
      player_y_change = 10
      
    elif player_y == ground_location_height - pixel_size:
      player_y_change = 0
      has_jumped = False
      has_crouched = False
  
    # Player Crouch Control Stops player from going too far down
    elif player_y > ground_location_height + 10 and has_crouched:
      player_y_change = -10
  
  
    # Obstacle
    cactus = pygame.draw.rect(screen, colours["white"], [cactus_x, cactus_y, pixel_size, pixel_size])
  
    # Obstacle Movement
    cactus_x -= speed
  
    if cactus_x == 0:
      cactus_x = screen_width
  
    if cactus_x == player_x and cactus_y == player_y:
      game_over = True
      #message("You Died to Cactus"), colours["black"], None, False, False
    
    # Player Model
    player = pygame.draw.rect(screen, colours["red"], 
                              [player_x, player_y, pixel_size, pixel_size])
  
    pygame.display.update()

    # Score
    score = score_counter(score)

    # Score Counter
    message("Score: {}".format(score), colours["black"], None, True, False)

    # Highscore Counter
    highscore = load_high_score(score)
    message("Highscore: {}".format(highscore), colours["black"], None, False, True)

    pygame.display.update()
  
  # Play Again
  while game_over == True:
    
    play_game = game_reset(player_y, cactus_x, quit_game, play_again)
    
    if play_game == False:
      quit_game = True
      play_again = False

    elif play_game == True and game_over:
      
      player_y = ground_location_height - pixel_size
      cactus_x = screen_width
      
      quit_game = False
      play_again = True
      game_over = False

      score = 0
      

# Quit Game
print("Game Quit!!!!")