#!/usr/bin/env python3
import re

from python.utils import aoc


def main():
    # Preparations
    aoc.setup(2023, 2)

    # Sample 1
    sample_input_1 = """
            Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
            """
    aoc.print_answer("1 - Sample", part1(sample_input_1.splitlines()))

    # Part 1
    input = aoc.get_input()
    part1_answer = part1(input)
    aoc.print_answer(1, part1_answer)
    # aoc.submit_answer(1, part1_answer)

    # Sample 2
    sample_input_2 = """
            Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
            """
    aoc.print_answer("2 - Sample", part2(sample_input_2.splitlines()))

    # Part 2
    input = aoc.get_input().readlines()
    part2_answer = part2(input)
    aoc.print_answer(2, part2_answer)
    # aoc.submit_answer(2, part2_answer)


def part1(input):
    res = []
    limits = {"red": 12, "green": 13, "blue": 14}
    regex = r"(?:\w+ (\d+): )*?(\d+) (\w+)"
    for line in input:
        line = line.strip()
        if line == "":
            continue

        matches = re.findall(regex, line)
        match_id = matches[0][0]
        valid_game = True
        for match in matches:
            if int(match[1]) > int(limits[match[2]]):
                valid_game = False
                break
        if valid_game:
            res.append(int(match_id))
    return sum(res)


def part2(input):
    res = []
    regex = r".*?(\d+) (\w+)"
    for line in input:
        limits = {"red": 0, "green": 0, "blue": 0}
        line = line.strip()
        if line == "":
            continue

        matches = re.findall(regex, line)
        for match in matches:
            limits[match[1]] = max(int(match[0]), int(limits[match[1]]))
        res.append(limits["red"] * limits["green"] * limits["blue"])
    return sum(res)


if __name__ == "__main__":
    main()
