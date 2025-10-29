
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
            handle_gatcha_events(event)
        elif current_state == STATE_ENCYCLOPEDIA:
            handle_encyclopedia_events(event)

    # 2. ロジック更新 (クッキークリッカー要素)
    update_clicker_logic() 

    # 3. 描画処理
    if current_state == STATE_GATCHA:
        draw_gatcha_screen()
    elif current_state == STATE_ENCYCLOPEDIA:
        draw_encyclopedia_screen()

    # 4. 画面更新とフレームレート設定
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
