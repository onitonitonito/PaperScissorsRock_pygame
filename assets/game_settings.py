from os import getlogin
from random import choice

# -- Game Info --
GAME_NAME = "Paper, Scissors, Rock"
GAME_VERSION = 2.0
AUTHOR = "Joshua Harvey"
GAME_DATE = "02/08/2018"
VERSION_DATE = {"begin": "03/08/2018",
                "finish": "06/08/2018"}

# -- Game Variables --
WINDOW_W = 700
WINDOW_H = 500
FRAMES = 140
SCRIPT_DELAY = 40

# -- Colours --
HEX_BLACK = '#000000'
HEX_WHITE = '#ffffff'

HEX_RED = '#ff0000'
HEX_GREEN = '#00c800'
HEX_BLUE = '#0000ff'

HEX_COLOR_BG = '#aabbff'
HEX_COLOR_ONMOUSE = '#ccddff'

# -- Logic --
try:
    USER_NAME = getlogin()
except:
    USER_NAME = "Player"

SPLASH_TEXT_CHOICES = [f"Welcome, {USER_NAME}!",
                       f"Hello, {USER_NAME}!",
                       f"It's-a me, {USER_NAME}!",
                       f"{USER_NAME}, do a barrel roll!",
                       f"Kept you waiting, huh?",
                       f"Made with Python 3 and Pygame!",
                       f"Version {int(GAME_VERSION)}!",
                       f"{GAME_NAME}, Chuck Norris!"
                       ]

SPLASH_TEXT = choice(SPLASH_TEXT_CHOICES)
