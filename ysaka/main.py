import pygame
import pygame.freetype  # ← 追加
import os
from config import *
from draw import draw_title_screen, draw_gatcha_screen, draw_encyclopedia_screen
from logic import handle_events

pygame.init()
pygame.freetype.init()  # ← 追加

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("全国ラーメン図鑑ガチャ")
clock = pygame.time.Clock()
background_image = pygame.image.load("assets/images/cover.png").convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# フォント（日本語対応）
font_path = os.path.join("assets", "fonts", "NotoSansCJKjp-Regular.otf")
font_large = pygame.freetype.Font(FONT_PATH, 48)
font_medium = pygame.freetype.Font(FONT_PATH, 36)
font_small = pygame.freetype.Font(FONT_PATH, 24)
fonts = [font_large, font_medium, font_small]

# 状態変数
state = STATE_TITLE
ramen_count = 0
last_pulled = None
encyclopedia = {name: (0, 0) for name in RAMEN_DATA}
running = True
ramen_images = {
    name: pygame.image.load(info['image']).convert_alpha()
    for name, info in RAMEN_DATA.items()
}

while running:
    for event in pygame.event.get():
        running, state, ramen_count, last_pulled = handle_events(event, state, ramen_count, encyclopedia, last_pulled)

    if state == STATE_TITLE:
        draw_title_screen(screen, font_medium, background_image)
    elif state == STATE_GATCHA:
        draw_gatcha_screen(screen, fonts, ramen_count, last_pulled, ramen_images)
    elif state == STATE_ENCYCLOPEDIA:
        draw_encyclopedia_screen(screen, fonts, encyclopedia, RAMEN_DATA, ramen_count)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
