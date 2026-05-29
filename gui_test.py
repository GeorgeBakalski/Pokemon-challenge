#gui_test.py

import pygame
import sys
import math
from ui import draw_intro_screen, draw_dialog_box, handle_resize, draw_move_menu, get_bottom_offset, draw_hp_bar, draw_text, wrap_text
from pokemon_data import get_random_opponent, create_pokemon
from battle import process_battle_round
from moves import MOVES

pygame.mixer.pre_init(44100, -16, 2, 2048) 
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

FONT_CACHE = {}

def get_font(path, size):
    key = (path, size)
    if key not in FONT_CACHE:
        FONT_CACHE[key] = pygame.font.Font(path, size)
    return FONT_CACHE[key]

IMAGE_CACHE = {}

def get_image(path):
    if path not in IMAGE_CACHE:
        IMAGE_CACHE[path] = pygame.image.load(path).convert_alpha()
    return IMAGE_CACHE[path]

title_font = pygame.font.SysFont('Arial', 80, bold=True)
menu_font = get_font("assets/pokemon_fire_red.ttf", 50)


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
                showing_title = False 

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

    pikachu_sprite = get_image("assets/sprites/25.png")
    ball_sprite = get_image("assets/poke-ball.png")
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

        pika_base_h = int(oak_height * 0.8) 
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
                ball_x = oak_x + 20 
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
            max_text_width = curr_w - 60
            wrapped_lines = wrap_text(intro_dialog[current_page], menu_font, max_text_width)
            draw_dialog_box(screen, menu_font, wrapped_lines)

        pygame.display.flip()

        # --- STATE 3: STARTER SELECTION ---
    starter_ball = get_image("assets/poke-ball.png")
    original_bg = pygame.image.load("assets/table.png").convert()
    curr_w, curr_h = screen.get_size()
    current_bg = pygame.transform.scale(original_bg, (curr_w, curr_h))

    starter_data = {
    0: {"name": "Bulbasaur", "image": get_image("assets/sprites/1.png")},
    1: {"name": "Charmander", "image": get_image("assets/sprites/4.png")},
    2: {"name": "Squirtle", "image": get_image("assets/sprites/7.png")}
}
    selected_index = -1 

    ball_size = int(curr_h * 0.15) 
    angles = [0, 5, 10, 5, 0, -5, -10, -5] 
    ball_frames = []
    for a in angles:
        base = pygame.transform.scale(starter_ball, (ball_size, ball_size))
        rotated = pygame.transform.rotate(base, a)
        ball_frames.append(rotated)


    selecting = True
    while selecting:
        clock.tick(60)
        curr_w, curr_h = screen.get_size()
        mouse_pos = pygame.mouse.get_pos()
        hovering_any = False
        
        ball_size = int(curr_h * 0.15)
        positions = [
        (int(curr_w * 0.25) - ball_size // 2, int(curr_h * 0.35)),
        (int(curr_w * 0.50) - ball_size // 2, int(curr_h * 0.35)),
        (int(curr_w * 0.75) - ball_size // 2, int(curr_h * 0.35))
    ]

        ball_rects = [pygame.Rect(pos[0], pos[1], ball_size, ball_size) for pos in positions]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.VIDEORESIZE:
                _, current_bg = handle_resize(event, original_bg)
                new_size = int(event.h * 0.15)
                ball_frames = []
                for a in angles:
                    base = pygame.transform.scale(starter_ball, (new_size, new_size))
                    rotated = pygame.transform.rotate(base, a)
                    ball_frames.append(rotated)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i, rect in enumerate(ball_rects):
                    if rect.collidepoint(mouse_pos):
                        selected_index = i
                        select_sound.play()
                        selecting = False 


        screen.blit(current_bg, (0, 0)) 
        frame_index = (pygame.time.get_ticks() // 100) % len(ball_frames)
        
        for i, rect in enumerate(ball_rects):
            if rect.collidepoint(mouse_pos):
                hovered_index = i
                hovering_any = True
                current_frame = ball_frames[frame_index]
                new_rect = current_frame.get_rect(midbottom=rect.midbottom)
                screen.blit(current_frame, new_rect)
                if hovered_index is not None:
                    # --- 1. SCALE THE BOX ---
                    box_h = int(curr_h * 0.45)
                    box_w = int(box_h * 0.8)
                    preview_rect = pygame.Rect((curr_w // 2) - (box_w // 2), int(curr_h * 0.5), box_w, box_h)
                    
                    pygame.draw.rect(screen, (255, 255, 255), preview_rect) 
                    pygame.draw.rect(screen, (0, 0, 0), preview_rect, 3)    

                    # --- 2. SCALE & CENTER THE SPRITE ---
                    data = starter_data[hovered_index]
                    raw_img = data["image"]
                    
                    sprite_w = int(box_w * 0.9)
                    sprite_h = int(raw_img.get_height() * (sprite_w / raw_img.get_width()))
                    big_img = pygame.transform.scale(raw_img, (sprite_w, sprite_h))
                    img_pos = big_img.get_rect(center=(preview_rect.centerx, preview_rect.top + (box_h * 0.4)))
                    screen.blit(big_img, img_pos)

                    # --- 3. THE NAME PLATE ---
                    plate_h = int(box_h * 0.2)
                    name_plate_rect = pygame.Rect(preview_rect.x, preview_rect.bottom - plate_h, preview_rect.width, plate_h)
                    pygame.draw.rect(screen, (200, 200, 200), name_plate_rect)
                    pygame.draw.rect(screen, (0, 0, 0), name_plate_rect, 2)

                    ui_font_size = int(plate_h * 0.6)
                    temp_font = pygame.font.Font("assets/pokemon_fire_red.ttf", ui_font_size)
                    
                    name_text = temp_font.render(data["name"], True, (0, 0, 0))
                    
                    if name_text.get_width() > name_plate_rect.width - 10:
                        ratio = (name_plate_rect.width - 10) / name_text.get_width()
                        name_text = pygame.transform.scale(name_text, (int(name_text.get_width() * ratio), int(name_text.get_height() * ratio)))

                    name_pos = name_text.get_rect(center=name_plate_rect.center)
                    screen.blit(name_text, name_pos)
            else:
                screen.blit(ball_frames[0], rect)
            

        if hovering_any:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()


       # --- STATE 4: BATTLE SETUP  ---
    opponent = get_random_opponent()
    starter = starter_data[selected_index]
    player = create_pokemon(starter["name"])
    player.level = 5
    opponent.level = player.level - 2
    battle_queue = []
    move_buttons = []

    player_hp = player.get_hp()
    display_player_hp = player_hp 
    player_max_hp = player_hp
    opponent_hp = opponent.get_hp()
    display_opponent_hp = opponent_hp
    opponent_max_hp = opponent_hp
    wins = 0
    battle = "Normal"

    p_name_text = player.name.upper()
    p_lvl_text = f"{player.level}"
    o_name_text = opponent.name.upper()
    o_lvl_text = f"{opponent.level}"

    opp_img = get_image(opponent.front_img)
    player_img = get_image(player.back_img)
    original_bg = pygame.image.load("assets/Backgrounds/grass_bg.png").convert()
    player_plate_img = get_image("assets/player hp.png")
    player_plate_img.set_colorkey((255, 255, 255))
    opp_plate_img = get_image("assets/opponent hp.png")
    opp_plate_img.set_colorkey((255, 255, 255))
    


    battle_state = "MESSAGE"
    current_message = f"A wild {opponent.name} appeared!"
    wrapped_lines = []
    last_wrapped_message = ""
    last_hp_string = ""
    current_hp_string = f"{int(display_player_hp)} / {player_max_hp}"
    p_hp_surf = None
    
    battling = True
    needs_scaling = True
    while battling:
        clock.tick(60)
        curr_w, curr_h = screen.get_size()
        hovering_any = False
        mouse_pos = pygame.mouse.get_pos()
        levels_to_gain = 1
        
        
        # --- 1. CALCULATE SIZES  ---
        if needs_scaling:
            box_height = min(180, curr_h // 4)
            arena_height = curr_h - box_height
            current_bg = pygame.transform.scale(original_bg, (curr_w, arena_height))
            
            opp_scale = int(arena_height * 0.6)
            player_scale = int(arena_height * 0.9)
            opp_scaled = pygame.transform.scale(opp_img, (opp_scale, opp_scale))
            player_scaled = pygame.transform.scale(player_img, (player_scale, player_scale))

            opp_padding = get_bottom_offset(opp_scaled)
            player_padding = get_bottom_offset(player_scaled)
            opp_rect = opp_scaled.get_rect()
            opp_rect.midbottom = (int(curr_w * 0.75), int(arena_height * 0.55) + opp_padding)
            player_rect = player_scaled.get_rect()
            player_rect.midbottom = (int(curr_w * 0.25), (curr_h - box_height) + player_padding)

            plate_scale_factor = (arena_height / 180) 
            dynamic_size = int(11 * plate_scale_factor) 
            ui_font = get_font("assets/pokemon_fire_red.ttf", dynamic_size)

            # Scale the Player Plate
            p_plate_w = int(104 * plate_scale_factor)
            p_plate_h = int(37 * plate_scale_factor) 
            player_plate_scaled = pygame.transform.scale(player_plate_img, (p_plate_w, p_plate_h))
            p_plate_x = curr_w - p_plate_w - 20 
            p_plate_y = arena_height - p_plate_h - 20
            p_bar_x = p_plate_x + (48 * plate_scale_factor)
            p_bar_y = p_plate_y + (17 * plate_scale_factor)


            # Scale the Opponent Plate
            o_plate_w = int(100 * plate_scale_factor)
            o_plate_h = int(29 * plate_scale_factor)
            opp_plate_scaled = pygame.transform.scale(opp_plate_img, (o_plate_w, o_plate_h))
            o_plate_x = 20
            o_plate_y = 20
            o_bar_x = o_plate_x + (39 * plate_scale_factor)
            o_bar_y = o_plate_y + (17 * plate_scale_factor)


            # PLAYER AND OPPONENT NAME AND LEVEL + HP
            
            lv_label_surface = ui_font.render("Lv", True, (64, 64, 64))
            p_lvl_end_x = int(95 * plate_scale_factor)
            o_lvl_end_x = int(87 * plate_scale_factor)

            
            p_name_surface = ui_font.render(p_name_text, True, (64, 64, 64))
            p_lvl_surface = ui_font.render(p_lvl_text, True, (64, 64, 64))

            p_name_x = int(14 * plate_scale_factor)
            p_name_y = int(5 * plate_scale_factor)
            p_lvl_x = p_lvl_end_x - p_lvl_surface.get_width()
            p_lvl_y = int(5 * plate_scale_factor)
            p_lv_label_x = p_lvl_x - lv_label_surface.get_width() - (2 * plate_scale_factor)

            o_name_surface = ui_font.render(o_name_text, True, (64, 64, 64))
            o_lvl_surface = ui_font.render(o_lvl_text, True, (64, 64, 64))

            o_name_x =  int(6 * plate_scale_factor)
            o_name_y = int(5 * plate_scale_factor)
            o_lvl_x = o_lvl_end_x - o_lvl_surface.get_width()
            o_lvl_y = int(5 * plate_scale_factor)
            o_lv_label_x = o_lvl_x - lv_label_surface.get_width() - (2 * plate_scale_factor)

            current_hp_string = f"{int(display_player_hp)} / {player_max_hp}"
            hp_x = p_plate_x + (95 * plate_scale_factor) - ui_font.size(current_hp_string)[0]
            hp_y = p_plate_y + (22 * plate_scale_factor) 

            draw_text(player_plate_scaled, ui_font, p_name_text, p_name_x, p_name_y)
            draw_text(player_plate_scaled, ui_font, p_lvl_text, p_lvl_x, p_lvl_y)
            draw_text(player_plate_scaled, ui_font, "Lv", p_lv_label_x, p_lvl_y)

            draw_text(opp_plate_scaled, ui_font, o_name_text, o_name_x, o_name_y)
            draw_text(opp_plate_scaled, ui_font, o_lvl_text, o_lvl_x, o_lvl_y)
            draw_text(opp_plate_scaled, ui_font, "Lv", o_lv_label_x, o_lvl_y)
            needs_scaling = False


        current_hp_string = f"{int(display_player_hp)} / {player_max_hp}"
        #  SMOOTH HP DRAIN 
        drain_speed = 0.5
            
        if display_player_hp > player_hp:
            display_player_hp -= drain_speed
            if display_player_hp < player_hp: 
                display_player_hp = player_hp
        elif display_player_hp < player_hp: 
            display_player_hp += drain_speed
                
        if display_opponent_hp > opponent_hp:
            display_opponent_hp -= drain_speed
            if display_opponent_hp < opponent_hp:
                display_opponent_hp = opponent_hp
        # TEXT AND HP

        
        if current_hp_string != last_hp_string:
            last_hp_string = current_hp_string
            hp_x = p_plate_x + (95 * plate_scale_factor) - ui_font.size(current_hp_string)[0]
            p_hp_surf = ui_font.render(current_hp_string, True, (64, 64, 64))
            p_hp_shadow = ui_font.render(current_hp_string, True, (208, 208, 200))

        # --- 2. DRAWING ---

        screen.blit(current_bg, (0, 0))
        screen.blit(opp_scaled, opp_rect)
        screen.blit(player_scaled, player_rect)

        screen.blit(player_plate_scaled, (p_plate_x, p_plate_y))
        screen.blit(opp_plate_scaled, (o_plate_x, o_plate_y))
        
        # For HP numbers
        screen.blit(p_hp_shadow, (hp_x + 1, hp_y + 1))
        screen.blit(p_hp_surf, (hp_x, hp_y))

        draw_hp_bar(screen, p_bar_x, p_bar_y, display_player_hp, player_max_hp, plate_scale_factor)
        draw_hp_bar(screen, o_bar_x, o_bar_y, display_opponent_hp, opponent_max_hp, plate_scale_factor)

        # --- 3. INPUT  ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.VIDEORESIZE:
                needs_scaling = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                select_sound.play()
                if battle_state == "MESSAGE":
                    battle_state = "PLAYER_TURN"
                
                elif battle_state == "PLAYER_TURN":
                    for i, rect in enumerate(move_buttons):
                        if rect.collidepoint(event.pos):
                            hovering_any = True
                            chosen_move = MOVES[player.moves[i]]
                            results = process_battle_round(player, opponent, chosen_move, player_hp, opponent_hp)
                            for turn in results:
                               for msg in turn["messages"]:
                                    battle_queue.append({
                                        "msg": msg,
                                        "p_hp": turn["player_hp_after"],
                                        "o_hp": turn["opponent_hp_after"]
                                    })
                            
                            battle_state = "EXECUTING_MOVE"
                            current_event = battle_queue.pop(0)
                            current_message = current_event["msg"]
                            player_hp = current_event["p_hp"]
                            opponent_hp = current_event["o_hp"]

                elif battle_state == "EXECUTING_MOVE":
                    if battle_queue:
                        current_event = battle_queue.pop(0)
                        current_message = current_event["msg"]
                        player_hp = current_event["p_hp"]
                        opponent_hp = current_event["o_hp"]
                    else:
                        if opponent_hp <= 0:
                            wins += 1
                            if battle == "BOSS":
                                player.gain_level(levels_to_gain)
                                player_hp = player.get_hp()
                                player.stages = {
                    "attack": 0,
                    "defence": 0,
                    "sp_attack": 0,
                    "sp_defence": 0,
                    "speed": 0,
                    "accuracy": 0,
                    "evasion": 0
                }
                                battle = "Normal"
                            else:
                                old_max = player.get_hp() 
                                player.gain_level(levels_to_gain)
                                new_max = player.get_hp() 

                                hp_gained = new_max - old_max
                                heal_amount = int(player.get_hp() * 0.20)
                                player_hp = min(player.get_hp(), player_hp + heal_amount + hp_gained)

                            opponent = get_random_opponent()
                            if wins % 10 == 0:
                                battle = "BOSS"
                                opponent.level = player.level + 2
                                levels_to_gain = 5
                            else:
                                opponent.level = player.level - 2
                                levels_to_gain = 1

                            p_lvl_text = f"{player.level}"
                            player_max_hp = player.get_hp()
                            opponent_hp = opponent.get_hp()
                            opponent_max_hp = opponent_hp
                            display_opponent_hp = opponent_hp
                            opp_img = get_image(opponent.front_img)
                            o_name_text = opponent.name.upper()
                            o_lvl_text = f"{opponent.level}"
                            
                            current_message = f"A wild {opponent.name} appeared!"
                            needs_scaling = True 
                            battle_state = "MESSAGE" 
                        elif player_hp <= 0:
                            battling = False
                        else:
                            battle_state = "PLAYER_TURN"


        if battle_state == "PLAYER_TURN":
            display_text = f"What will {player.name} do?"
            max_text_width = (curr_w // 2) - 60
        else:
            display_text = current_message
            max_text_width = curr_w - 60

        if display_text != last_wrapped_message:
            wrapped_lines = wrap_text(display_text, menu_font, max_text_width)
            last_wrapped_message = display_text


        if battle_state == "PLAYER_TURN":
            draw_dialog_box(screen, menu_font, wrapped_lines, menu_open=True)
            move_buttons = draw_move_menu(screen, menu_font, player.moves)
        else:
            draw_dialog_box(screen, menu_font, wrapped_lines)
            move_buttons = []


        if any(rect.collidepoint(mouse_pos) for rect in move_buttons):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()
if __name__ == "__main__":
    main()