package com.jimmylarsson.adventofcode2019;

import com.jimmylarsson.adventofcode2019.common.Day;

import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws InstantiationException, IllegalAccessException, ClassNotFoundException, IOException, InvocationTargetException, NoSuchMethodException {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Which day would you like to run? ");
        int day = scanner.nextInt();

        System.out.println("Running day " + day + ":");
        Day instance = (Day) Class.forName("com.jimmylarsson.adventofcode2019.days.Day" + day).getDeclaredConstructor().newInstance();
        instance.printAllParts();
        System.out.println();

    }
}
