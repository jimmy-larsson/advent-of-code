#!/usr/bin/env python3

from utils import aoc

aoc.setup(2022, 2)


# Part 1
def getScore(hand):
    if hand == 'A' or hand == 'X': return 1
    if hand == 'B' or hand == 'Y': return 2
    if hand == 'C' or hand == 'Z': return 3


def calculateScore(h1, h2):
    s1 = getScore(h1)
    s2 = getScore(h2)
    if s1 == s2:
        return 3 + s2

    if (s1 % 3) + 1 == s2:
        return 6 + s2

    else:
        return s2


fin = aoc.get_input()
sum = 0
for round in fin.readlines():
    hands = round.split()
    sum = sum + calculateScore(hands[0], hands[1])

aoc.print_answer(1, sum)


# Part 2
def getHand(e):
    if e == 1:
        return 'X'
    if e == 2:
        return 'Y'
    if e == 3:
        return 'Z'


def calculateTrueScore(h1, outcome):
    if outcome == 'X':
        tmp = (getScore(h1) - 2) % 3
        return calculateScore(h1, getHand(tmp + 1))
    if outcome == 'Y':
        return calculateScore(h1, h1)
    if outcome == 'Z':
        tmp = getScore(h1) % 3
        return calculateScore(h1, getHand(tmp + 1))


fin = aoc.get_input()
sum = 0
for round in fin.readlines():
    hand_to_outcome = round.split()
    sum = sum + calculateTrueScore(hand_to_outcome[0], hand_to_outcome[1])

aoc.print_answer(2, sum)
