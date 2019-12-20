package fileutils

import (
	"bufio"
	"os"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func openFile(filepath string) *os.File {
	file, err := os.Open(filepath)
	check(err)

	return file
}

func ReadLines(filepath string) []string {
	file := openFile(filepath)


	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	var lines []string
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	defer file.Close()
	return lines
}

func ReadInts(filepath string) []int {
	file := openFile(filepath)

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanWords)

	var ints []int
	for scanner.Scan() {
		value, error := strconv.Atoi(scanner.Text())
		check(error)
		ints = append(ints, value)
	}

	defer file.Close()
	return ints
}
