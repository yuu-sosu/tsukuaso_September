import pygame
import sys
import random

# --- 初期化 ---
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("クリックでスコアアップ！")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 60)

# --- 色 ---
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# --- 丸の情報 ---
radius = 40

# --- スコア ---
score = 0

# --- メインループ ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # マウスクリックイベント
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos  # クリック座標
            # クリックが円の中かどうか判定
            distance = ((mx - x) ** 2 + (my - y) ** 2) ** 0.5
            if distance <= radius:
                score += 1

    # --- 画面描画 ---
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (20, 20))

    pygame.display.flip()
    clock.tick(60)
