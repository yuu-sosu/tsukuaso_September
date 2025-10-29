import pygame
from config import *
from draw import draw_title_screen, draw_gatcha_screen, draw_encyclopedia_screen
from logic import handle_events

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("全国ラーメン図鑑ガチャ")
clock = pygame.time.Clock()

# フォント
font_large = pygame.font.Font(None, 48)
font_medium = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 24)
fonts = [font_large, font_medium, font_small]

# 状態変数
state = STATE_TITLE
ramen_count = 0
last_pulled = None
encyclopedia = {name: (0, 0) for name in RAMEN_DATA}
running = True

while running:
    for event in pygame.event.get():
        running, state, ramen_count, last_pulled = handle_events(event, state, ramen_count, encyclopedia, last_pulled)

    if state == STATE_TITLE:
        draw_title_screen(screen, font_large)
    elif state == STATE_GATCHA:
        draw_gatcha_screen(screen, fonts, ramen_count, last_pulled)
    elif state == STATE_ENCYCLOPEDIA:
        draw_encyclopedia_screen(screen, fonts, encyclopedia, RAMEN_DATA, ramen_count)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
