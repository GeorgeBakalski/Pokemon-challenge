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


def draw_dialog_box(screen, font, text,menu_open=False):
    curr_w, curr_h = screen.get_size()
    
    # Draw the Box (Semi-transparent black rectangle)
    box_height = min(180, curr_h // 4) 
    box_rect = pygame.Rect(0, curr_h - box_height, curr_w, box_height)

    pygame.draw.rect(screen, (255, 255, 255), box_rect)
    pygame.draw.rect(screen, (0, 0, 0), box_rect, 6) 
    inner_rect = box_rect.inflate(-20, -20) 
    pygame.draw.rect(screen, (0, 0, 0), inner_rect, 2)


    if menu_open:
        max_text_width = (curr_w // 2) - 60
    else:
        max_text_width = curr_w - 60
    lines = wrap_text(text, font, max_text_width)

    # Draw each line
    for i, line in enumerate(lines):
         if (i + 1) * font.get_linesize() < box_rect.height - 20:
            text_surf = font.render(line, True, (0, 0, 0))
            line_y = box_rect.y + 20 + (i * font.get_linesize())
            screen.blit(text_surf, (box_rect.x + 20, line_y))

def wrap_text(text, font, max_width):
    """
    Splits a string into a list of lines that fit within max_width.
    """
    words = text.split(' ')
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        if font.size(test_line)[0] <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    
    lines.append(' '.join(current_line))
    return lines

def handle_resize(event, original_bg):
    """
    Handles the window resize event and returns the new screen 
    and the correctly scaled background image.
    """
    new_w, new_h = event.w, event.h
    new_bg = pygame.transform.scale(original_bg, (new_w, new_h))
    return None, new_bg

def draw_move_menu(screen, font, moves):
    curr_w, curr_h = screen.get_size()
    
    box_height = min(180, curr_h // 4)

    menu_width = (curr_w // 2)
    menu_rect = pygame.Rect(curr_w - menu_width, curr_h - box_height, menu_width, box_height)

    pygame.draw.rect(screen, (255, 255, 255), menu_rect)
    pygame.draw.rect(screen, (0, 0, 0), menu_rect, 6)

    move_rects = []
    col_width = menu_rect.width // 2
    row_height = menu_rect.height // 2


    for i in range(min(len(moves), 4)):
        col = i % 2     
        row = i // 2     

        x = menu_rect.x + (col * col_width)
        y = menu_rect.y + (row * row_height)
        
        button_rect = pygame.Rect(x, y, col_width, row_height)
        move_rects.append(button_rect)


        move_name = moves[i]
        text_surf = font.render(move_name.upper(), True, (0, 0, 0))
        text_pos = text_surf.get_rect(center=button_rect.center)
        screen.blit(text_surf, text_pos)

    return move_rects

def get_bottom_offset(surface):
    """
    Finds how many empty pixels are at the bottom of a sprite.
    """
    width, height = surface.get_size()
    for y in range(height - 1, -1, -1):
        for x in range(width):
            if surface.get_at((x, y))[3] > 0: 
                return height - 1 - y
    return 0

def draw_hp_bar(screen, x, y, current_hp, max_hp, scale_factor):
    bar_max_width = 48 * scale_factor
    bar_height = 3 * scale_factor
    shade_height = 1 * scale_factor
    
    # Calculate percentage
    remaining_ratio = current_hp / max_hp
    current_width = int(bar_max_width * remaining_ratio)
    
    # Determine color
    if remaining_ratio > 0.5:
        color = (112, 248, 168)
        color_shade = (88, 208, 128)   
    elif remaining_ratio > 0.2:
        color = (248, 224, 56) 
        color_shade = (200, 168, 8)   
    else:
        color = (248, 88, 56)  
        color_shade = (168, 64, 72) 

    
    pygame.draw.rect(screen, (50, 50, 50), (x, y, bar_max_width, bar_height))
    if current_width > 0:
        pygame.draw.rect(screen, color, (x, y, current_width, bar_height))
        pygame.draw.rect(screen, color_shade, (x, y, current_width, shade_height))
