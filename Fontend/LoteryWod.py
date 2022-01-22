import os
import json
import random
from sys import argv
from collections import Counter


def setGroupNum(person):
    group = 0
    if person < 7:
        group = person
    elif person < 12:
        group = 2
    elif person < 16:
        group = 3
    else:
        group = 4
    if person == 9:
        group = 3
    return group

def selectCards():
    lucky = random.choice(cards)  # 随机选取一个元素
    # print(cards)
    cards.remove(lucky)
    # print(cards)
    # print("---------------")
    return lucky

def calculateScore(score_list, team):
    score_list[team - 1] = score_list[team - 1] + 1
    print('score_list is {}'.format(score_list))

def whoWins():
    instr = int(input("which team wins this round？ "))
    print("input >> {}".format(instr))
    return instr

def playA(person):  # 每人一队
    groupNum = setGroupNum(person)



def playB(person):  # 分组
    groupNum = setGroupNum(person)
    score_list = [0] * groupNum
    lucky_list = []
    for i in range(4):
        lucky_list.append(selectCards())
        team = whoWins()
        calculateScore(score_list, team)
    lucky_list.append(selectCards())
    maxValue = max(score_list)
    if maxValue in dict(Counter(score_list)):
        print("Final PK !!!")
        first = score_list.index(maxValue)
        second = score_list.index(maxValue, first + 1)
        print("team{} and team{}".format(first+1, second+1))
    print('lucky is {}'.format(lucky_list))

if __name__ == '__main__':
    cards = ['A', 'B', 'C', 'D'] * 13
    configFile = "config"
    main_wd = os.getcwd()
    with open('{}/config/{}.json'.format(main_wd, configFile), mode='r', errors='ignore') as json_file:
        settings = json.load(json_file)

    person = int(argv[1])
    if person < 6 and person > 0:
        playA(person)
    elif person < 24:
        playB(person)
    for i in range(10):
        selectCards()

    print("--------")