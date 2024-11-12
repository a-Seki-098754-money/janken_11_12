# ユーザーの手の入力
def pon():
    print('1.グー 2.チョキ 3.パー\nグー、チョキ、パーのいずれかを入力してください＞')
    U_hand = int(input())
    if U_hand == 1:
        print('あなたの手：グー')
    elif U_hand == 2:
        print('あなたの手：チョキ')
    else:
        print('あなたの手：パー')
    return U_hand