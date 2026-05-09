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


def draw_dialog_box(screen, font, text):
    curr_w, curr_h = screen.get_size()
    
    # Draw the Box (Semi-transparent black rectangle)
    box_height = min(180, curr_h // 4) 
    margin = 20
    box_rect = pygame.Rect(margin, curr_h - box_height - margin, curr_w - (margin * 2), box_height)

    pygame.draw.rect(screen, (255, 255, 255), box_rect)
    pygame.draw.rect(screen, (0, 0, 0), box_rect, 6) 
    inner_rect = box_rect.inflate(-20, -20) 
    pygame.draw.rect(screen, (0, 0, 0), inner_rect, 2)


    # Wrap the text so it doesn't leak out
    max_text_width = box_rect.width - 40
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