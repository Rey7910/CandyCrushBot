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
        '''
            0. Up
            1. Down
            2. Left
            3. Right
        '''
        self.dy = (-1, 1, 0, 0)
        self.dy = (0, 0, -1, 1)
        self.basic = (0, 0)

    def solve(self, board: list, specialLocs: tuple = ()) -> tuple:
        # Initializes the internal check board
        for r in range(9):
            for c in range(9):
                self.checkBoard[r][c] = False

    def checkSpecial(self, r: int, c: int, board: list) -> tuple:
        for i in range(4):
            nr = r + self.dy[i]
            nc = c + self.dx[i]

            if nr >= 0 and nr < 9 and nc >= 0 and nc < 9:
                if board[nr][nc] >= 10:
                    return (self.dy[i], self.dx[i])

        return ()

    def checkBasic(self, r: int, c: int, kind: int, board: list) -> tuple:
        # Up
        nr = r-1
        nc = c
        if nr >= 0 and nr < 9 and nc >= 0 and nc < 9:
            if nc-1 >= 0 and \
               board[nr][nc-1] % 10 == kind % 10 and \
               nc+1 < 9 and \
               board[nr][nc+1] % 10 == kind % 10:
                if kind >= 10:
                    return (-1, 0)

                self.basic = (-1, 0)

        # Down
        nr = r+1
        nc = c
        if nr >= 0 and nr < 9 and nc >= 0 and nc < 9:
            if nc-1 >= 0 and \
               board[nr][nc-1] % 10 == kind % 10 and \
               nc+1 < 9 and \
               board[nr][nc+1] % 10 == kind % 10:
                if kind >= 10:
                    return (1, 0)

                self.basic = (1, 0)

        # Left
        nr = r
        nc = c-1
        if nr >= 0 and nr < 9 and nc >= 0 and nc < 9:
            if nr-1 >= 0 and \
               board[nr-1][nc] % 10 == kind % 10 and \
               nr+1 < 9 and \
               board[nr+1][nc] % 10 == kind % 10:
                if kind >= 10:
                    return (0, -1)

                self.basic = (0, -1)

        return ()
