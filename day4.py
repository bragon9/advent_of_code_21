from typing import List

def get_input(file_location: str, sample: bool = False) -> List[List[str]]:
    """Pass in a file path and it will read lines."""

    if sample:
        file_name = file_location.split('.txt')[0]
        file_location = f'{file_name}_sample.txt'

    with open(f'{file_location}') as input_file:
        return input_file.read().splitlines()

class Board:
    """Representation of a bingo board."""

    def __init__(self) -> None:
        self.rows = []
        # key: number
        # value: (x, y) coords, bool if it has been called
        self.board_dict = {}
        self.called_rows = {i:0 for i in range(5)}
        self.called_cols = {i:0 for i in range(5)}

    def play_number(self, number) -> bool:
        """Play a number.  Returns TRUE if it results in a win."""

        if number in self.board_dict:
            self.board_dict[number][1] = True
            x, y = self.board_dict[number][0]
            self.called_cols[x] += 1
            self.called_rows[y] += 1

            if self.called_cols[x] >= 5 or self.called_rows[y] >= 5:
                return True

        return False

    def add_row(self, row: List[int]) -> None:
        for i in range(5):
            self.board_dict[row[i]] = [(i, len(self.rows)), False]
        self.rows.append(row)

    def score(self) -> int:
        """Score the board (all uncalled numbers) and return value."""

        score = 0
        for num in self.board_dict:
            if self.board_dict[num][1] is False:
                score += num

        return score

    def print_board(self) -> None:
        for row in self.rows:
            print(row)

class Bingo:
    """Bingo game consisting of moves and boards."""

    def __init__(self) -> None:
        self.moves = None
        self.boards = []

    def add_board(self, board: Board) -> None:
        self.boards.append(board)

    def play(self) -> None:
        """Play through the move list one at a time and play that number on
        all of the boards.  Print out the score and stop play when
        there is a winner."""

        for move in self.moves:
            for board_num, board in enumerate(self.boards):

                winner = board.play_number(move)

                if winner is True:
                    score = board.score()
                    print(
                        f'Winner! Board #{board_num+1} with a score of '
                        f'{score}. '
                        '\n'
                        f'{score} * last number called {move} = {score*move}')

                    return

    def print_boards(self):
        for board in self.boards:
            board.print_board()
            print('\n')

def initialize_bingo_game(text_input: List[str]) -> Bingo:
    """Given an input return an initialized Bingo object."""

    bingo_game = Bingo()
    bingo_game.moves = [int(x) for x in text_input[0].split(',')]
    board = None

    for i in range(1, len(text_input)):
        row = text_input[i]
        if row == '':
            if board is not None:
                bingo_game.add_board(board)
            board = Board()
        else:
            int_row = [int(x) for x in text_input[i].strip().split()]
            board.add_row(int_row)

    bingo_game.add_board(board)

    return bingo_game

if __name__ == '__main__':
    INPUT = get_input('./inputs/day4.txt')
    game = initialize_bingo_game(INPUT)
    game.play()
