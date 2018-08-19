import pygame
import game_functions

from pygame.locals import *
from game_settings import *


def Title_Screen(window):
    window.fill([170, 170, 255])
    keys = pygame.mouse.get_pressed()
    game_functions.Display_Text(window, "Press the Left Mouse Button", 25, pos=[
                                WINDOW_W // 2, WINDOW_H // 2 + 50])
    if keys[0]:
        return "main_menu"
    else:
        return "title"


def Main_Menu(window):
    window.fill([170, 170, 255])
    state = "main_menu"
    game = game_functions.Button(
        window, WINDOW_W // 2, WINDOW_H // 2, old_state="main_menu", new_state="game_loop")
    controls = game_functions.Button(
        window, WINDOW_W // 2, WINDOW_H // 2 + 50, old_state="main_menu", new_state="controls")
    game_functions.Button(window, WINDOW_W // 2, WINDOW_H //
                          2 + 100, target=game_functions.Power_Off)

    game_functions.multi_line_text(window, 25, 50, WHITE, [WINDOW_W // 2, WINDOW_H // 2], True,
                                   "Play",
                                   "Controls",
                                   "Exit")

    if controls != state:
        return controls
    elif game != state:
        return game
    else:
        return state


def Controls(window):
    window.fill([170, 170, 255])
    state = "controls"
    game_functions.Display_Text(window, "How to Play", 30, pos=[
                                20, WINDOW_H // 2 - 20], centered=False)
    game_functions.Display_Text(window, "Buttons", 30, pos=[
                                WINDOW_W // 1.75, WINDOW_H // 2 - 20], centered=False)
    game_functions.multi_line_text(window, 15, 15, WHITE, [20, WINDOW_H // 2 + 30], False,
                                   "Click the Left Mouse Button to pick",
                                   "either Paper, Scissors or Rock.",
                                   "<n>",
                                   "Paper beats Rock",
                                   "Rock beats Scissors",
                                   "Scissors beats Paper")
    game_functions.multi_line_text(window, 15, 25, WHITE, [WINDOW_W // 1.75, WINDOW_H // 2 + 30], False,
                                   "[F1] - Reset the game.",
                                   "[ESC] - Quit the game.",
                                   "[Left Mouse Button] - Click an option.")
    menu = game_functions.Button(
        window, WINDOW_W // 2, WINDOW_H - 80, old_state="controls", new_state="main_menu")
    game_functions.Display_Text(window, "Menu", 25, pos=[
                                WINDOW_W // 2, WINDOW_H - 80])

    if menu != state:
        return menu
    else:
        return state
