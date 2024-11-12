def judge(U_hand, P_hand):
    if U_hand == 1:
        if P_hand == 1:
            print('引き分けです。')
            return 'tie'
        elif P_hand == 2:
            print('コンピュータの勝ちです。')
            return 'lose'
        else:
            print('あなたの勝ちです。')
            return 'win'
    if U_hand == 2:
        if P_hand == 1:
            print('あなたの勝ちです。')
            return 'win'
        elif P_hand == 2:
            print('引き分けです。')
            return 'tie'
        else:
            print('コンピュータの勝ちです。')
            return 'lose'
    if U_hand == 3:
        if P_hand == 1:
            print('コンピュータの勝ちです。')
            return 'lose'
        elif P_hand == 2:
            print('あなたの勝ちです。')
            return 'win'
        else:
            print('引き分けです。')
            return 'tie'