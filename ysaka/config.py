import pygame

# 画面設定
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# 色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 150, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# 状態定義
STATE_TITLE = 0
STATE_GATCHA = 1
STATE_ENCYCLOPEDIA = 2

# ボタン定義
BUTTON_START = pygame.Rect(300, 300, 200, 80)
BUTTON_GATCHA = pygame.Rect(250, 450, 300, 100)
BUTTON_TO_ENCYCLOPEDIA = pygame.Rect(650, 30, 130, 50)
BUTTON_TO_GATCHA = pygame.Rect(20, 30, 130, 50)

# ラーメンデータ
RAMEN_DATA = {
    '博多ラーメン': (0.30, '九州', 'N'),
    '札幌味噌ラーメン': (0.25, '北海道', 'N'),
    '喜多方ラーメン': (0.15, '東北', 'R'),
    '尾道ラーメン': (0.10, '中国', 'R'),
    '和歌山ラーメン': (0.08, '近畿', 'SR'),
    '家系ラーメン': (0.07, '関東', 'SR'),
    '幻の金のラーメン': (0.05, '全国', 'SSR'),
}
