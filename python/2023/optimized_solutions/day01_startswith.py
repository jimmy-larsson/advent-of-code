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
    score = 0
    for line in input:
        line = line.strip()
        if line == "":
            continue

        digits = []
        for character in line:
            if character.isnumeric():
                digits.append(character)

        score += int(digits[0] + digits[-1])
    return score


def part2(input):
    score = 0
    for line in input:
        line = line.strip()
        if line == "":
            continue

        digits = []
        for character_index, character in enumerate(line):
            if character.isnumeric():
                digits.append(character)
                continue

            for digit_index, digit in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if line[character_index:].startswith(digit):
                    digits.append(str(digit_index + 1))
                    break

        score += int(digits[0] + digits[-1])
    return score


if __name__ == "__main__":
    main()
