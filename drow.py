import pygame
import random
import time

# 色定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 150, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)


# 画面設定
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# ボタンの座標とサイズ（汎用化を避け、シンプルな固定値で実装）
BUTTON_GATCHA = pygame.Rect(250, 450, 300, 100)
BUTTON_TO_ENCYCLOPEDIA = pygame.Rect(650, 30, 130, 50)
BUTTON_TO_GATCHA = pygame.Rect(20, 30, 130, 50)

# ラーメンデータ: (出現率, エリア, レア度) ※合計出現率は1.0になるように調整
RAMEN_DATA = {
    '博多ラーメン': (0.30, '九州', 'N'),
    '札幌味噌ラーメン': (0.25, '北海道', 'N'),
    '喜多方ラーメン': (0.15, '東北', 'R'),
    '尾道ラーメン': (0.10, '中国', 'R'),
    '和歌山ラーメン': (0.08, '近畿', 'SR'),
    '家系ラーメン': (0.07, '関東', 'SR'),
    '幻の金のラーメン': (0.05, '全国', 'SSR'),
}
RAMEN_NAMES = list(RAMEN_DATA.keys())
RAMEN_WEIGHTS = [data[0] for data in RAMEN_DATA.values()]

# クッキークリッカー設定
BASE_RAMEN_GAIN_RATE_MS = 1000  # 1000ms（1秒）ごとに1回増加


# ==============================================================================
# 6. 描画関数
# ==============================================================================

def draw_gatcha_screen(screen, font_large, font_medium, font_small, ramen_count, last_pulled_ramen):
    """ガチャ画面の描画"""
    screen.fill((255, 240, 200)) # 背景色（クリーム色）

    # タイトル
    title_text = font_large.render("🍜 ラーメンガチャ！", True, BLACK)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 50))

    # 1. カウント表示 (クッキークリッカー資産)
    count_text = font_medium.render(f"所持ラーメンカウント: {ramen_count}", True, BLUE)
    screen.blit(count_text, (SCREEN_WIDTH // 2 - count_text.get_width() // 2, 120))

    # 2. 最新のガチャ結果表示エリア
    pygame.draw.rect(screen, WHITE, (150, 180, 500, 200), border_radius=10) # 結果枠
    pygame.draw.rect(screen, BLACK, (150, 180, 500, 200), 2, border_radius=10) # 枠線

    if last_pulled_ramen:
        ramen_name = last_pulled_ramen
        data = RAMEN_DATA[ramen_name]

        # レア度に応じた色を設定
        if data[2] == 'SSR':
            color = YELLOW
            rarity_text = "🎉 SSR！幻の！"
        elif data[2] == 'SR':
            color = RED
            rarity_text = "✨ SR！レア！"
        elif data[2] == 'R':
            color = BLUE
            rarity_text = "R"
        else:
            color = BLACK
            rarity_text = "N"

        name_text = font_large.render(ramen_name, True, color)
        info_text = font_medium.render(f"エリア: {data[1]} / レア度: {data[2]}", True, BLACK)

        screen.blit(name_text, (SCREEN_WIDTH // 2 - name_text.get_width() // 2, 230))
        screen.blit(info_text, (SCREEN_WIDTH // 2 - info_text.get_width() // 2, 300))

    else:
        # 初回表示
        msg_text = font_medium.render("ガチャを引いてラーメンを見つけよう！", True, GRAY)
        screen.blit(msg_text, (SCREEN_WIDTH // 2 - msg_text.get_width() // 2, 260))

    # 3. ガチャボタン
    if ramen_count > 0:
        pygame.draw.rect(screen, RED, BUTTON_GATCHA, border_radius=15)
        button_text = font_large.render("ガチャを引く", True, WHITE)
    else:
        pygame.draw.rect(screen, GRAY, BUTTON_GATCHA, border_radius=15)
        button_text = font_large.render("待機中...", True, WHITE)

    screen.blit(button_text, (BUTTON_GATCHA.x + 30, BUTTON_GATCHA.y + 30))

    # 4. 図鑑へボタン
    pygame.draw.rect(screen, GREEN, BUTTON_TO_ENCYCLOPEDIA, border_radius=5)
    ency_text = font_medium.render("図鑑へ", True, WHITE)
    screen.blit(ency_text, (BUTTON_TO_ENCYCLOPEDIA.x + 20, BUTTON_TO_ENCYCLOPEDIA.y + 10))


def draw_encyclopedia_screen(screen, font_large, font_medium, font_small, ramen_count, last_pulled_ramen):
    """図鑑画面の描画"""
    screen.fill((200, 240, 255)) # 背景色（水色）

    # タイトル
    title_text = font_large.render("全国ラーメン図鑑", True, BLACK)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 30))

    # 1. ガチャ画面へボタン
    pygame.draw.rect(screen, GREEN, BUTTON_TO_GATCHA, border_radius=5)
    gatcha_text = font_medium.render("ガチャへ", True, WHITE)
    screen.blit(gatcha_text, (BUTTON_TO_GATCHA.x + 10, BUTTON_TO_GATCHA.y + 10))

    # 2. 図鑑リストの描画
    y_offset = 120
    completed_count = 0
    total_count = len(encyclopedia)

    # ヘッダー
    header_title = font_medium.render("ラーメン名 / エリア", True, BLACK)
    header_count = font_medium.render("獲得回数 / 初回発見", True, BLACK)
    screen.blit(header_title, (50, y_offset - 30))
    screen.blit(header_count, (450, y_offset - 30))


    for name in RAMEN_NAMES: # RAMEN_NAMESの順番で表示
        count, first_time = encyclopedia[name]
        is_acquired = count > 0
        data = RAMEN_DATA[name]

        if is_acquired:
            # ゲット済み
            display_name = f"★ {name} ({data[1]} / {data[2]})"
            text_color = BLACK
            completed_count += 1

            # 発見時間を整形
            time_str = time.strftime("%y/%m/%d %H:%M", time.localtime(first_time))
            count_info = f"{count}杯 / {time_str}"
        else:
            # 未発見
            display_name = "??? (未発見)"
            text_color = GRAY
            count_info = "---"

        # ラーメン名
        ramen_text = font_medium.render(display_name, True, text_color)
        screen.blit(ramen_text, (50, y_offset))

        # 獲得回数
        count_text = font_medium.render(count_info, True, text_color)
        screen.blit(count_text, (450, y_offset))

        y_offset += 40

    # 3. 全国制覇状況の表示
    comp_rate = (completed_count / total_count) * 100 if total_count > 0 else 0
    comp_text = font_large.render(
        f"🏆 全国制覇率: {completed_count}/{total_count} ({comp_rate:.1f}%) 🏆", True, BLUE)
    screen.blit(comp_text, (SCREEN_WIDTH // 2 - comp_text.get_width() // 2, 550))
