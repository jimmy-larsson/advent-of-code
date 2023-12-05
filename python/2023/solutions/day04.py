#!/usr/bin/env python3
import re
from collections import defaultdict

import numpy

from python.utils import aoc


def main():
    # Preparations
    aoc.setup(2023, 4)

    # Sample 1
    sample_input_1 = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
                        Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
                        Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
                        Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
                        Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
                        Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    aoc.print_answer("1 - Sample", part1(sample_input_1.splitlines()))

    # Part 1
    input = aoc.get_input()
    part1_answer = part1(input)
    aoc.print_answer(1, part1_answer)
    # aoc.submit_answer(1, part1_answer)

    # Sample 2
    sample_input_2 = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
                        Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
                        Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
                        Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
                        Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
                        Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    aoc.print_answer("2 - Sample", part2(sample_input_2.splitlines()))

    # Part 2
    input = aoc.get_input().readlines()
    part2_answer = part2(input)
    aoc.print_answer(2, part2_answer)
    # aoc.submit_answer(2, part2_answer)


def part1(input_raw):
    input = [line.strip() for line in input_raw if line.strip() != ""]

    sum = 0
    for line in input:
        card, values = line.split(':')
        [winning], [owned] = [values.split('|')[0].split()], [values.split('|')[1].split()]
        winning = set().union(winning)
        owned = set().union(owned)
        matches = winning.intersection(owned)
        score = 0 if len(matches) == 0 else 2 ** (len(matches)-1)
        sum += score

    return sum


def part2(input_raw):
    input = [line.strip() for line in input_raw if line.strip() != ""]
    scratchcards = { i:1 for i in range(1, len(input)+1) }

    for line in input:
        card, values = line.split(':')
        card_id = card.split()[1]
        [winning], [owned] = [values.split('|')[0].split()], [values.split('|')[1].split()]
        winning = set().union(winning)
        owned = set().union(owned)
        matches = winning.intersection(owned)
        for i in range(1, len(matches)+1):
            scratchcards[int(card_id)+i] = scratchcards[int(card_id)+i] + scratchcards[int(card_id)]

    return sum(scratchcards.values())


if __name__ == "__main__":
    main()
