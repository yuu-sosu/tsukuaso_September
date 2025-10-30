import pygame
from config import GAME_TIME_LIMIT

start_time = None  # ゲーム開始時刻を保存

def start_timer():
    global start_time
    start_time = pygame.time.get_ticks()

def get_remaining_time():
    """残り時間（秒）を返す"""
    if start_time is None:
        return GAME_TIME_LIMIT
    elapsed = (pygame.time.get_ticks() - start_time) / 1000
    remaining = max(0, GAME_TIME_LIMIT - int(elapsed))
    return remaining
