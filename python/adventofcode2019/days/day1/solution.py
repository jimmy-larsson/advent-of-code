def read_input(file_path: str):
    with open(file_path, "r") as file:
        return [int(line) for line in file.readlines()]


def part1(inputs: list):
    return sum([(mass // 3 - 2) for mass in inputs])


def part2(inputs: list):
    mass_total = 0
    for mass in inputs:
        module_total_mass = 0

        fuel_mass = calculate_fuel_cost_from_mass(mass)
        while fuel_mass > 0:
            module_total_mass += fuel_mass
            fuel_mass = calculate_fuel_cost_from_mass(fuel_mass)

        mass_total += module_total_mass

    return mass_total


def calculate_fuel_cost_from_mass(mass: int):
    return mass // 3 - 2


if __name__ == "__main__":
    print(f"Part 1: {part1(read_input('input_part1.txt'))}")
    print(f"Part 2: {part2(read_input('input_part2.txt'))}")
