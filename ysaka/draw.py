import pygame
from config import *

def draw_title_screen(screen, font):
    screen.fill(WHITE)
    title = font.render("全国ラーメン図鑑ガチャ", True, BLACK)
    screen.blit(title, (200, 150))
    pygame.draw.rect(screen, GREEN, BUTTON_START)
    start_text = font.render("スタート", True, WHITE)
    screen.blit(start_text, (BUTTON_START.x + 40, BUTTON_START.y + 20))

def draw_gatcha_screen(screen, fonts, ramen_count, last_pulled):
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, BUTTON_GATCHA)
    gatcha_text = fonts[1].render("ガチャを引く！", True, WHITE)
    screen.blit(gatcha_text, (BUTTON_GATCHA.x + 60, BUTTON_GATCHA.y + 30))

    pygame.draw.rect(screen, BLUE, BUTTON_TO_ENCYCLOPEDIA)
    encyclopedia_text = fonts[2].render("図鑑を見る", True, WHITE)
    screen.blit(encyclopedia_text, (BUTTON_TO_ENCYCLOPEDIA.x + 10, BUTTON_TO_ENCYCLOPEDIA.y + 10))

    count_text = fonts[2].render(f"ガチャ回数: {ramen_count}", True, BLACK)
    screen.blit(count_text, (20, 550))

    if last_pulled:
        pulled_text = fonts[1].render(f"出た！ {last_pulled}", True, BLACK)
        screen.blit(pulled_text, (250, 350))

def draw_encyclopedia_screen(screen, fonts, encyclopedia, ramen_data, total_pulls):
    screen.fill(GRAY)
    pygame.draw.rect(screen, GREEN, BUTTON_TO_GATCHA)
    back_text = fonts[2].render("戻る", True, WHITE)
    screen.blit(back_text, (BUTTON_TO_GATCHA.x + 30, BUTTON_TO_GATCHA.y + 10))

    y = 100
    discovered = 0
    for name in ramen_data:
        count, _ = encyclopedia[name]
        if count > 0:
            text = f"{name} - {count}回"
            discovered += 1
        else:
            text = "？？？"
        ramen_text = fonts[2].render(text, True, BLACK)
        screen.blit(ramen_text, (50, y))
        y += 30

    rate = int((discovered / len(ramen_data)) * 100)
    rate_text = fonts[2].render(f"コンプリート率: {rate}%", True, BLACK)
    screen.blit(rate_text, (50, y + 20))

    pulls_text = fonts[2].render(f"ガチャ回数: {total_pulls}", True, BLACK)
    screen.blit(pulls_text, (50, y + 50))
