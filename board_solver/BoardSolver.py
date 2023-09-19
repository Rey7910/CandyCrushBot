ORANGE = 0
BLUE = 1
RED = 2
PURPLE = 3

LINE_ORANGE = 10
LINE_BLUE = 11
LINE_RED = 12
LINE_PURPLE = 13

BOOM_ORANGE = 20
BOOM_BLUE = 21
BOOM_RED = 22
BOOM_PURPLE = 23

CHOCO = 66


class BoardSolver:
    def __init__(self) -> None:
        self.checkBoard = [[False for c in range(9)] for r in range(9)]

    def solve(self, board: list, specialLocs: tuple = ()) -> tuple:
        # Initializes the internal check board
        for r in range(9):
            for c in range(9):
                self.checkBoard[r][c] = False
