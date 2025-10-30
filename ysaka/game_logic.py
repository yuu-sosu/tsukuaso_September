import pygame
from config import GAME_TIME_LIMIT

start_time = None  # ゲーム開始時刻を保存

import pygame
from config import GAME_TIME_LIMIT

start_time = None
paused_time = 0
pause_start = None  # 一時停止開始時刻

def start_timer():
    global start_time, paused_time
    start_time = pygame.time.get_ticks()
    paused_time = 0

def pause_timer():
    global pause_start
    if pause_start is None:
        pause_start = pygame.time.get_ticks()

def resume_timer():
    global paused_time, pause_start
    if pause_start is not None:
        paused_time += pygame.time.get_ticks() - pause_start
        pause_start = None

def get_remaining_time():
    if start_time is None:
        return GAME_TIME_LIMIT
    elapsed = (pygame.time.get_ticks() - start_time - paused_time) / 1000
    remaining = max(0, GAME_TIME_LIMIT - int(elapsed))
    return remaining
