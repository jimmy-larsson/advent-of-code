#!/usr/bin/env python3

from python.utils import aoc

def main():
    # Preparations
    aoc.setup(2023, 1)

    # Sample 1
    sample_input_1 = """
            1abc2
            pqr3stu8vwx
            a1b2c3d4e5f
            treb7uchet
            """
    aoc.print_answer("1 - Sample", part1(sample_input_1.splitlines()))


    # Part 1
    input = aoc.get_input()
    part1_answer = part1(input)
    aoc.print_answer(1, part1_answer)
    # aoc.submit_answer(1, part1_answer)


    # Sample 2
    sample_input_2 = """
            two1nine
            eightwothree
            abcone2threexyz
            xtwone3four
            4nineeightseven2
            zoneight234
            7pqrstsixteen
            """
    aoc.print_answer("2 - Sample", part2(sample_input_2.splitlines()))


    # Part 2
    input = aoc.get_input().readlines()
    part2_answer = part2(input)
    aoc.print_answer(2, part2_answer)
    # aoc.submit_answer(2, part2_answer)

def part1(input):
    first = None
    last = None
    values = []
    for line in input:
        line = line.strip()

        if line == "":
            continue

        for character in line:
            if character.isnumeric():
                if first is None:
                    first = character
                last = character

        value = first + last
        values.append(int(value))
        first = None
        last = None

    return sum(values)

def part2(input):
    lines = []
    dict = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n",
            "eight": "e8t", "nine": "n9e", "zero": "z0o"}

    for line in input:
        if line.strip() == "":
            continue

        lines.append(replace_all(line, dict))

    return part1(lines)

def replace_all(text, dict):
    for i, j in dict.items():
        text = text.replace(i, j)
    return text

if __name__ == "__main__":
    main()
