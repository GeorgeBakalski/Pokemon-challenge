#gui_test
import pygame
import sys
from pokemon_data import create_pokemon

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon Survival GUI Test")


player_mon = create_pokemon("Charmander")
opponent_mon = create_pokemon("Rhyhorn")

# 4. Load the Images
# Pygame needs to "convert" images to its own format for speed
player_sprite = pygame.image.load(player_mon.back_img).convert_alpha()
opponent_sprite = pygame.image.load(opponent_mon.front_img).convert_alpha()

# Scale them up so they aren't tiny! (The sprites are usually 64x64 or 96x96)
player_sprite = pygame.transform.scale(player_sprite, (300, 300))
opponent_sprite = pygame.transform.scale(opponent_sprite, (250, 250))

# 5. Main Loop
running = True
while running:
    # Check for events (like clicking the 'X' to close the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # DRAWING
    screen.fill((255, 255, 255)) # Fill screen with white

    # Draw Opponent (Top Right)
    screen.blit(opponent_sprite, (450, 50))
    
    # Draw Player (Bottom Left)
    screen.blit(player_sprite, (50, 250))

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()