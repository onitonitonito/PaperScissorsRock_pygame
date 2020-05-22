import pygame

SFX_PATH = "static/sound/"
IMG_PATH = "static/image/"
ETC_PATH = "static/etc/"

pygame.mixer.init()
pygame.display.init()

# images
IMG_HUM = pygame.image.load(IMG_PATH + "human.png")
IMG_HUM_WIN = pygame.image.load(IMG_PATH + "human.png")
IMG_HUM_LOSE = pygame.image.load(IMG_PATH + "human.png")



IMG_BOT = pygame.image.load(IMG_PATH + "bot.png")
IMG_BOT_WIN = pygame.image.load(IMG_PATH + "bot_win.png")
IMG_BOT_LOSE = pygame.image.load(IMG_PATH + "bot_lose.png")

IMG_ICON = pygame.image.load(IMG_PATH + "icon.png")

# sounds
SFX_BEEP = pygame.mixer.Sound(SFX_PATH + "menu_beep.wav")

# other
TXT_MAIN = ETC_PATH + "Comfortaa-Regular.ttf"
