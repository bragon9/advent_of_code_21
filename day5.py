from collections import defaultdict
from typing import Dict, List, Tuple

def get_input(file_location: str, sample: bool = False) -> List[str]:
    """Pass in a file path and it will read lines."""

    if sample:
        file_name = file_location.split('.txt')[0]
        file_location = f'{file_name}_sample.txt'

    with open(f'{file_location}') as input_file:
        return input_file.read().splitlines()

def build_overlap_chart(INPUT: List[str]) -> Dict[Tuple[int, int], int]:
    """Given an input build a dictionary with the overlap."""

    overlap_dict = defaultdict(int)

    for line in INPUT:
        start, stop = line.split(' -> ')
        x1, y1 = [int(x) for x in start.split(',')]
        x2, y2 = [int(x) for x in stop.split(',')]

        # Vertical.
        if x1 == x2:
            y_min, y_max = min(y1, y2), max(y1, y2)
            for i in range(y_min, y_max+1):
                coords = tuple([x1, i])
                overlap_dict[coords] += 1
        # horizontal
        elif y1 == y2:
            x_min, x_max = min(x1, x2), max(x1, x2)
            for i in range(x_min, x_max+1):
                coords = tuple([i, y1])
                overlap_dict[coords] += 1
        # Only count straight lines
        else:
            continue

    return overlap_dict

def spots_with_min_density(chart: Dict[Tuple[int, int], int],\
                           min_density) -> int:
    """Given a chart return spots over a given density."""

    count = 0

    for coord, density in chart.items():
        if density >= min_density:
            count += 1

    return count

if __name__ == '__main__':
    INPUT = get_input('./inputs/day5.txt')
    chart = build_overlap_chart(INPUT)
    minimum_overlap = 2
    answer = spots_with_min_density(chart, minimum_overlap)

    print(f'{answer} locations with a minimum density of {minimum_overlap}.')
