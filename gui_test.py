#gui_test.py

import pygame
import sys
from ui import draw_intro_screen, draw_dialog_box, handle_resize, wrap_text
pygame.init()
pygame.mixer.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

title_font = pygame.font.SysFont('Arial', 80, bold=True)
menu_font = pygame.font.Font("assets/PKMN RBYGSC.ttf", 32)


original_bg = pygame.image.load("assets/intro_forest.png").convert()
current_bg = pygame.transform.scale(original_bg, (WIDTH, HEIGHT))


def main():
    global current_bg, screen, original_bg 
    clock = pygame.time.Clock()

    select_sound = pygame.mixer.Sound("assets/sounds/cling sound.wav")
    pokeball_sound = pygame.mixer.Sound("assets/sounds/pokeball sound.wav")
    
    # --- STATE 1: TITLE ---
    showing_title = True
    while showing_title:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.VIDEORESIZE:
                _, current_bg = handle_resize(event, original_bg)

            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                select_sound.play()
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

    pikachu_sprite = pygame.image.load("assets/sprites/25.png").convert_alpha()
    ball_sprite = pygame.image.load("assets/poke-ball.png").convert_alpha() 
    anim_timer = 0

    original_bg = pygame.image.load("assets/dialog_bg.png").convert()
    curr_w, curr_h = screen.get_size()
    current_bg = pygame.transform.scale(original_bg, (curr_w, curr_h))
    ball_size = int(curr_h * 0.08)

    running_intro = True
    while running_intro:
        clock.tick(60)
        curr_w, curr_h = screen.get_size() 

        oak_height = int(curr_h * 0.4)
        oak_width = oak_height 
        oak_scaled = pygame.transform.scale(oak_sprite, (oak_width, oak_height))

        pika_base_h = int(oak_height * 0.8) # Pikachu is 60% of Oak's height
        pika_base_w = pika_base_h

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.VIDEORESIZE:
                _, current_bg = handle_resize(event, original_bg)
            
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                select_sound.play()
                current_page += 1
                anim_timer = 0
                if current_page >= len(intro_dialog):
                    running_intro = False 

        screen.blit(current_bg, (0, 0)) 

        oak_x = int(curr_w * 0.6) - (oak_width // 2)
        oak_y = int(curr_h * 0.15)
        screen.blit(oak_scaled, (oak_x, oak_y))

        if current_page >= 2:
            anim_timer += 1
            
            # STAGE 1: Hold the ball in hand (Frames 1-30)
            if current_page == 2 and anim_timer < 30:
                ball_x = oak_x + 20 # In his hand area
                ball_y = oak_y + (oak_height // 2.5) 
                screen.blit(pygame.transform.scale(ball_sprite, (ball_size, ball_size)), (ball_x, ball_y))

            # STAGE 2: The Curve Throw (Frames 30-60)
            elif current_page == 2 and 30 <= anim_timer < 60:
                t = (anim_timer - 30) 
                ball_x = oak_x - (t * 4) 
                curve = -0.4 * (t - 15)**2 + 90 
                ball_y = (oak_y + oak_height // 2) - curve
                screen.blit(pygame.transform.scale(ball_sprite, (ball_size, ball_size)), (ball_x, ball_y))

            # STAGE 3: Pikachu Appears and Scales
            elif (current_page == 2 and anim_timer >= 60) or current_page > 2:
                if current_page == 2 and anim_timer == 60:
                    pokeball_sound.play()
                pkmn_x = oak_x - (pika_base_w // 2) + 20 
                pkmn_y = oak_y + oak_height - pika_base_h + ( pika_base_h // 3)
                
                growth = min(1.0, (anim_timer - 60) / 15.0) if current_page == 2 else 1.0
                
                final_w = int(pika_base_w * growth)
                final_h = int(pika_base_h * growth)
                
                pika_scaled = pygame.transform.scale(pikachu_sprite, (final_w, final_h))
                screen.blit(pika_scaled, (pkmn_x, pkmn_y))

        if running_intro and current_page < len(intro_dialog):
            draw_dialog_box(screen, menu_font, intro_dialog[current_page])

        pygame.display.flip()

    print("Moving to selection...")
if __name__ == "__main__":
    main()