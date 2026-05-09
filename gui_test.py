#gui_test.py

import pygame
import sys
from ui import draw_intro_screen # Import your drawing function

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

title_font = pygame.font.SysFont('Arial', 80, bold=True)
menu_font = pygame.font.SysFont('Arial', 32)


original_bg = pygame.image.load("assets/intro_forest.png").convert()
current_bg = pygame.transform.scale(original_bg, (WIDTH, HEIGHT))

def main():
    global current_bg, screen 
    # Scene 1: Intro
    running_intro = True
    while running_intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.VIDEORESIZE:

                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                current_bg = pygame.transform.scale(original_bg, (event.w, event.h))

            if event.type == pygame.KEYDOWN:
                running_intro = False

        # Call the drawing function from ui.py
        draw_intro_screen(screen, title_font, menu_font, current_bg)
        pygame.display.flip()

    # Scene 2: Selection (to be built next!)
    print("Moving to selection...")

if __name__ == "__main__":
    main()