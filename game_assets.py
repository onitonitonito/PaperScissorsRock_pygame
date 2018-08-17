import pygame

SFX_PATH = "assets/sound/"
IMG_PATH = "assets/image/"
ETC_PATH = "assets/etc/"

pygame.mixer.init()
pygame.display.init()

#images
IMG_HUM = pygame.image.load(IMG_PATH + "human.png")
IMG_BOT = pygame.image.load(IMG_PATH + "bot.png")
IMG_BOTLOSE = pygame.image.load(IMG_PATH + "bot_lose.png")
IMG_BOTWIN = pygame.image.load(IMG_PATH + "bot_win.png")
IMG_ICON = pygame.image.load(IMG_PATH + "icon.png")

#sounds
SFX_BEEP = pygame.mixer.Sound(SFX_PATH + "menu_beep.wav")

#other
TXT_MAIN = ETC_PATH + "Comfortaa-Regular.ttf"