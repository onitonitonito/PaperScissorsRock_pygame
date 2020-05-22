"""
# RockScissorsPaper from Pygame.org
# http://pygame.org/examples
#
"""
# Best example structure to learn how to consist a structure
#  - some modifications are applied to original.
print(__doc__)

import pygame
from pygame.locals import *

from assets.game_menus import *
from assets.game_settings import *
from assets.game_functions import *

from bot import Bot
from assets.game_assets import (
                            IMG_ICON,
                            IMG_BOT,
                            IMG_BOT_LOSE,
                            IMG_BOT_WIN,
                            IMG_HUM.
                        )

decision_made = False
choice_player = False
choice_bot = False
Wins = 0
Losses = 0
Draws = 0
Combo = 0
game_done = False
winner = None

bot = Bot()

def main():
    pygame.init()
    pygame.display.set_icon(IMG_ICON)

    window = pygame.display.set_mode([WINDOW_W,WINDOW_H])
    window.fill(color_pick(HEX_COLOR_BG))
    pygame.display.update()

    FPS = pygame.time.Clock()


    global choice_player
    global choice_bot
    global decision_made
    global game_done
    global winner
    global Wins
    global Losses
    global Draws
    global Combo

    winner = None
    decision_made = choice_player = choice_bot = game_done = False
    Wins = Losses = Draws = Combos = 0

    increase_text = True
    text_size = 10

    state = "title"

    while True:
        event_handler()

        if state == "title":
            pygame.display.set_caption(GAME_NAME + " | Title Screen")
            state = title_screen(window)

        elif state == "main_menu":
            pygame.display.set_caption(GAME_NAME + " | Main Menu")
            state = main_menu(window)


        elif state == "controls":
            pygame.display.set_caption(GAME_NAME + " | Controls")
            state = controls(window)

        elif state == "game_loop":
            pygame.display.set_caption(GAME_NAME + " | {0} {1} - {2} BOT | Combo x{3} | Draws {4}".format(USER_NAME.upper(), Wins, Losses, Combo, Draws))
            state = game_loop(window)

        if state in ["title", "main_menu", "controls"]:
            if state != "controls":
                if text_size == 17:
                    increase_text = False

                elif text_size == 10:
                    increase_text = True

                if increase_text == True:
                    text_size += 1

                else:
                    text_size -= 1

                display_text(window, SPLASH_TEXT, text_size,color_pick(HEX_WHITE), [WINDOW_W//2, 140])

            display_text(window, GAME_NAME, 55, pos=[WINDOW_W//2, 100])
            display_text(window, "version {0} - by {1} - 2018".format(GAME_VERSION, AUTHOR), 15, [200,200,255], [10, WINDOW_H -23], False)

        pygame.time.delay(SCRIPT_DELAY)
        pygame.display.update()
        FPS.tick(FRAMES)

def game_loop(window):
    window.fill(color_pick(HEX_COLOR_BG))

    state = "game_loop"

    global decision_made
    global choice_player
    global choice_bot
    global bot

    display_text(window, USER_NAME, 40, pos=[WINDOW_W //4, WINDOW_H//8])
    display_text(window, "Computer", 40, pos=[WINDOW_W - WINDOW_W //4, WINDOW_H//8])

    window.blit(IMG_HUM, [WINDOW_W //4 - 75, WINDOW_H//5])
    window.blit(IMG_BOT, [WINDOW_W - WINDOW_W //4 - 75, WINDOW_H//5])

    if decision_made == False:

        choice_player = [
            button(window, WINDOW_W //5, WINDOW_H - 170, option=True),
            button(window, WINDOW_W //2, WINDOW_H - 170, option=True),
            button(window, WINDOW_W - WINDOW_W //5, WINDOW_H - 170, option=True)]

        display_text(window, "Rock", 25, pos=[WINDOW_W //5, WINDOW_H - 170])
        display_text(window, "Paper", 25, pos=[WINDOW_W //2, WINDOW_H - 170])
        display_text(window, "Scissors", 25, pos=[WINDOW_W - WINDOW_W //5, WINDOW_H - 170])

        if True in choice_player:

            decision_made = True

            if choice_player[0] == True:
                choice_player = "rock"

            elif choice_player[1] == True:
                choice_player = "paper"

            elif choice_player[2] == True:
                choice_player = "scissors"

            bot.player_thrown.append(choice_player)
            choice_bot = bot.throw_hand()

    if decision_made == True:
        state = result_screen(window)

    return state

def result_screen(window):
    global choice_player
    global choice_bot
    global Wins
    global Losses
    global Combo
    global Draws
    global game_done
    global winner

    if game_done != True:
        if choice_player != choice_bot:
            if choice_player == "scissors":
                if choice_bot == "paper":
                    Wins += 1
                    Combo += 1
                    winner = "player"

                else:
                    Losses += 1
                    Combo = 0
                    winner = "com"

            elif choice_player == "paper":
                if choice_bot == "rock":
                    Wins += 1
                    Combo += 1
                    winner = "player"

                else:
                    Losses += 1
                    Combo = 0
                    winner = "com"

            elif choice_player == "rock":
                if choice_bot == "scissors":
                    Wins += 1
                    Combo += 1
                    winner = "player"

                else:
                    Losses += 1
                    Combo = 0
                    winner = "com"

            game_done = True

        if choice_player == choice_bot:
            Combo = 0
            Draws += 1
            game_done = True

    display_text(window, "Wins {0}".format(Wins), 20, pos=[WINDOW_W //4, WINDOW_H//15])
    display_text(window, "Wins {0}".format(Losses), 20, pos=[WINDOW_W - WINDOW_W //4, WINDOW_H//15])

    if Combo > 1:
        display_text(window, "x{0}".format(Combo), 20, color=[255,255,0],pos=[WINDOW_W //4 + 60, WINDOW_H//5 + 175])

    if winner == "player":
        display_text(window, "Won!", 30, color=color_pick(HEX_GREEN), pos=[WINDOW_W //4, WINDOW_H//5 + 175])
        display_text(window, "Lost!", 30, color=color_pick(HEX_RED), pos=[WINDOW_W - WINDOW_W //4, WINDOW_H//5 + 175])
        window.blit(IMG_BOT_LOSE, [WINDOW_W - WINDOW_W //4 - 41, WINDOW_H//5 + 41])

    elif winner == "com":
        display_text(window, "Lost!", 30, color=color_pick(HEX_RED), pos=[WINDOW_W //4, WINDOW_H//5 + 175])
        display_text(window, "Won!", 30, color=color_pick(HEX_GREEN), pos=[WINDOW_W - WINDOW_W //4, WINDOW_H//5 + 175])
        window.blit(IMG_BOT_WIN, [WINDOW_W - WINDOW_W //4 - 41, WINDOW_H//5 + 41])

    else:
        display_text(window, "Draw", 30, pos=[WINDOW_W //2, WINDOW_H//5 + 175])

    display_text(window, choice_player, 20, pos=[WINDOW_W //4, WINDOW_H//8 + 25])
    display_text(window, choice_bot, 20, pos=[WINDOW_W - WINDOW_W //4, WINDOW_H//8 +25])

    button(window, WINDOW_W //3, WINDOW_H - 120, target=reset_game)

    exit = button(window, WINDOW_W - WINDOW_W //3, WINDOW_H - 120, target=reset_game, args=True)

    display_text(window, "Play Again", 25, pos=[WINDOW_W //3, WINDOW_H - 120])
    display_text(window, "Main Menu", 25, pos=[WINDOW_W - WINDOW_W //3, WINDOW_H - 120])



    if exit == True:
        window.fill(color_pick(HEX_COLOR_BG))
        return "main_menu"

    else:
        return "game_loop"

def reset_game(change_state=False):
    global decision_made
    global choice_player
    global choice_bot
    global game_done
    global winner

    game_done = False
    winner = None
    choice_player = False
    choice_bot = False
    decision_made = False

    if change_state == True:
        return True

    else:
        return False


if __name__ == '__main__':
    main()
    pass
