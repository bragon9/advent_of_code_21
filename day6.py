from typing import List

REPRODUCTIVE_CYCLE_LENGTH = 6
CYCLES_TO_SEXUAL_MATURITY = 2

def get_input(file_location: str, sample: bool = False) -> List[str]:
    """Pass in a file path and it will read lines."""

    if sample:
        file_name = file_location.split('.txt')[0]
        file_location = f'{file_name}_sample.txt'

    with open(f'{file_location}') as input_file:
        return input_file.read().splitlines()

class Fish:
    """A fish."""

    def __init__(self, timer) -> None:
        self.timer = timer

    def age(self) -> bool:
        """Age 1 cycle.  Return a bool if a new fish is spawned."""

        self.timer -= 1

        if self.timer < 0:
            self.timer = REPRODUCTIVE_CYCLE_LENGTH
            return True

        return False

    def __repr__(self) -> str:
        return f'Fish with timer {self.timer}'

class School:
    """A school of fish."""

    def __init__(self) -> None:
        self.fish = []

    def add_fish(self, fish: Fish) -> None:
        self.fish.append(fish)

    def cycle(self, n: int) -> None:
        """Simulate time for n cycles."""

        for _ in range(n):
            num_births = 0

            for fish in self.fish:
                reproduce = fish.age()

                if reproduce:
                    num_births += 1

            for _ in range(num_births):
                self.fish.append(
                    Fish(REPRODUCTIVE_CYCLE_LENGTH + CYCLES_TO_SEXUAL_MATURITY))

    def __str__(self) -> str:
        return f'{len(self.fish)} fish in school.'

def initialize_school(INPUT: List[str]) -> School:
    """Return a school of fishes created from the given input."""

    current_fish_cycles = [int(x) for x in INPUT[0].split(',')]

    school = School()

    for num in current_fish_cycles:
        school.add_fish(Fish(num))

    return school

if __name__ == '__main__':
    INPUT = get_input('./inputs/day6.txt')
    school = initialize_school(INPUT)
    school.cycle(80)
    print(school)
