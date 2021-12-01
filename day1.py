from typing import List

def get_input(file_location: str):
    """Pass in a file path and it will read lines into integers."""
    with open(f'{file_location}') as input_file:
        return[int(x) for x in input_file]

def count_increases(nums_arr: List[int]) -> int:
    """Takes a list of numbers and counts the times a num > prev num."""
    increases = 0
    for i in range(1, len(nums_arr)):
        if nums_arr[i] > nums_arr[i-1]:
            increases += 1
    return increases

if __name__ == '__main__':
    INPUT = get_input('./inputs/day1.txt')
    print(count_increases(INPUT))
