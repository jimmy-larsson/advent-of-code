package com.jimmylarsson.adventofcode2019.days;

import com.jimmylarsson.adventofcode2019.common.Day;

import java.io.IOException;
import java.util.Optional;
import java.util.Scanner;

public class Day1 implements Day {

    @Override
    public Object part1(Optional<String[]> customInput) throws IOException {
        Scanner sc = getInputScanner(customInput, "com/jimmylarsson/adventofcode2019/days/day1/input_part1.txt");

        int massTotal = 0;
        while (sc.hasNextLine()) {
            massTotal += calculateFuelCostFromMass(sc.nextInt());
        }

        return massTotal;
    }

    @Override
    public Object part2(Optional<String[]> customInput) throws IOException {
        Scanner sc = getInputScanner(customInput, "com/jimmylarsson/adventofcode2019/days/day1/input_part2.txt");

        int massTotal = 0;
        while (sc.hasNextLine()) {
            int moduleTotalMass = 0;

            int fuelMass = calculateFuelCostFromMass(sc.nextInt());
            while (fuelMass > 0) {
                moduleTotalMass += fuelMass;
                fuelMass = calculateFuelCostFromMass(fuelMass);
            }

            massTotal += moduleTotalMass;
        }

        return massTotal;
    }

    private int calculateFuelCostFromMass(int mass) {
        return Math.floorDiv(mass, 3) - 2;
    }
}
