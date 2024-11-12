import random
import player
import computer
import janken_judge

def janken_main():
    win = 0
    lose = 0
    tie = 0
    for _ in range(3):
        U_hand = player.pon()
        P_hand = computer.pon()
        result = map(int, janken_judge.judge(U_hand, P_hand))
        if result == 'win':
            win += 1
        elif result == 'lose':
            lose += 1
        else:
            tie += 1
    if win > lose:
        total_result = 'あなたの総合勝利です。'
    elif win < lose:
        total_result = 'コンピュータの総合勝利です。'
    else:
        total_result = '引き分けです。'
    print(f'【最終結果】\nあなた：{win}勝\nコンピュータ：{lose}勝\n{total_result}')