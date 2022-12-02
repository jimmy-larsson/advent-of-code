#!/usr/bin/env python3

from utils import aoc

aoc.setup(2022, 1)

# Part 1
fin = aoc.get_input()
max_calories = 0
current_calorie_sum = 0

for line in fin:
    value = int(line) if line != "\n" else -1

    if value == -1:
        max_calories = max(max_calories, current_calorie_sum)
        current_calorie_sum = 0
    else:
        current_calorie_sum = current_calorie_sum + value

aoc.print_answer(1, max_calories)
# aoc.submit_answer(1, max_calories)

# Part 2 - Starting over from scratch
fin = aoc.get_input()
max_calories = [0, 0, 0]
current_calorie_sum = 0

for line in fin:
    value = int(line) if line != "\n" else -1

    if value == -1:
        index_min = min(range(len(max_calories)), key=max_calories.__getitem__)
        max_calories[index_min] = max(max_calories[index_min], current_calorie_sum)
        current_calorie_sum = 0
    else:
        current_calorie_sum = current_calorie_sum + value

aoc.print_answer(2, sum(max_calories))
# aoc.submit_answer(2, sum(max_calories))
