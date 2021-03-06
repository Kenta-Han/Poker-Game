# -*- coding: utf-8 -*-
# Pokerを動かす為のメインプログラム

from Poker import Poker
from Tactics import tactics

# 初期化
Poker = Poker()

# 初回の手札表示
print(Poker.printhand())

# 繰り返し処理(５回)
c_card = []
for count in range(5):
    print('\n\n{}回目の手札交換を行います．\n"c"を入力してください：'.format(count+1),end="")
    x = input()

    # 手札交換
    c_card = tactics(Poker.gethand(),count)
    Poker.change_card(c_card)
    print(Poker.printhand())
