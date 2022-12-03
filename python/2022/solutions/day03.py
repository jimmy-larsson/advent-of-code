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


# Part 1
fin = aoc.get_input()
for rucksack in fin.readlines():
    rucksack = rucksack.strip('\n')
    intersecting_items = set(rucksack[:len(rucksack) // 2]).intersection(rucksack[len(rucksack) // 2:])

    for item in intersecting_items:
        p1_sum += get_item_score(item)
aoc.print_answer(1, p1_sum)

# Part 2
fin = aoc.get_input()
elf = 0
for rucksack in fin.readlines():
    rucksack = rucksack.strip('\n')
    if elf % 3 == 0:
        elf_check = set(list(rucksack))
    else:
        elf_check = elf_check.intersection(rucksack)

    elf += 1
    if elf % 3 == 0:
        p2_sum += get_item_score(elf_check.pop())

aoc.print_answer(2, p2_sum)
