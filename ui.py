#ui.py
import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

def draw_intro_screen(screen, title_font, menu_font, bg_image):
    curr_w, curr_h = screen.get_size()
    
    screen.blit(bg_image, (0, 0))

    # Center text based on the CURRENT screen size
    title_surf = title_font.render("POKEMON SURVIVAL", True, (255, 215, 0))
    title_rect = title_surf.get_rect(center=(curr_w // 2, curr_h // 2 - 50))
    screen.blit(title_surf, title_rect)

    # In ui.py
    start_surf = menu_font.render("Press any key to begin", True, (0, 0, 0))
    # Center it horizontally, but place it lower than the title vertically
    start_rect = start_surf.get_rect(center=(curr_w // 2, curr_h // 2 + 100))
    screen.blit(start_surf, start_rect)