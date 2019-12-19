package com.jimmylarsson.adventofcode2019.common;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Optional;
import java.util.Scanner;

public interface Day {

    Object part1(Optional<String[]> customInput) throws IOException;

    Object part2(Optional<String[]> customInput) throws IOException;

    default void printPart1() throws IOException {
        System.out.println("Part 1: " + part1(Optional.empty()));
    }

    default void printPart2() throws IOException {
        System.out.println("Part 2 : " + part2(Optional.empty()));
    }

    default void printAllParts() throws IOException {
        printPart1();
        printPart2();
    }

    default Scanner getInputScanner(Optional<String[]> customInput, String filePath) throws FileNotFoundException {
        Scanner scanner;

        if (customInput.isPresent()) {
            String outputAsSingleString = String.join("\n", customInput.get());
            scanner = new Scanner(outputAsSingleString);
        } else {
            File file = new File(getClass().getClassLoader().getResource(filePath).getFile());
            scanner = new Scanner(file);
        }

        return scanner;
    }

}
