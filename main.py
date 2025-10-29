
import pygame
import random
import time

from drow import draw_gatcha_screen
from drow import draw_encyclopedia_screen
from logic import pull_gatcha
from logic import update_clicker_logic
from logic import handle_gatcha_events
from logic import handle_encyclopedia_events

# ==============================================================================
# 1. 定数と設定
# ==============================================================================

# 画面設定
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# ゲームの状態
STATE_GATCHA = 1
STATE_ENCYCLOPEDIA = 2

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
# 2. Pygame初期化
# ==============================================================================
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("全国ラーメン図鑑コンプリート")
clock = pygame.time.Clock()
font_large = pygame.font.Font(None, 48)
font_medium = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 24)

# ==============================================================================
# 3. ゲームの状態管理変数
# ==============================================================================
current_state = STATE_GATCHA  # 初期状態はガチャ画面
ramen_count = 5  # 初期ガチャ回数 (クッキークリッカーの資産)
last_pulled_ramen = None  # 最新のガチャ結果
LAST_TICK_TIME = pygame.time.get_ticks() # 自動増加のための最終更新時間

# 図鑑データ: {'ラーメン名': (入手済み回数, 初回入手時間)}
encyclopedia = {name: (0, 0) for name in RAMEN_DATA.keys()}

# ==============================================================================
# 7. メインループ
# ==============================================================================
running = True
while running:
    # 1. イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # マウスイベントを現在の状態に合わせて処理
        if current_state == STATE_GATCHA:
            handle_gatcha_events(event, ramen_count)
        elif current_state == STATE_ENCYCLOPEDIA:
            handle_encyclopedia_events(event)

    # 2. ロジック更新 (クッキークリッカー要素)
    update_clicker_logic(BASE_RAMEN_GAIN_RATE_MS, LAST_TICK_TIME, ramen_count)

    # 3. 描画処理
    if current_state == STATE_GATCHA:
        draw_gatcha_screen(screen, font_large, font_medium, font_small, ramen_count, last_pulled_ramen)
    elif current_state == STATE_ENCYCLOPEDIA:
        draw_encyclopedia_screen(srceen, font_large, font_medium, font_small, ramen_count, last_pulled_ramen)

    # 4. 画面更新とフレームレート設定
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
