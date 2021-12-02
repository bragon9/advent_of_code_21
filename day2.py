from typing import List

FORWARD = 'forward'
UP = 'up'
DOWN = 'down'

def get_input(file_location: str):
    """Pass in a file path and it will read direction and distance."""

    with open(f'{file_location}') as input_file:
        return input_file.read().splitlines()

def parse_input():
    pass

class Submarine:
    """Class to represent a submarine."""

    def __init__(self):
        self.x = 0
        self.y = 0

    def travel_route(self, route: List[str]) -> None:
        """Input is a route, outputs the final x and y coordinates."""

        for instruction in route:
            direction, distance = instruction.split()
            distance = int(distance)

            if direction == FORWARD:
                self.forward(distance)
            elif direction == UP:
                self.up(distance)
            elif direction == DOWN:
                self.down(distance)

        return self.x, self.y

    def forward(self, distance: int) -> None:
        self.x += distance

    def up(self, distance: int) -> None:
        self.y -= distance

    def down(self, distance: int) -> None:
        self.y += distance

if __name__ == '__main__':
    INPUT = get_input('./inputs/day2.txt')
    sub = Submarine()
    x, y = sub.travel_route(INPUT)
    print(x * y)
