#!/usr/bin/env python3

import re
from copy import deepcopy

from utils import aoc

aoc.setup(2022, 5)
p1_answer = ""
p2_answer = ""
rows = []
columns = []

fin = aoc.get_input()

for line in fin:
    if line == '\n':  # Done with the box rows.
        break
    rows.append(line.strip('\n'))

for index, column in enumerate(zip(*rows)):  # Using zip to transpose the matrix of rows.
    if index % 4 == 1:  # Every 4th character is a box, starting from character index 1.
        column_tmp = list(''.join(column[:-1]).lstrip())
        column_tmp.reverse()
        columns.append(column_tmp)

columns_p1 = deepcopy(columns)
columns_p2 = deepcopy(columns)
for line in fin:
    match = re.search('move (\\d+) from (\\d+) to (\\d+)', line.strip('\n'))
    if match is not None:
        moves, from_box, to_box = map(int, match.groups())
        moves = int(match.group(1))
        from_box = from_box - 1  # Adjust to actual index
        to_box = to_box - 1  # Adjust to actual index

        # Part 1 - Pop one element at a time
        for i in range(0, moves):
            columns_p1[to_box].append(columns_p1[from_box].pop())

        # Part 2 - Move multiple elements at once by splitting and extending the arrays
        columns_p2[to_box].extend(columns_p2[from_box][-moves:])
        columns_p2[from_box] = columns_p2[from_box][:-moves]

for col in columns_p1:
    p1_answer += col[-1]

for col in columns_p2:
    p2_answer += col[-1]

aoc.print_answer(1, p1_answer)
aoc.print_answer(2, p2_answer)
