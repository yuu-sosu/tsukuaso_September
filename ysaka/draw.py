import pygame
from config import *

def draw_title_screen(screen, font):
    screen.fill(WHITE)
    font.render_to(screen, (200, 150), "全国ラーメン図鑑ガチャ", BLACK)
    pygame.draw.rect(screen, GREEN, BUTTON_START)
    font.render_to(screen, (BUTTON_START.x + 40, BUTTON_START.y + 20), "スタート", WHITE)

def draw_gatcha_screen(screen, fonts, ramen_count, last_pulled, ramen_images):
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, BUTTON_GATCHA)
    fonts[1].render_to(screen, (BUTTON_GATCHA.x + 60, BUTTON_GATCHA.y + 30), "ガチャを引く！", WHITE)

    pygame.draw.rect(screen, BLUE, BUTTON_TO_ENCYCLOPEDIA)
    fonts[2].render_to(screen, (BUTTON_TO_ENCYCLOPEDIA.x + 10, BUTTON_TO_ENCYCLOPEDIA.y + 10), "図鑑を見る", WHITE)

    fonts[2].render_to(screen, (20, 550), f"ガチャ回数: {ramen_count}", BLACK)

    if last_pulled:
        fonts[1].render_to(screen, (250, 300), f"出た！ {last_pulled}", BLACK)
        image = ramen_images.get(last_pulled)
        if image:
            # 1. 調整したいサイズを (幅, 高さ) で指定します
            NEW_WIDTH = 250
            NEW_HEIGHT = 250
            
            # 2. 画像を新しいサイズに変換 (scaled_image が新しいSurface)
            scaled_image = pygame.transform.scale(image, (NEW_WIDTH, NEW_HEIGHT))
            
            screen.blit(scaled_image,(250, 50))  # 画像の表示位置を調整

def draw_encyclopedia_screen(screen, fonts, encyclopedia, ramen_data, total_pulls):
    screen.fill(GRAY)
    pygame.draw.rect(screen, GREEN, BUTTON_TO_GATCHA)
    fonts[2].render_to(screen, (BUTTON_TO_GATCHA.x + 30, BUTTON_TO_GATCHA.y + 10), "戻る", WHITE)

    y = 100
    discovered = 0
    for name in ramen_data:
        count, _ = encyclopedia[name]
        if count > 0:
            text = f"{name} - {count}回"
            discovered += 1
        else:
            text = "？？？"
        fonts[2].render_to(screen, (50, y), text, BLACK)
        y += 30

    rate = int((discovered / len(ramen_data)) * 100)
    fonts[2].render_to(screen, (50, y + 20), f"コンプリート率: {rate}%", BLACK)
    fonts[2].render_to(screen, (50, y + 50), f"ガチャ回数: {total_pulls}", BLACK)
