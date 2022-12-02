#!/usr/bin/env python3

from utils import aoc

aoc.setup(2022, 1)
fin = aoc.get_input()

elves = fin.read().split('\n\n')
elves = sorted([sum(tuple(map(int, elf.split()))) for elf in elves], reverse=True)

part1 = elves[0]
part2 = sum(elves[:3])

aoc.print_answer(1, part1)
aoc.print_answer(2, part2)