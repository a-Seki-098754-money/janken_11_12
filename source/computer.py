def pon():
    P_hand = random.randint(0,2)
    if P_hand == 1:
        print('コンピュータの手：グー')
    elif P_hand == 2:
        print('コンピュータの手：チョキ')
    else:
        print('コンピュータの手：パー')
    return P_hand