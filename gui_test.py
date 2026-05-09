#gui_test.py

import pygame
import sys
from ui import draw_intro_screen, draw_dialog_box, handle_resize, wrap_text
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

title_font = pygame.font.SysFont('Arial', 80, bold=True)
menu_font = pygame.font.Font("assets/PKMN RBYGSC.ttf", 32)


original_bg = pygame.image.load("assets/intro_forest.png").convert()
current_bg = pygame.transform.scale(original_bg, (WIDTH, HEIGHT))


def main():
    global current_bg, screen, original_bg 
    
    # --- STATE 1: TITLE ---
    showing_title = True
    while showing_title:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.VIDEORESIZE:
                _, current_bg = handle_resize(event, original_bg)

            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                showing_title = False # Move to Dialog

        # Draw the TITLE version
        draw_intro_screen(screen, title_font, menu_font, current_bg)
        pygame.display.flip()

    # --- STATE 2: DIALOGUE ---
    current_page = 0
    intro_dialog = [
    "Hello there! Welcome to the world of POKEMON!",
    "My name is OAK! People call me the POKEMON PROF!",
    "This world is inhabited by creatures called POKEMON!",
    "For some, POKEMON are pets. Others use them for fights.",
    "Your journey of survival is about to begin!",
    "First, tell me, which POKEMON will you choose?"
    ]

    oak_sprite = pygame.image.load("assets/oak.png").convert()
    transparent_color = oak_sprite.get_at((0, 0))
    oak_sprite.set_colorkey(transparent_color)
    oak_scaled = pygame.transform.scale(oak_sprite, (300, 300))
    oak_scaled.set_colorkey(transparent_color)

    original_bg = pygame.image.load("assets/dialog_bg.png").convert()
    curr_w, curr_h = screen.get_size()
    current_bg = pygame.transform.scale(original_bg, (curr_w, curr_h))

    running_intro = True
    while running_intro:
        curr_w, curr_h = screen.get_size() 
        oak_height = int(curr_h * 0.4)
        oak_width = oak_height 
        oak_scaled = pygame.transform.scale(oak_sprite, (oak_width, oak_height))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.VIDEORESIZE:
                _, current_bg = handle_resize(event, original_bg)
            
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                current_page += 1
                if current_page >= len(intro_dialog):
                    running_intro = False 

        # Draw the BACKGROUND + DIALOGUE BOX
        oak_x = int(curr_w * 0.6) - (oak_width // 2)
        oak_y = int(curr_h * 0.15)
        screen.blit(current_bg, (0, 0)) # Redraw background
        screen.blit(oak_scaled, (oak_x, oak_y))
        if running_intro: # Safety check to not index out of range
            draw_dialog_box(screen, menu_font, intro_dialog[current_page])

        pygame.display.flip()

    print("Moving to selection...")
if __name__ == "__main__":
    main()