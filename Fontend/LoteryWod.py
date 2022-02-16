import os
import json
import random
from sys import argv
from collections import Counter
from Card import FrenchDeck

def setGroupNum(person):
    group = 0
    if person < 6:
        group = person
    elif person < 10:
        group = 2
    elif person < 16:
        group = 3
    else:
        group = 4
    if person == 9:
        group = 3

    configFile = "input"
    main_wd = os.getcwd()
    with open('{}/{}.json'.format(main_wd, configFile), mode='r', errors='ignore') as json_file:
        settings = json.load(json_file)

    for i in range(group):
        settings['team'][i] = 'True'

    print('loterywod', group)
    return group

# def randomCards():
#     randomDeck = FrenchDeck()
#     randomCard = random.choice(randomDeck)  # 随机选取一个元素
#     return randomCard

def selectCards():
    cardDeck = FrenchDeck()
    luckyCard = random.choice(cardDeck)  # 随机选取一个元素
    cardDeck.remove(luckyCard)
    return luckyCard

def selectWod():
    wodDeck = FrenchDeck()
    luckyWod = random.choice(wodDeck)  # 随机选取一个元素
    wodDeck.remove(luckyWod)
    return luckyWod

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
        lucky = selectCards()
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