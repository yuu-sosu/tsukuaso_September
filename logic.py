import pygame
import random
import time

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

# ==============================================================================
# 4. ロジック関数 (ガチャ / クリッカー)
# ==============================================================================

def pull_gatcha(ramen_count):
    """ガチャを1回引き、結果を返して図鑑を更新する"""

    if ramen_count <= 0:
        return None # ガチャ回数がなければ引けない

    ramen_count -= 1 # ガチャ回数を消費

    # random.choicesで重み付きランダム選択
    result_ramen = random.choices(RAMEN_NAMES, weights=RAMEN_WEIGHTS, k=1)[0]

    # 図鑑を更新
    count, first_time = encyclopedia[result_ramen]
    current_time = int(time.time())

    # 初回ゲットなら時間を記録
    if count == 0:
        encyclopedia[result_ramen] = (count + 1, current_time)
    else:
        encyclopedia[result_ramen] = (count + 1, first_time)

    last_pulled_ramen = result_ramen
    return result_ramen

def update_clicker_logic(gain_rate_ms, LAST_TICK_TIME, ramen_count):
    """時間経過でガチャ回数を自動増加させる"""

    current_time = pygame.time.get_ticks()

    # 経過した時間に基づいて増加回数を計算
    time_elapsed = current_time - LAST_TICK_TIME
    gains = time_elapsed // gain_rate_ms

    if gains >= 1:
        ramen_count += gains
        # 増加した分だけ時間を進める（小数点以下の誤差を減らすため）
        LAST_TICK_TIME += gains * gain_rate_ms

# ==============================================================================
# 5. イベントハンドラ関数
# ==============================================================================

def handle_gatcha_events(event, ramen_count):
    """ガチャ画面でのイベント処理"""

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos

        # ガチャボタンのクリック判定
        if BUTTON_GATCHA.collidepoint(mouse_pos):
            pull_gatcha(ramen_count)

        # 図鑑へボタンのクリック判定
        if BUTTON_TO_ENCYCLOPEDIA.collidepoint(mouse_pos):
            current_state = STATE_ENCYCLOPEDIA

def handle_encyclopedia_events(event):
    """図鑑画面でのイベント処理"""

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos

        # ガチャへボタンのクリック判定
        if BUTTON_TO_GATCHA.collidepoint(mouse_pos):
            current_state = STATE_GATCHA
