#!/usr/bin/env python3
import re

import numpy

from python.utils import aoc


def main():
    # Preparations
    aoc.setup(2023, 3)

    # Sample 1
    sample_input_1 = """467..114..
                        ...*......
                        ..35..633.
                        ......#...
                        617*......
                        .....+.58.
                        ..592.....
                        ......755.
                        ...$.*....
                        .664.598.."""
    aoc.print_answer("1 - Sample", part1(sample_input_1.splitlines()))

    # Part 1
    input = aoc.get_input()
    part1_answer = part1(input)
    aoc.print_answer(1, part1_answer)
    # aoc.submit_answer(1, part1_answer)

    # Sample 2
    sample_input_2 = """467..114..
                        ...*......
                        ..35..633.
                        ......#...
                        617*......
                        .....+.58.
                        ..592.....
                        ......755.
                        ...$.*....
                        .664.598.."""
    aoc.print_answer("2 - Sample", part2(sample_input_2.splitlines()))

    # Part 2
    input = aoc.get_input().readlines()
    part2_answer = part2(input)
    aoc.print_answer(2, part2_answer)
    # aoc.submit_answer(2, part2_answer)


def part1(input_raw):
    input = [line.strip() for line in input_raw if line.strip() != ""]

    is_valid_matrix = [[]]
    row = 0

    # Mark valid or not
    for line in input:
        line = line.strip()
        if line == "":
            continue

        if is_valid_matrix == [[]]:
            is_valid_matrix = [[False for _ in range(len(line))] for _ in range(len(input))]

        for column, character in enumerate(line):
            if character != "." and not character.isnumeric():
                mark_valid(is_valid_matrix, column, row)
        row += 1

    # Calculate sums:
    values = []
    row = 0
    value_as_string = ""
    for line in input:
        line = line.strip()
        if line == "":
            continue

        if value_as_string != "" and is_valid:
            values.append(int(value_as_string))

        value_as_string = ""
        is_valid = False
        for column, character in enumerate(line):
            if character.isnumeric():
                value_as_string += character
                if is_valid_matrix[column][row]:
                    is_valid = True
            elif not character.isnumeric() and value_as_string != "" and is_valid:
                values.append(int(value_as_string))
                value_as_string = ""
                is_valid = False
            else:
                value_as_string = ""
                is_valid = False

        row += 1
    return sum(values)

def part2(input_raw):
    input = [line.strip() for line in input_raw if line.strip() != ""]
    symbols = {}
    visited = {}
    sum = 0

    for row, line in enumerate(input):
        for column, character in enumerate(line):
            if not character.isnumeric() and character != ".":
                symbols["x" + str(column) + "y" + str(row)] = {"character": character, "parts": find_connected_parts(input, column, row, visited)}

    for key, value in symbols.items():
        if value["character"] == "*" and len(value["parts"]) == 2:
            sum += numpy.prod(value["parts"])
    return sum

def find_connected_parts(input, column, row, visited):
    parts = []
    directions = [
        {"column": column - 1, "row": row - 1},
        {"column": column, "row": row - 1},
        {"column": column + 1, "row": row - 1},
        {"column": column - 1, "row": row},
        {"column": column + 1, "row": row},
        {"column": column - 1, "row": row + 1},
        {"column": column, "row": row + 1},
        {"column": column + 1, "row": row + 1 }
    ]

    for direction in directions:
        if direction["column"] < 0 or direction["row"] < 0 or direction["column"] >= len(input[0]) or direction["row"] >= len(input):
            continue
        if input[direction["row"]][direction["column"]].isnumeric():
            part = get_part_number(input, direction["column"], direction["row"], visited)
            if part != -1:
                parts.append(part)
    return parts

def get_part_number(input, column, row, visited):
    if visited.get("x" + str(column) + "y" + str(row)) is not None:
        return -1
    x, y = column, row
    part_number = ""
    while x > 0 and input[y][x-1].isnumeric():
        x -= 1
    while x < len(input) and input[y][x].isnumeric():
        part_number += input[y][x]
        visited["x" + str(x) + "y" + str(y)] = True
        x += 1
    return int(part_number)

def mark_valid(matrix, column, row):
    # Mark self
    matrix[column][row] = True
    # Mark left
    matrix[max(column - 1, 0)][row] = True
    # Mark up
    matrix[column][max(row - 1, 0)] = True
    # Mark right
    matrix[min(column + 1, len(matrix[0]))][row] = True
    # Mark down
    matrix[column][min(row + 1, len(matrix))] = True
    # Mark diagonals
    matrix[max(column - 1, 0)][max(row - 1, 0)] = True
    matrix[max(column - 1, 0)][min(row + 1, len(matrix))] = True
    matrix[min(column + 1, len(matrix[0]))][max(row - 1, 0)] = True
    matrix[min(column + 1, len(matrix[0]))][min(row + 1, len(matrix))] = True

if __name__ == "__main__":
    main()
