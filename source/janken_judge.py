def judge():
    if U_hand == 1:
        if P_hand == 1:
            print('引き分けです。')
            tie += 1
        elif P_hand == 2:
            print('コンピュータの勝ちです。')
            lose += 1
        else:
            print('あなたの勝ちです。')
            win += 1
    if U_hand == 2:
        if P_hand == 1:
            print('あなたの勝ちです。')
            win += 1
        elif P_hand == 2:
            print('引き分けです。')
            tie += 1
        else:
            print('コンピュータの勝ちです。')
            lose += 1
    if U_hand == 3:
        if P_hand == 1:
            print('コンピュータの勝ちです。')
            lose += 1
        elif P_hand == 2:
            print('あなたの勝ちです。')
            win += 1
        else:
            print('引き分けです。')
            tie += 1
    return (win, lose, tie)