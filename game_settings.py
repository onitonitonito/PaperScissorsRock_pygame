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
BLACK = [0,0,0]
WHITE = [255,255,255]
RED = [255,0,0]
GREEN = [0,200,0]
BLUE = [0,0,255]

# -- Logic --
try:
    USER_NAME = getlogin()
except:
    USER_NAME = "Player"

SPLASH_TEXT_CHOICES = ["Welcome, {}!".format(USER_NAME),
                       "Hello, {}!".format(USER_NAME),
                       "It's-a me, {}!".format(USER_NAME),
                       "{}, do a barrel roll!".format(USER_NAME),
                       "Kept you waiting, huh?",
                       "Made with Python 3 and Pygame!",
                       "Version {}!".format(int(GAME_VERSION)),
                       "{}, Chuck Norris!".format(GAME_NAME)]

SPLASH_TEXT = choice(SPLASH_TEXT_CHOICES)
