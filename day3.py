from typing import List, Tuple

CO2 = 'CO2'
OXYGEN = 'OXYGEN'

FORMULAS = (CO2, OXYGEN)

def get_input(file_location: str):
    """Pass in a file path and it will read lines."""

    with open(f'{file_location}') as input_file:
        return input_file.read().splitlines()

def calculate_power_rates(input_arr: List[str]) -> Tuple[int, int]:
    """Take an input array and return the gamma (most frequent) and epsilon
    (least frequent) rate."""

    # This array will be keep track of the most frequent and least frequent
    # bits.  The index will be incremented each time a '1' is seen and
    # decremented each time a 0 is seen.  The index will be positive if there
    # are more 1's than 0's and negative if more 0's than 1's.
    bit_arr = [0] * len(input_arr[0])

    for line in input_arr:
        for index, value in enumerate(line):
            if value == '1':
                bit_arr[index] += 1
            else:
                bit_arr[index] -= 1

    gamma_rate_binary = []
    epsilon_rate_binary = []

    # Epsilon rate is NOT of gamma rate.
    for num in bit_arr:
        if num > 0:
            gamma_rate_binary.append('1')
            epsilon_rate_binary.append('0')
        else:
            gamma_rate_binary.append('0')
            epsilon_rate_binary.append('1')

    gamma_rate_binary = ''.join(gamma_rate_binary)
    epsilon_rate_binary = ''.join(epsilon_rate_binary)

    return (int(gamma_rate_binary, 2), int(epsilon_rate_binary, 2))

def calculate_life_support(input_arr: List[str], formula: str) -> int:
    """Take an input array and return the rating for the requested formula."""

    if formula not in FORMULAS:
        raise ValueError('Invalid formula.')

    arr = input_arr.copy()
    value_length = len(arr[0])

    for i in range(value_length):
        ones_arr = []
        zeroes_arr = []
        frequency = 0

        for value in arr:
            if value[i] == '1':
                ones_arr.append(value)
                frequency += 1
            else:
                zeroes_arr.append(value)
                frequency -= 1

        # If formula is oxygen, use most common value. CO2 uses least common.
        if frequency >= 0:
            if formula == OXYGEN:
                arr = ones_arr
            else:
                arr = zeroes_arr
        else:
            if formula == OXYGEN:
                arr = zeroes_arr
            else:
                arr = ones_arr

        if len(arr) == 1:
            return int(arr[0], 2)

if __name__ == '__main__':
    INPUT = get_input('./inputs/day3.txt')
    o2_generator_rating = calculate_life_support(INPUT, OXYGEN)
    co2_scrubber_rating = calculate_life_support(INPUT, CO2)

    print(f'o2={o2_generator_rating}, '
          f'co2={co2_scrubber_rating}, '
          f'life support={o2_generator_rating*co2_scrubber_rating}')
