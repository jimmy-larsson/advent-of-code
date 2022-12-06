#!/usr/bin/env python3

from utils import aoc

aoc.setup(2022, 6)


# Helpers
def find_solution(data, puzzle_length):
    for index in range(puzzle_length, len(data)):
        if len(set(data[index - puzzle_length:index])) == puzzle_length:
            return index


# Note: We can never find a longer unique string earlier than we found the shorter unique string meaning that
#       we could also pass on a start_index=p1_answer when calculating p2_answer if we wanted to optimize it further.

data = aoc.get_input().readlines()[0].rstrip('\n')
p1_answer = find_solution(data, 4)
p2_answer = find_solution(data, 14)

aoc.print_answer(1, p1_answer)
aoc.print_answer(2, p2_answer)
