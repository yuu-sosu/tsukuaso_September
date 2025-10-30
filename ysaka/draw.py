import pygame
from config import *
from game_logic import get_remaining_time  # ← タイマー用関数をインポート！


def draw_title_screen(screen, font, background_image):
    screen.blit(background_image, (0, 0))
    pygame.draw.rect(screen, GREEN, BUTTON_START)
    font.render_to(screen, (BUTTON_START.x + 10, BUTTON_START.y + 10), "スタート", WHITE)


def draw_timer(screen, font):
    """左上に残り時間を表示"""
    remaining = get_remaining_time()
    text = f"残り時間: {remaining} 秒"
    # 👇 引数の順番とカッコを修正
    font.render_to(screen, (20, 20), text, RED)


def draw_gatcha_screen(screen, fonts, ramen_count, last_pulled, ramen_images):
    # 背景画像の描画
    background = pygame.image.load("assets/images/second_background.png")  # 背景画像の読み込み
    background = pygame.transform.scale(background, screen.get_size())    # 画面サイズに合わせる
    screen.blit(background, (0, 0))                                       # 背景を描画

    # タイマー表示
    draw_timer(screen, fonts[2])

    # ガチャボタン
    pygame.draw.rect(screen, RED, BUTTON_GATCHA)
    fonts[1].render_to(screen, (BUTTON_GATCHA.x + 30, BUTTON_GATCHA.y + 30), "ガチャを引く！", WHITE)

    # 図鑑ボタン
    pygame.draw.rect(screen, BLUE, BUTTON_TO_ENCYCLOPEDIA)
    fonts[2].render_to(screen, (BUTTON_TO_ENCYCLOPEDIA.x + 10, BUTTON_TO_ENCYCLOPEDIA.y + 10), "図鑑を見る", WHITE)

    # ガチャ回数表示
    fonts[2].render_to(screen, (20, 550), f"ガチャ回数: {ramen_count}", BLACK)

    # 直近で引いたラーメンの表示
    if last_pulled:
        rarity_colors = {
            "SSR": (255, 215, 0),    # 金色
            "SR":  (186, 85, 211),   # 紫
            "R":   (30, 144, 255),   # 青
            "N":   (169, 169, 169),  # グレー
        }

        ramen_info = RAMEN_DATA.get(last_pulled, {})
        rarity = ramen_info.get("rarity", "N")
        color = rarity_colors.get(rarity, (0, 0, 0))

        # 名前表示
        fonts[1].render_to(screen, (250, 300), f"出た！ {last_pulled}", color)

        # 画像表示
        image = ramen_images.get(last_pulled)
        if image:
            scaled_image = pygame.transform.scale(image, (250, 250))
            screen.blit(scaled_image, (275, 50))


def draw_encyclopedia_screen(screen, fonts, encyclopedia, ramen_data, total_pulls):
    # 背景画像を描画
    background = pygame.image.load("assets/images/encyclopedia_bg.png")
    background = pygame.transform.scale(background, screen.get_size())
    screen.blit(background, (0, 0))


    # 戻るボタン
    pygame.draw.rect(screen, GREEN, BUTTON_TO_GATCHA)
    fonts[2].render_to(screen, (BUTTON_TO_GATCHA.x + 30, BUTTON_TO_GATCHA.y + 10), "戻る", WHITE)

    rarity_colors = {
        'N': BLACK,
        'R': BLUE,
        'SR': GREEN,
        'SSR': YELLOW
    }

    y = 100
    discovered = 0
    for name in ramen_data:
        count, _ = encyclopedia[name]
        if count > 0:
            rarity = ramen_data[name]['rarity']
            text = f"{name} - {count}回 [{rarity}]"
            color = rarity_colors.get(rarity, BLACK)
            fonts[2].render_to(screen, (50, y), text, color)
            discovered += 1
        else:
            fonts[2].render_to(screen, (50, y), "？？？", BLACK)
        y += 30

    rate = int((discovered / len(ramen_data)) * 100)
    fonts[2].render_to(screen, (50, y + 20), f"コンプリート率: {rate}%", BLACK)
    fonts[2].render_to(screen, (50, y + 50), f"ガチャ回数: {total_pulls}", BLACK)
