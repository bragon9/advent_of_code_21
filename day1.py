from typing import List

def get_input(file_location: str):
    """Pass in a file path and it will read lines into integers."""

    with open(f'{file_location}') as input_file:
        return [int(x) for x in input_file]

def count_increases(nums_arr: List[int], window_size: int = 1) -> int:
    """Takes a list of numbers a subarray size, and returns the number of times
    that a sliding window is larger than the previous window sum."""

    if len(nums_arr) <= 1:
        return 0

    if window_size >= len(nums_arr):
        raise ValueError('Window size must be less than array length.')

    increases = 0

    # Check if the number being added to the window is greater than the number
    # being removed from the array
    for i in range(window_size, len(nums_arr)):
        if nums_arr[i] > nums_arr[i-window_size]:
            increases += 1
    return increases

if __name__ == '__main__':
    INPUT = get_input('./inputs/day1.txt')
    print(count_increases(INPUT, 3))
