from typing import List

# Constants
FORWARD = 'forward'
UP = 'up'
DOWN = 'down'

def get_input(file_location: str):
    """Pass in a file path and it will read lines."""

    with open(f'{file_location}') as input_file:
        return input_file.read().splitlines()

class Submarine:
    """Class to represent a submarine."""

    def __init__(self):
        self.x = 0
        self.y = 0

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

    def forward(self, amount: int) -> None:
        self.x += amount

    def up(self, amount: int) -> None:
        self.y -= amount

    def down(self, amount: int) -> None:
        self.y += amount

class SubmarineMk2(Submarine):
    """New version of submarine with updated movement capability."""

    def __init__(self):
        super().__init__()
        self.aim = 0

    def forward(self, amount: int) -> None:
        self.x += amount
        self.y += self.aim * amount

    def up(self, amount: int) -> None:
        self.aim -= amount

    def down(self, amount: int) -> None:
        self.aim += amount

if __name__ == '__main__':
    INPUT = get_input('./inputs/day2.txt')
    sub = SubmarineMk2()
    x, y = sub.travel_route(INPUT)
    print(f'final coordinates: ({x}, {y}). Answer={x*y}')
