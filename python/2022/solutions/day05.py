#!/usr/bin/env python3

import re

from utils import aoc

aoc.setup(2022, 5)
p1_answer = ""
p2_answer = ""

# Helpers


# Part 1
fin = aoc.get_input()
number_of_columns = -1
columns_p1 = []
columns_p2 = []
reversed_it = False
for line in fin.readlines():
    if line.__contains__('['):
        doing_boxes = True
    else:
        doing_boxes = False
        if not reversed_it:
            for index, col in enumerate(columns_p1):
                col.reverse()
                columns_p1[index] = col
            for index, col in enumerate(columns_p2):
                col.reverse()
                columns_p2[index] = col
            reversed_it = True

    if doing_boxes:
        if number_of_columns == -1:
            number_of_columns = int(len(line) / 4)
            columns_p1 = [None] * number_of_columns
            columns_p2 = [None] * number_of_columns

        line = line.replace('[', '').replace(']', '').strip('\n').replace('    ', '_').replace(' ', '')

        for index, box in enumerate(line):
            if box == '_':
                continue
            else:
                if columns_p1[index] == None:
                    columns_p1[index] = []
                    columns_p2[index] = []
                columns_p1[index].append(box)
                columns_p2[index].append(box)
            index += 1

    if not doing_boxes:
        m = re.search('move (\\d+) from (\\d+) to (\\d+)', line.strip('\n'))
        if m != None:
            moves = int(m.group(1))
            from_box = int(m.group(2)) - 1
            to_box = int(m.group(3)) - 1

            columns_p2[to_box].extend(columns_p2[from_box][-moves:])
            columns_p2[from_box] = columns_p2[from_box][:-moves]
            for i in range(0, moves):
                columns_p1[to_box].append(columns_p1[from_box].pop())

for col in columns_p1:
    p1_answer += col[-1]

for col in columns_p2:
    p2_answer += col[-1]

aoc.print_answer(1, p1_answer)
aoc.print_answer(2, p2_answer)

