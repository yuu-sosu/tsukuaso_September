import pygame
import random
from config import *
from game_logic import *

def pull_ramen():
    names = list(RAMEN_DATA.keys())
    weights = [RAMEN_DATA[name]['weight'] for name in names]
    return random.choices(names, weights=weights)[0]

def update_encyclopedia(encyclopedia, ramen_name, total_pulls):
    count, first_time = encyclopedia[ramen_name]
    if count == 0:
        first_time = pygame.time.get_ticks()
    encyclopedia[ramen_name] = (count + 1, first_time)
    return total_pulls + 1

def all_ramen_collected(encyclopedia):
    """全てのラーメンが1回以上引かれているか"""
    return all(count > 0 for count, _ in encyclopedia.values())
	
def handle_events(event, state, ramen_count, encyclopedia, last_pulled):
    global final_remaining_time  # 追加
    if event.type == pygame.QUIT:
        return False, state, ramen_count, last_pulled

    if event.type == pygame.MOUSEBUTTONDOWN:
        if state == STATE_TITLE and BUTTON_START.collidepoint(event.pos):
            state = STATE_GATCHA
            start_timer()  # タイマー開始

        elif state == STATE_GATCHA:
            if BUTTON_GATCHA.collidepoint(event.pos):
                ramen_name = pull_ramen()
                ramen_count += 1
                last_pulled = ramen_name
                update_encyclopedia(encyclopedia, ramen_name, ramen_count)

                # コンプリート判定
                if all_ramen_collected(encyclopedia):
                    if final_remaining_time is None:
                        final_remaining_time = get_remaining_time()  # ここで固定
                    state = STATE_GAMECLEAR

            elif BUTTON_TO_ENCYCLOPEDIA.collidepoint(event.pos):
                pause_timer()
                state = STATE_ENCYCLOPEDIA

        elif state == STATE_ENCYCLOPEDIA and BUTTON_TO_GATCHA.collidepoint(event.pos):
            resume_timer()
            state = STATE_GATCHA

    return True, state, ramen_count, last_pulled
