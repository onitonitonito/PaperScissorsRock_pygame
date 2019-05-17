import pygame
import app

from pygame.locals import *
from game_settings import *
from game_assets import SFX_BEEP, TXT_MAIN


pygame.mixer.init()


def color_pick(hex_code_with_sharp):
    """ turn '#aabbff' into color int array [170, 187, 255]
    Convert HEX string 'aa' to INTEGER --> int('aa', base=16)
    """
    rgb_array_int = []
    for i in [1, 3, 5]:
        hex_to_int = int(hex_code_with_sharp[i:i+2], base=16)
        rgb_array_int.append(hex_to_int)

    return rgb_array_int


def event_handler():
    """ for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Power_Off()
            elif event.type == pygame.KEYUP:
                if event.key == K_ESCAPE:
                    Power_Off()
                elif event.key == K_F1:
                    Power_Off(True)
    """
    for event in pygame.event.get():
        event_dict = {
            'quit': [(event.type == QUIT),
                     (event.type == KEYUP and event.key == K_ESCAPE),],
            'F1': [(event.type == KEYUP and event.key == K_F1),],
            '1': [(event.type == KEYUP and event.key == K_1),],
            '2': [(event.type == KEYUP and event.key == K_2),],
            '3': [(event.type == KEYUP and event.key == K_3),],
        }

        if any(event_dict['quit']): Power_Off()
        if any(event_dict['F1']): Power_Off(True)
        if any(event_dict['1']): pass
        if any(event_dict['2']): pass
        if any(event_dict['3']): Power_Off()


def display_text(surface, text, size=20, color=color_pick(HEX_WHITE), pos=[0, 0], centered=True):
    font = pygame.font.Font(TXT_MAIN, size)
    text_obj = font.render(text, True, color).convert_alpha()
    width, height = text_obj.get_size()

    if centered == True:
        pos[0] -= width // 2
        pos[1] -= height // 2

    surface.blit(text_obj, pos)


def button(surface,  x, y, target=False, old_state="title", new_state=False, option=False, args=None):
    pos = pygame.mouse.get_pos()
    keys = pygame.mouse.get_pressed()

    w, h = 200, 35
    x, y = x, y

    rect = pygame.surface.Surface([w, h])
    rect.convert()
    selected = False

    if pos[0] > x - w // 2 and pos[0] < x - w // 2 + w and pos[1] > y - h // 2 and pos[1] < y - h // 2 + h:
        selected = True
        rect.fill(color_pick(HEX_COLOR_ONMOUSE))
        surface.blit(rect, [x - w // 2, y - h // 2])

    else:
        selected = False
        rect.fill(color_pick(HEX_COLOR_BG))
        surface.blit(rect, [x - w // 2, y - h // 2])

    if selected == True:
        if new_state != False:
            if keys[0]:
                SFX_BEEP.play()
                return new_state
            else:
                return old_state

        elif target != False:
            if keys[0]:
                SFX_BEEP.play()
                if args != None:
                    return target(args)
                else:
                    return target()

        elif option != False:
            if keys[0]:
                SFX_BEEP.play()
                return True
            else:
                return False

    else:
        if new_state != False:
            return old_state

        elif option != False:
            return False


def multi_line_text(surface, size=20, spacing=20, color=color_pick(HEX_WHITE), pos=[0, 0], centered=True, *text):
    next_line = 0

    for i in text:
        if i == "<n>":
            next_line += spacing
        else:
            display_text(surface, i, size, color, [
                         pos[0], pos[1] + next_line], centered)
            next_line += spacing


def Power_Off(reset=False):
    if reset == True:
        pygame.quit()
        app.main()

    else:
        pygame.quit()
        raise SystemExit
