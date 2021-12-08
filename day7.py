from collections import Counter
from statistics import median
from typing import List


def get_input(file_location: str, sample: bool = False) -> List[str]:
    """Pass in a file path and it will read lines."""

    if sample:
        file_name = file_location.split('.txt')[0]
        file_location = f'{file_name}_sample.txt'

    with open(f'{file_location}') as input_file:
        return input_file.read().splitlines()

def calculate_fuel_costs(INPUT: List[str]) -> int:
    """Given an input finds the fuel to move all crabs to median."""

    num_inputs = [int(x) for x in INPUT[0].split(',')]
    optimal_position = median(num_inputs)

    crab_positioning_dict = Counter(num_inputs)

    fuel_costs = 0
    for position, num_crabs in crab_positioning_dict.items():
        fuel_costs += int(abs(position - optimal_position) * num_crabs)

    print(
        f'{fuel_costs} fuel to move all crabs to {optimal_position} position.')

if __name__ == '__main__':
    INPUT = get_input('./inputs/day7.txt')
    calculate_fuel_costs(INPUT)
