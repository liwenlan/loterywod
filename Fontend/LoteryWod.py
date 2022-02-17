import os
import json
import random
from sys import argv
from collections import Counter
from Card import AthleteDeck, WodDeck

def setGroupNum(person, team):
    group = 0
    # 1-5人 X组
    # 6-8、10人 2组
    # 11-15、9人 3组
    # 16-24人 4组
    if person < 6:
        group = person
    elif person < 10:
        group = 2
    elif person < 16:
        group = 3
    elif person <= 24:
        group = 4
    if person == 9:
        group = 3

    for i in range(group):
        team[i] = 1

    return group

def setTeamNum(person):
    """
    1-5 X组，每组1人
    6-8组，10人：2组，每组X/2人
    11-15组，9人：3组，11->4,4,3  12:4,4,4  13: 4,4,5  14:4,5,5  9:3 3 3    X/3
    16-24: X/4  16:(4,4,4,4), 17:(4,4,4,5), 18:(4,4,5,5), 19:(4,5,5,5), 20:(5,5,5,5), 21:(5,5,5,6),
    22:(5,5,6,6), 23:(5,6,6,6), 24:(6,6,6,6)
    :param person:
    :param group:
    :return:
    """
    dict_team = {1: [1, 0, 0, 0, 0], 2: [1, 1, 0, 0, 0], 3: [1, 1, 1, 0, 0], 4: [1, 1, 1, 1, 0], 5: [1, 1, 1, 1, 1],
                 6: [3, 3, 0, 0, 0], 7: [3, 4, 0, 0, 0], 8: [4, 4, 0, 0, 0], 9: [3, 3, 3, 0, 0], 10: [5, 5, 0, 0, 0],
                 11: [3, 4, 4, 0, 0], 12: [4, 4, 4, 0, 0], 13: [4, 4, 5, 0, 0], 14: [4, 5, 5, 0, 0], 15: [5, 5, 5, 0, 0],
                 16: [4, 4, 4, 4, 0], 17: [4, 4, 4, 5, 0], 18: [4, 4, 5, 5, 0], 19: [4, 5, 5, 5, 0], 20: [5, 5, 5, 5, 0],
                 21: [5, 5, 5, 6, 0], 22: [5, 5, 6, 6, 0], 23: [5, 6, 6, 6, 0], 24: [6, 6, 6, 6, 0]}
    return dict_team[person]

# def randomCards():
#     randomDeck = FrenchDeck()
#     randomCard = random.choice(randomDeck)  # 随机选取一个元素
#     return randomCard

def selectWod():
    wodDeck = WodDeck()
    luckyWod = random.choice(wodDeck)  # 随机选取一个元素
    wodDeck.remove(luckyWod)
    return luckyWod

def selectAthlete():
    athleteDeck = AthleteDeck()
    luckyCard = random.choice(athleteDeck)  # 随机选取一个元素
    return luckyCard


def calculateScore(score_list, team):
    score_list[team - 1] = score_list[team - 1] + 1
    print('score_list is {}'.format(score_list))

def whoWins():
    instr = int(input("which team wins this round？ "))
    print("input >> {}".format(instr))
    return instr

def playA(group):  # 每人一队
    score_list = [0] * group

def playB(group):  # 分组
    score_list = [0] * group
    lucky_list = []
    for i in range(4):
        lucky = selectWod()
        lucky_list.append(lucky)
        # team = whoWins()
        # calculateScore(score_list, team)
    # lucky_list.append(selectCards())
    # maxValue = max(score_list)
    # if maxValue in dict(Counter(score_list)):
    #     print("Final PK !!!")
    #     first = score_list.index(maxValue)
    #     second = score_list.index(maxValue, first + 1)
    #     print("team{} and team{}".format(first+1, second+1))
    print('lucky is {}'.format(lucky_list))

def playC(person):
    pass

if __name__ == '__main__':
    # cards = ['A', 'B', 'C', 'D'] * 13
    configFile = "input"
    main_wd = os.getcwd()
    with open('{}/{}.json'.format(main_wd, configFile), mode='r', errors='ignore') as json_file:
        settings = json.load(json_file)

    person = int(argv[1])
    group = setGroupNum(person)

    if person > 0 and person < 6 :
        playA(group)
    elif person < 15:
        playB(group)
    else:
        playC(group)
    
    print("--------")