import constants_lists_dict as cld
import pygame
import player as pl

# Functions

# Movment Function
def movement():
  
  '''
  This function grabs the player's keybinds and the jump / crouch height, and then allows the user to jump or crouch as the game runs using the keybinds, these keybinds and values can be change in player.py
  '''
  
  while not cld.quit_game:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        cld.quit_game = True
      if event.type == pygame.KEYDOWN:
        if event.key == pl.player_jump:
          cld.player_y_change = 10#pl.player_jump_height
          print("Jumped")
        elif event.key == pl.player_crouch:
          cld.player_y_change = 10#pl.player_crouch_height
          print("Crouched")
        elif event.key == pygame.K_ESCAPE:
          cld.quit_game = True
          
    cld.player_location_height += cld.player_y_change
    #print("Player Y Change", cld.player_y_change)
    #print("Player Y Pos", cld.player_location_height)
    
    return cld.player_location_height
