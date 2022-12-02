#!/usr/bin/env python3

from utils import aoc

aoc.setup(2022, 2)
fin = aoc.get_input()

ord_a = ord('A')  # 65
ord_x = ord('X')  # 88

score_p1 = 0
score_p2 = 0

for a, b in map(str.split, fin):
    a = ord(a) - ord_a
    b = ord(b) - ord_x

    # Part 1
    score_p1 += b + 1  # The score of the hand is hand_score = b + 1

    if a == 0:
        score_p1 += ((b + 1) % 3) * 3  # The round score if the opponent does rock is round_score = ((b + 1) % 3) * 3
    elif a == 1:
        score_p1 += b * 3  # The round score if the opponent uses paper is round_score = b * 3
    else:
        score_p1 += ((b + 2) % 3) * 3  # The round score if the opponent uses scissor is round_score = ((b + 2) % 3) * 3

    # Part 2
    if b == 0:  # Lose
        score_p2 += 0  # Just to make it extra clear that this is a loss
        score_p2 += (a - 1) % 3 + 1
    elif b == 1:  # Draw
        score_p2 += 3
        score_p2 += a + 1
    else:  # Win
        score_p2 += 6
        score_p2 += ((a + 1) % 3) + 1

aoc.print_answer(1, score_p1)
aoc.print_answer(2, score_p2)
