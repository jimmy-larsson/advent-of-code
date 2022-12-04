#!/usr/bin/env python3

from utils import aoc

aoc.setup(2022, 4)
p1_answer = 0
p2_answer = 0


# Helpers
def sector_to_map(input):
    lower = int(input.split('-')[0])
    upper = int(input.split('-')[1])

    return set(list(range(lower, upper+1)))


# Solution
fin = aoc.get_input()

for line in fin.readlines():
    elf_1_sections, elf_2_sections = line.strip('\n').split(',')

    elf_1_map = sector_to_map(elf_1_sections)
    elf_2_map = sector_to_map(elf_2_sections)

    # Part 1
    if elf_1_map.issubset(elf_2_map) or elf_2_map.issubset(elf_1_map):
        p1_answer += 1

    # Part 2
    if elf_1_map.intersection(elf_2_map):
        p2_answer += 1


aoc.print_answer(1, p1_answer)
aoc.print_answer(2, p2_answer)
