# -*- coding: utf-8 -*-

def tactics(hand,times):
    # 手札と回数から何を変更するべきか決定するプログラムメソッド（これを作成する）
    # hand = 手札
    # times = 回数
    # 変更するカード番号を返す

    # ダミープログラム（奇数回は奇数番，偶数回は偶数番を変更）
    if (times % 2) == 0:
        return [0,2,4]
    else:
        return [1,3]
