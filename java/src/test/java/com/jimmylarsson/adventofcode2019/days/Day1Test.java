package com.jimmylarsson.adventofcode2019.days;

import org.junit.Assert;
import org.junit.Test;

import java.io.IOException;
import java.util.Optional;

public class Day1Test {

    @Test
    public void part1ProblemExampleReturnsCorrectValue() throws IOException {
        Assert.assertEquals(33583, new Day1().part1(Optional.of(new String[]{"100756"})));
    }

    @Test
    public void part2ProblemExampleReturnsCorrectValue() throws IOException {
        Assert.assertEquals(50346, new Day1().part2(Optional.of(new String[]{"100756"})));
    }
}