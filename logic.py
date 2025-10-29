
# ==============================================================================
# 4. ロジック関数 (ガチャ / クリッカー)
# ==============================================================================

def pull_gatcha():
    """ガチャを1回引き、結果を返して図鑑を更新する"""
    global encyclopedia, ramen_count, last_pulled_ramen
    
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

def update_clicker_logic():
    """時間経過でガチャ回数を自動増加させる"""
    global ramen_count, LAST_TICK_TIME
    
    current_time = pygame.time.get_ticks()
    
    # ラーメンの自動増加速度を決定（将来的にアップグレードで変動する部分）
    gain_rate_ms = BASE_RAMEN_GAIN_RATE_MS 
    
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

def handle_gatcha_events(event):
    """ガチャ画面でのイベント処理"""
    global current_state

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos
        
        # ガチャボタンのクリック判定
        if BUTTON_GATCHA.collidepoint(mouse_pos):
            pull_gatcha()

        # 図鑑へボタンのクリック判定
        if BUTTON_TO_ENCYCLOPEDIA.collidepoint(mouse_pos):
            current_state = STATE_ENCYCLOPEDIA

def handle_encyclopedia_events(event):
    """図鑑画面でのイベント処理"""
    global current_state

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos
        
        # ガチャへボタンのクリック判定
        if BUTTON_TO_GATCHA.collidepoint(mouse_pos):
            current_state = STATE_GATCHA

