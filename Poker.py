# -*- coding: utf-8 -*-
# poker用のclass
import random

class Poker:
    # デッキ用リスト
    __deck=[]
    # 手札用リスト
    __hand=[]

    # コンストラクタ
    def __init__(self):
        list_word = ["s","h","d","c"]
        list_num = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        ## 52枚のカード作成
        card_list = []
        for i in list_word:
            for j in list_num:
                card_list.append([i,j])

        # カードをシャッフル
        card_list = random.sample(card_list,len(card_list))
        # 手札
        self.__hand = card_list[:5]
        # 山札
        self.__deck = card_list[6:]

    # ゲッタ
    def gethand(self):
        return self.__hand

    # 綺麗に表示
    def printhand(self):
        card  = []
        for i in self.__hand:
            card.append(i[0]+str(i[1]))
        return card

    # 手札入れ替え
    # 指定された引数をデック先頭と入れ替え，デックからpop
    def change_card(self,change_num):
        for i in change_num:
            self.__hand[i] = self.__deck.pop(0)
