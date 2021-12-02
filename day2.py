from typing import List

FORWARD = 'forward'
UP = 'up'
DOWN = 'down'

def get_input(file_location: str):
    """Pass in a file path and it will read direction and distance."""

    with open(f'{file_location}') as input_file:
        return input_file.read().splitlines()

class Submarine:
    """Class to represent a submarine."""

    def __init__(self):
        self.x = 0
        self.y = 0
        self.aim = 0

    def travel_route(self, route: List[str]) -> None:
        """Input is a route, outputs the final x and y coordinates."""

        for instruction in route:
            direction, amount = instruction.split()
            amount = int(amount)

            if direction == FORWARD:
                self.forward(amount)
            elif direction == UP:
                self.up(amount)
            elif direction == DOWN:
                self.down(amount)

        return self.x, self.y

    def forward(self, distance: int) -> None:
        self.x += distance
        self.y += self.aim * distance

    def up(self, degrees: int) -> None:
        self.aim -= degrees

    def down(self, degrees: int) -> None:
        self.aim += degrees

if __name__ == '__main__':
    INPUT = get_input('./inputs/day2.txt')
    sub = Submarine()
    x, y = sub.travel_route(INPUT)
    print(f'final coordinates: ({x}, {y}). Answer={x*y}')
