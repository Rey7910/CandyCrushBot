ORANGE = 0
BLUE = 1
RED = 2
PURPLE = 3
YELLOW = 4
GREEN = 5

LINE_ORANGE = 10
LINE_BLUE = 11
LINE_RED = 12
LINE_PURPLE = 13
LINE_YELLOW = 14
LINE_GREEN = 15

BOOM_ORANGE = 20
BOOM_BLUE = 21
BOOM_RED = 22
BOOM_PURPLE = 23
BOOM_YELLOW = 24
BOOM_GREEN = 25

CHOCO = 66


class BoardSolver:
    def __init__(self) -> None:
        self.board = []
        self.checkBoard = [[False for c in range(9)] for r in range(9)]
        '''
            0. Up
            1. Down
            2. Left
            3. Right
        '''
        self.dy = (-1, 1, 0, 0)
        self.dx = (0, 0, -1, 1)
        self.basic = [(), ()]

    def solve(self, board: list, specialLocs: list = ()) -> tuple:
        # Initializes the internal check board
        self.board = board
        for r in range(9):
            for c in range(9):
                self.checkBoard[r][c] = False

        # Checks the special candies
        for specialLoc in specialLocs:
            movement = self.checkSpecial(specialLoc[0], specialLoc[1])
            if movement != ():
                return movement

            if self.basic[0] == ():
                self.checkBasic(specialLoc[0], specialLoc[1],
                                self.board[specialLoc[0]][specialLoc[1]])

            self.checkBoard[specialLoc[0]][specialLoc[1]] = True

            # Checks in the surroundings of the special candy
            self.searchZone(specialLoc[0], specialLoc[1])

        # Checks the rest of the board
        for nr in range(9):
            for nc in range(9):
                if not self.checkBoard[nr][nc]:

                    if self.basic[1] == ():
                        self.checkBasic(nr, nc, self.board[nr][nc])

        # Returns a basic movement if there's no better option
        if self.basic[0] != ():
            return self.basic[0]
        return self.basic[1]

    def checkBasic(self, r: int, c: int, kind: int) -> None:
        if self.checkBasic1(r, c, kind):
            pass
        elif self.checkBasic2(r, c, kind):
            pass
        elif self.checkBasic3(r, c, kind):
            pass
        elif self.checkBasic4(r, c, kind):
            pass

    def checkChoco(self, r: int, c: int, kind: int) -> tuple:
        ckind = kind % 10

        # Up
        nr = r-1
        nc = c
        if (nr >= 0 and nr):
            pass

    def searchZone(self, r: int, c: int) -> tuple:
        cornerR = r-2
        cornerC = c-2

        for i in range(9):
            sr = cornerR+i

            if sr >= 0 and sr < 9:
                for j in range(9):
                    sc = cornerC+j

                    if sc >= 0 and sc < 9 and not self.checkBoard[sr][sc]:
                        if self.basic[1] == ():
                            self.checkBasic(sr, sc, self.board[sr][sc])

                        self.checkBoard[sr][sc] = True

    def checkSpecial(self, r: int, c: int) -> tuple:
        for i in range(4):
            nr = r + self.dy[i]
            nc = c + self.dx[i]

            if nr >= 0 and nr < 9 and nc >= 0 and nc < 9:
                if self.board[nr][nc] >= 10:
                    return ((r, c), (self.dy[i], self.dx[i]))

        return ()

    def checkBasic3(self, r: int, c: int, kind: int) -> bool:
        ckind = kind % 10

        # Up
        nr = r-1
        nc = c
        if nr >= 0:
            if (nc-1 >= 0 and
                    self.board[nr][nc-1] % 10 == ckind and
                    nc+1 < 9 and
                    self.board[nr][nc+1] % 10 == ckind):
                if kind >= 10:
                    self.basic[0] = ((r, c), (-1, 0))

                self.basic[1] = ((r, c), (-1, 0))

                return True

        # Down
        nr = r+1
        nc = c
        if nr < 9:
            if (nc-1 >= 0 and
                    self.board[nr][nc-1] % 10 == ckind and
                    nc+1 < 9 and
                    self.board[nr][nc+1] % 10 == ckind):
                if kind >= 10:
                    self.basic[0] = ((r, c), (1, 0))

                self.basic[1] = ((r, c), (1, 0))

                return True

        # Left
        nr = r
        nc = c-1
        if nc >= 0:
            if (nr-1 >= 0 and
                    self.board[nr-1][nc] % 10 == ckind and
                    nr+1 < 9 and
                    self.board[nr+1][nc] % 10 == ckind):
                if kind >= 10:
                    self.basic[0] = ((r, c), (0, -1))

                self.basic[1] = ((r, c), (0, -1))

                return True

        # Right
        nr = r
        nc = c+1
        if nc < 9:
            if (nr-1 >= 0 and
                    self.board[nr-1][nc] % 10 == ckind and
                    nr+1 < 9 and
                    self.board[nr+1][nc] % 10 == ckind):
                if kind >= 10:
                    self.basic[0] = ((r, c), (0, 1))

                self.basic[1] = ((r, c), (0, 1))

                return True

    def checkBasic2(self, r: int, c: int, kind: int) -> bool:
        ckind = kind % 10

        # Up
        nr = r-1
        nc = c
        if nr >= 0:
            if (nc-2 >= 0 and
                    self.board[nr][nc-2] % 10 == ckind and
                    self.board[nr][nc-1] % 10 == ckind):
                if kind >= 10:
                    self.basic[0] = ((r, c), (-1, 0))

                self.basic[1] = ((r, c), (-1, 0))

                return True

        # Down
        nr = r+1
        nc = c
        if nr < 9:
            if (nc+2 < 9 and
                    self.board[nr][nc+1] % 10 == ckind and
                    self.board[nr][nc+2] % 10 == ckind):
                if kind >= 10:
                    self.basic[0] = ((r, c), (1, 0))

                self.basic[1] = ((r, c), (1, 0))

                return True

        # Left
        nr = r
        nc = c-1
        if nc >= 0:
            if (nr+2 < 9 and
                    self.board[nr+2][nc] % 10 == ckind and
                    self.board[nr+1][nc] % 10 == ckind):
                if kind >= 10:
                    self.basic[0] = ((r, c), (0, -1))

                self.basic[1] = ((r, c), (0, -1))

                return True

        # Right
        nr = r
        nc = c+1
        if nc < 9:
            if (nr-2 >= 0 and
                    self.board[nr-2][nc] % 10 == ckind and
                    self.board[nr-1][nc] % 10 == ckind):
                if kind >= 10:
                    self.basic[0] = ((r, c), (0, 1))

                self.basic[1] = ((r, c), (0, 1))

                return True

    def checkBasic1(self, r: int, c: int, kind: int) -> bool:
        ckind = kind % 10

        # Up
        nr = r-1
        nc = c
        if nr >= 0:
            if (nc+2 < 9 and
                    self.board[nr][nc+2] % 10 == ckind and
                    self.board[nr][nc+1] % 10 == ckind):
                if kind >= 10:
                    self.basic[0] = ((r, c), (-1, 0))

                self.basic[1] = ((r, c), (-1, 0))

                return True

        # Down
        nr = r+1
        nc = c
        if nr < 9:
            if (nc-2 >= 0 and
                    self.board[nr][nc-1] % 10 == ckind and
                    self.board[nr][nc-2] % 10 == ckind):
                if kind >= 10:
                    self.basic[0] = ((r, c), (1, 0))

                self.basic[1] = ((r, c), (1, 0))

                return True

        # Left
        nr = r
        nc = c-1
        if nc >= 0:
            if (nr-2 >= 0 and
                    self.board[nr-2][nc] % 10 == ckind and
                    self.board[nr-1][nc] % 10 == ckind):
                if kind >= 10:
                    self.basic[0] = ((r, c), (0, -1))

                self.basic[1] = ((r, c), (0, -1))

                return True

        # Right
        nr = r
        nc = c+1
        if nc < 9:
            if (nr+2 < 9 and
                    self.board[nr+2][nc] % 10 == ckind and
                    self.board[nr+1][nc] % 10 == ckind):
                if kind >= 10:
                    self.basic[0] = ((r, c), (0, 1))

                self.basic[1] = ((r, c), (0, 1))

                return True

    def checkBasic4(self, r: int, c: int, kind: int) -> bool:
        ckind = kind % 10

        # Up
        nr = r-1
        nc = c
        if nr >= 0:
            if (nr-2 >= 0 and
                    self.board[nr-2][nc] % 10 == ckind and
                    self.board[nr-1][nc] % 10 == ckind):
                if kind >= 10:
                    self.basic[0] = ((r, c), (-1, 0))

                self.basic[1] = ((r, c), (-1, 0))

                return True

        # Down
        nr = r+1
        nc = c
        if nr < 9:
            if (nr+2 < 9 and
                    self.board[nr+2][nc] % 10 == ckind and
                    self.board[nr+1][nc] % 10 == ckind):
                if kind >= 10:
                    self.basic[0] = ((r, c), (1, 0))

                self.basic[1] = ((r, c), (1, 0))

                return True

        # Left
        nr = r
        nc = c-1
        if nc >= 0:
            if (nc-2 >= 0 and
                    self.board[nr][nc-2] % 10 == ckind and
                    self.board[nr][nc-1] % 10 == ckind):
                if kind >= 10:
                    self.basic[0] = ((r, c), (0, -1))

                self.basic[1] = ((r, c), (0, -1))

                return True

        # Right
        nr = r
        nc = c+1
        if nc < 9:
            if (nc+2 < 9 and
                    self.board[nr][nc+2] % 10 == ckind and
                    self.board[nr][nc+1] % 10 == ckind):
                if kind >= 10:
                    self.basic[0] = ((r, c), (0, 1))

                self.basic[1] = ((r, c), (0, 1))

                return True
