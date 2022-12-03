#!/usr/bin/env python3

from utils import aoc

aoc.setup(2022, 3)
p1_sum = 0
p2_sum = 0


# Helper
def get_item_score(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 1 + 26


fin = aoc.get_input()
elf = 0
intersecting_badges = set()
for rucksack in fin.readlines():
    rucksack = rucksack.strip('\n')

    # Part 1
    intersecting_items = set(rucksack[:len(rucksack) // 2]).intersection(rucksack[len(rucksack) // 2:])

    for item in intersecting_items:
        p1_sum += get_item_score(item)

    # Part 2
    if elf % 3 == 0:
        intersecting_badges = set(list(rucksack))
    else:
        intersecting_badges = intersecting_badges.intersection(rucksack)
    elf += 1

    if elf % 3 == 0 and len(intersecting_badges) > 0:
        p2_sum += get_item_score(intersecting_badges.pop())

aoc.print_answer(1, p1_sum)
aoc.print_answer(2, p2_sum)
