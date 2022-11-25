import pygame, characters

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

FONT = pygame.font.SysFont('consolas', 20)

SCREEN = pygame.display.set_mode(
    (SCREEN_WIDTH,SCREEN_HEIGHT)
)

CLOCK = pygame.time.Clock()

pygame.display.set_caption('Property Game')
ICON = pygame.Surface((1,1))
pygame.display.set_icon(ICON)

JOHN = characters.playable_character()


WHITE = (255,255,255)
DARK_GRAY = (50,50,50)
GRAY = (100,100,100)
BLACK = (0,0,0)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)

ORANGE = (255,128,0)
