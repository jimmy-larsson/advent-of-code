#!/usr/bin/env python3

from utils import aoc

aoc.setup(2022, 4)
p1_answer = 0
p2_answer = 0


# Helpers

# Solution
fin = aoc.get_input()

for line in fin.readlines():
    elf_1_sections, elf_2_sections = line.strip('\n').split(',')
    elf_1_lower, elf_1_upper = map(int, elf_1_sections.split('-'))
    elf_2_lower, elf_2_upper = map(int, elf_2_sections.split('-'))
    elf_1_set = set(range(elf_1_lower, elf_1_upper+1))
    elf_2_set = set(range(elf_2_lower, elf_2_upper+1))

    # Part 1
    if elf_1_set.issubset(elf_2_set) or elf_2_set.issubset(elf_1_set):
        p1_answer += 1

    # Part 2
    if elf_1_set.intersection(elf_2_set):
        p2_answer += 1


aoc.print_answer(1, p1_answer)
aoc.print_answer(2, p2_answer)
