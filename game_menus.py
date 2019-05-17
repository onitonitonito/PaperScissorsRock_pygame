import pygame

from pygame.locals import *
from game_settings import *
from game_functions import *

def title_screen(window):
    window.fill(color_pick(HEX_COLOR_BG))
    keys = pygame.mouse.get_pressed()
    display_text(window, "Press the Left Mouse Button", 25, pos=[
                                WINDOW_W // 2, WINDOW_H // 2 + 50])
    if keys[0]:
        return "main_menu"
    else:
        return "title"


def main_menu(window):
    window.fill(color_pick(HEX_COLOR_BG))
    state = "main_menu"
    game = button(
        window, WINDOW_W // 2, WINDOW_H // 2, old_state="main_menu", new_state="game_loop")
    controls = button(
        window, WINDOW_W // 2, WINDOW_H // 2 + 50, old_state="main_menu", new_state="controls")
    button(window, WINDOW_W // 2, WINDOW_H //
                          2 + 100, target=Power_Off)

    multi_line_text(window, 25, 50, color_pick(HEX_WHITE), [WINDOW_W // 2, WINDOW_H // 2], True,
                                   "Play",
                                   "Controls",
                                   "Exit")

    if controls != state:
        return controls
    elif game != state:
        return game
    else:
        return state


def controls(window):
    window.fill(color_pick(HEX_COLOR_BG))
    state = "controls"
    display_text(window, "How to Play", 30, pos=[
                                20, WINDOW_H // 2 - 20], centered=False)
    display_text(window, "Buttons", 30, pos=[
                                WINDOW_W // 1.75, WINDOW_H // 2 - 20], centered=False)
    multi_line_text(window, 15, 15, color_pick(HEX_WHITE), [20, WINDOW_H // 2 + 30], False,
                                   "Click the Left Mouse Button to pick",
                                   "either Paper, Scissors or Rock.",
                                   "<n>",
                                   "Paper beats Rock",
                                   "Rock beats Scissors",
                                   "Scissors beats Paper")
    multi_line_text(window, 15, 25, color_pick(HEX_WHITE), [WINDOW_W // 1.75, WINDOW_H // 2 + 30], False,
                                   "[F1] - Reset the game.",
                                   "[ESC] - Quit the game.",
                                   "[Left Mouse Button] - Click an option.")
    menu = button(
        window, WINDOW_W // 2, WINDOW_H - 80, old_state="controls", new_state="main_menu")
    display_text(window, "Menu", 25, pos=[
                                WINDOW_W // 2, WINDOW_H - 80])

    if menu != state:
        return menu
    else:
        return state
