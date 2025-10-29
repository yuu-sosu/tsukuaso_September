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

# ボタン定義
BUTTON_START = pygame.Rect(300, 300, 200, 80)
BUTTON_GATCHA = pygame.Rect(250, 450, 300, 100)
BUTTON_TO_ENCYCLOPEDIA = pygame.Rect(650, 30, 130, 50)
BUTTON_TO_GATCHA = pygame.Rect(20, 30, 130, 50)

# ラーメンデータ
RAMEN_DATA = {
    '博多ラーメン': {
        'weight': 0.30,
        'region': '九州',
        'rarity': 'N',
        'image': 'assets/images/tonkotsu.png'
    },
    '札幌味噌ラーメン': {
        'weight': 0.25,
        'region': '北海道',
        'rarity': 'N',
        'image': 'assets/images/sapporo.png'
    },
    '喜多方ラーメン': {
        'weight': 0.15,
        'region': '東北',
        'rarity': 'R',
        'image': 'assets/images/syouyu.png'
    },
    '尾道ラーメン': {
        'weight': 0.10,
        'region': '中国',
        'rarity': 'R',
        'image': 'assets/images/abura.png'
    },
    '和歌山ラーメン': {
        'weight': 0.08,
        'region': '近畿',
        'rarity': 'SR',
        'image': 'assets/images/tukemen.png'
    },
    '家系ラーメン': {
        'weight': 0.07,
        'region': '関東',
        'rarity': 'SR',
        'image': 'assets/images/ie.png'
    },
    '幻の金のラーメン': {
        'weight': 0.05,
        'region': '全国',
        'rarity': 'SSR',
        'image': 'assets/images/ziro.png'
    },
}


FONT_PATH = os.path.join("assets", "fonts", "NotoSansCJKjp-Regular.otf")
