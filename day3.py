from typing import List, Tuple

def get_input(file_location: str):
    """Pass in a file path and it will read lines."""

    with open(f'{file_location}') as input_file:
        return input_file.read().splitlines()

def calculate_rates(input_arr: List[str]) -> Tuple[int, int]:
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

if __name__ == '__main__':
    INPUT = get_input('./inputs/day3.txt')
    gamma_rate, epsilon_rate = calculate_rates(INPUT)

    print(f'gamma={gamma_rate}, '
          f'epsilon={epsilon_rate}, '
          f'power={gamma_rate*epsilon_rate}')
