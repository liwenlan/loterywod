import os
import json
import random
from sys import argv
from collections import Counter
import numpy as np
from Card import AthleteDeck, WodDeck

wodBomb = ['A', '2', '3', '4', '5']
rule_A = {'heart': 2, 'spade': 2, 'club': 2, 'diamond': 2, 'bomb': 3}

def rulesForA(flower, num, rule_A):
    if num in wodBomb:
        flower = 'bomb'
    rule_A[flower] = rule_A[flower] - 1



def rulesForPerRound_A():
    pass

def selectActionWithoutBack(wodDeck, card_flower, card_number, rule_A, index):
    """
    1. 选取动作，不放回
    2. 一次抽两张牌
    3. 两张牌不能是一样的动作，只能出现最多一次的炸弹
    """
    if card_flower == [] and rule_A['bomb'] != 0:
        action = np.random.choice(['heart', 'spade', 'club', 'diamond'], 1, True)
        num = np.random.choice(['A', '2', '3', '4', '5'], 1, True)  # 随机选取一个元素
    else:
        num = np.random.choice(card_number, 1, False)  # 随机选取一个元素
        action = np.random.choice(card_flower, 1, False)  # 随机选取一个元素

    print("抽牌card is ", action[0] + '_' + num[0])
    rulesForA(action[0], num[0], rule_A)  # 更新剩余次数
    print("remain is ", rule_A)

    if num in wodDeck.bomb:
        for b in wodDeck.bomb:
            card_number.remove(b)
    else:
        for a in action:
            card_flower.remove(a)



def modeA():
    totalTime = 30  # min
    round = 5
    wodDeck = WodDeck()
    index = 0
    for i in range(0, round):
        print("第", i+1, "轮")
        card_flower = ['heart', 'spade', 'club', 'diamond']
        card_number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for action in rule_A:
            if rule_A[action] == 0:
                if action != 'bomb':
                    card_flower.remove(action)
                else:
                    card_number = ['6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # print("card_flower IS ", card_flower)
        # print("card_number IS ", card_number)
        # print("rule_A IS ", rule_A)
        for j in range(0, 2):
            selectActionWithoutBack(wodDeck, card_flower, card_number, rule_A, index)
            index += 1
        print("------------------------------------")

def modeB():
    pass

def modeC():
    pass


def getTeamNum(person):
    """
    1-5 X组，每组1人
    6-8组，10人：2组，每组X/2人
    11-15组，9人：3组，11->4,4,3  12:4,4,4  13: 4,4,5  14:4,5,5  9:3 3 3    X/3
    16-24: X/4  16:(4,4,4,4), 17:(4,4,4,5), 18:(4,4,5,5), 19:(4,5,5,5), 20:(5,5,5,5), 21:(5,5,5,6),
    22:(5,5,6,6), 23:(5,6,6,6), 24:(6,6,6,6)
    :param person:
    :param group:
    :return:list，组数以及每组的人数
    """
    dict_team = {1: [1], 2: [1, 1], 3: [1, 1, 1], 4: [1, 1, 1, 1], 5: [1, 1, 1, 1, 1],
                 6: [3, 3], 7: [3, 4], 8: [4, 4], 9: [3, 3, 3], 10: [3, 3, 4],
                 11: [3, 4, 4], 12: [4, 4, 4], 13: [3, 3, 3, 4], 14: [3, 3, 4, 4], 15: [3, 4, 4, 4],
                 16: [4, 4, 4, 4], 17: [4, 4, 4, 5], 18: [4, 4, 5, 5], 19: [4, 5, 5, 5], 20: [5, 5, 5, 5],
                 21: [5, 5, 5, 6], 22: [5, 5, 6, 6], 23: [5, 6, 6, 6], 24: [6, 6, 6, 6]}
    return dict_team[person]

def selectMode(personNum):
    teamNum = getTeamNum(personNum)
    eachTeam = len(teamNum)   # 队伍数量
    if personNum < 7:
        modeA()
    elif personNum < 17:
        modeB()
    elif personNum <= 24:
        modeC()



if __name__ == '__main__':
    selectMode(4)