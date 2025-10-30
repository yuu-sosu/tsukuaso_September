import os
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

# 制限時間（秒）
GAME_TIME_LIMIT = 180  # 3分

# ボタン定義
BUTTON_START = pygame.Rect(630, 500, 150, 60)
BUTTON_GATCHA = pygame.Rect(250, 450, 300, 100)
BUTTON_TO_ENCYCLOPEDIA = pygame.Rect(650, 30, 130, 50)
BUTTON_TO_GATCHA = pygame.Rect(20, 30, 130, 50)

# ラーメンデータ
RAMEN_DATA = {
    '豚骨': {
        'weight': 0.20,
        'region': '全国',
        'rarity': 'N',
        'image': 'assets/images/tonkotsu.png'
    },
    '醤油': {
        'weight': 0.20,
        'region': '全国',
        'rarity': 'N',
        'image': 'assets/images/syouyu.png'
    },
    'つけ麺': {
        'weight': 0.15,
        'region': '全国',
        'rarity': 'R',
        'image': 'assets/images/tukemen.png'
    },
    '油そば': {
        'weight': 0.15,
        'region': '全国',
        'rarity': 'R',
        'image': 'assets/images/abura.png'
    },
    '札幌ラーメン': {
        'weight': 0.10,
        'region': '北海道',
        'rarity': 'SR',
        'image': 'assets/images/sapporo.png'
    },
    '熊本ラーメン': {
        'weight': 0.10,
        'region': '九州',
        'rarity': 'SR',
        'image': 'assets/images/kumamoto.png'
    },
    '家系': {
        'weight': 0.099,
        'region': '関東',
        'rarity': 'SR',
        'image': 'assets/images/ie.png'
    },
    '次郎系': {
        'weight': 0.001,
        'region': '全国',
        'rarity': 'SSR',
        'image': 'assets/images/ziro.png'
    },
}


FONT_PATH = os.path.join("assets", "fonts", "NotoSansCJKjp-Regular.otf")
