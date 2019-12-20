package main

import (
	"fmt"
	"strconv"

	"../../fileutils"
)

func main() {
	solveAllParts()
}

func part1(inputOverride []int, filepath string) int {
	var inputs []int
	if inputOverride != nil {
		inputs = inputOverride
	} else {
		inputs = fileutils.ReadInts(filepath)
	}

	sum := 0
	for _, value := range inputs {
		sum += (value / 3) - 2
	}

	return sum
}

func part2(inputOverride []int, filepath string) int {
	return 0
}

func solvePart1() {
	fmt.Println("Part 1: " + strconv.Itoa(part1(nil, "src/2019/day1/input_part1.txt")))
}

func solvePart2() {
	fmt.Println("Part 2: " + strconv.Itoa(part2(nil, "src/2019/day1/input_part2.txt")))
}

func solveAllParts() {
	solvePart1()
	solvePart2()
}
