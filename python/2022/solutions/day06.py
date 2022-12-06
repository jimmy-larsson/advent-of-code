#!/usr/bin/env python3

from utils import aoc

aoc.setup(2022, 6)


# Helpers
def find_solution(fin, puzzle_length):
    arr = [None] * puzzle_length

    for index, char in enumerate(fin.read()):
        arr[index % puzzle_length] = char
        if index >= puzzle_length:
            if len(set(arr)) == puzzle_length:
                return index+1


p1_answer = find_solution(aoc.get_input(), 4)
p2_answer = find_solution(aoc.get_input(), 14)

aoc.print_answer(1, p1_answer)
aoc.print_answer(2, p2_answer)
