rows, cols = (8, 8)


class Board:
    def __init__(self, board=None):
        if board is None:
            self.grid = [['-' for i in range(cols)] for j in range(rows)]
            self.grid[3][3] = 'W'
            self.grid[3][4] = 'B'
            self.grid[4][3] = 'B'
            self.grid[4][4] = 'W'
        else:
            self.copyCon(board)

    def copyCon(self, board):
        self.grid = board.grid

    def printBoard(self):
        for i in range(0, 8):
            for j in range(0, 8):
                print(self.grid[i][j], end=" ")
            print('\n')

    def getBoard(self):
        return self


class Othello:
    def __init__(self, o=None):
        if o is None:
            self.board = Board()
        else:
            self.copyCon(o)

    def copyCon(self, o):
        self.board = Board()
        self.board.grid = o.board.grid

    def getPossibleMoves(self, p):
        n = 0
        move_list = []
        if p == 'B':
            for i in range(0, 8):
                for j in range(0, 8):
                    k = 0
                    m = 0
                    if self.board.grid[i][j] == 'B':
                        # check row right
                        if j < 7 and self.board.grid[i][j + 1] == 'W':
                            k = j + 1
                            while self.board.grid[i][k] == 'W' and k < 8:
                                k = k + 1
                                if k > 7:
                                    break
                            if k < 8:
                                if self.board.grid[i][k] != 'B':
                                    move_list.append([i, k])

                        # check row left
                        if j > 0 and self.board.grid[i][j - 1] == 'W':
                            k = j - 1
                            while self.board.grid[i][k] == 'W' and k >= 0:
                                k = k - 1
                                if k < 0:
                                    break
                            if k >= 0:
                                if self.board.grid[i][k] != 'B':
                                    move_list.append([i, k])
                        # check column up
                        if i > 0 and self.board.grid[i - 1][j] == 'W':
                            k = i - 1
                            while self.board.grid[k][j] == 'W' and k >= 0:
                                k = k - 1
                                if k < 0:
                                    break
                            if k >= 0:
                                if self.board.grid[k][j] != 'B':
                                    move_list.append([k, j])
                        # check column down
                        if i < 7 and self.board.grid[i + 1][j] == 'W':
                            k = i + 1
                            while self.board.grid[k][j] == 'W' and k < 8:
                                k = k + 1
                                if k > 7:
                                    break
                            if k < 8:
                                if self.board.grid[k][j] != 'B':
                                    move_list.append([k, j])
                        # check diagonal right up
                        if i > 0 and j < 7 and self.board.grid[i - 1][j + 1] == 'W':
                            m = i - 1
                            k = j + 1
                            while self.board.grid[m][k] == 'W' and k < 8 and m >= 0:
                                k = k + 1
                                m = m - 1
                                if k > 7 or m < 0:
                                    break
                            if k < 8 and m >= 0:
                                if self.board.grid[m][k] != 'B':
                                    move_list.append([m, k])
                        # check diagonal right down
                        if i < 7 and j < 7 and self.board.grid[i + 1][j + 1] == 'W':
                            m = i + 1
                            k = j + 1
                            while self.board.grid[m][k] == 'W' and k < 8 and m < 8:
                                k = k + 1
                                m = m + 1
                                if k > 7 or m > 7:
                                    break
                            if k < 8 and m < 8:
                                if self.board.grid[m][k] != 'B':
                                    move_list.append([m, k])
                        # check diagonal left up
                        if i > 0 and j > 0 and self.board.grid[i - 1][j - 1] == 'W':
                            m = i - 1
                            k = j - 1
                            while self.board.grid[m][k] == 'W' and k >= 0 and m >= 0:
                                k = k - 1
                                m = m - 1
                                if k < 0 or m < 0:
                                    break
                            if k >= 0 and m >= 0:
                                if self.board.grid[m][k] != 'B':
                                    move_list.append([m, k])
                        # check diagonal left down
                        if i < 7 and j > 0 and self.board.grid[i + 1][j - 1] == 'W':
                            m = i + 1
                            k = j - 1
                            while self.board.grid[m][k] == 'W' and k >= 0 and m < 8:
                                k = k - 1
                                m = m + 1
                                if k < 0 or m > 7:
                                    break
                            if k >= 0 and m < 8:
                                if self.board.grid[m][k] != 'B':
                                    move_list.append([m, k])
        else:
            for i in range(0, 8):
                for j in range(0, 8):
                    if self.board.grid[i][j] == 'W':
                        # check row right
                        if j < 7 and self.board.grid[i][j + 1] == 'B':
                            k = j + 1
                            while self.board.grid[i][k] == 'B' and k < 8:
                                k = k + 1
                                if k > 7:
                                    break
                            if k < 8:
                                if self.board.grid[i][k] != 'W':
                                    move_list.append([i, k])
                        # check row left
                        if j > 0 and self.board.grid[i][j - 1] == 'B':
                            k = j - 1
                            while self.board.grid[i][k] == 'B' and k >= 0:
                                k = k - 1
                                if k < 0:
                                    break
                            if k >= 0:
                                if self.board.grid[i][k] != 'W':
                                    move_list.append([i, k])
                        # check column up
                        if i > 0 and self.board.grid[i - 1][j] == 'B':
                            k = i - 1
                            while self.board.grid[k][j] == 'B' and k >= 0:
                                k = k - 1
                                if k < 0:
                                    break
                            if k >= 0:
                                if self.board.grid[k][j] != 'W':
                                    move_list.append([k, j])
                        # check column down
                        if i < 7 and self.board.grid[i + 1][j] == 'B':
                            k = i + 1
                            while self.board.grid[k][j] == 'B' and k < 8:
                                k = k + 1
                                if k > 7:
                                    break
                            if k < 8:
                                if self.board.grid[k][j] != 'W':
                                    move_list.append([k, j])
                        # check diagonal right up
                        if i > 0 and j < 7 and self.board.grid[i - 1][j + 1] == 'B':
                            m = i - 1
                            k = j + 1
                            while self.board.grid[m][k] == 'B' and k < 8 and m >= 0:
                                k = k + 1
                                m = m - 1
                                if m < 0 or k > 7:
                                    break
                            if k < 8 and m >= 0:
                                if self.board.grid[m][k] != 'W':
                                    move_list.append([m, k])

                        # check diagonal right down
                        if i < 7 and j < 7 and self.board.grid[i + 1][j + 1] == 'B':
                            m = i + 1
                            k = j + 1
                            while self.board.grid[m][k] == 'B' and k < 8 and m < 8:
                                k = k + 1
                                m = m + 1
                                if k > 7 or m > 7:
                                    break
                            if k < 8 and m < 8:
                                if self.board.grid[m][k] != 'W':
                                    move_list.append([m, k])

                        # check diagonal left up
                        if i > 0 and j > 0 and self.board.grid[i - 1][j - 1] == 'B':
                            m = i - 1
                            k = j - 1
                            while self.board.grid[m][k] == 'B' and k >= 0 and m >= 0:
                                k = k - 1
                                m = m - 1
                                if k < 0 or m < 0:
                                    break
                            if k >= 0 and m >= 0:
                                if self.board.grid[m][k] != 'W':
                                    move_list.append([m, k])

                        # check diagonal left down
                        if i < 7 and j > 0 and self.board.grid[i + 1][j - 1] == 'B':
                            m = i + 1
                            k = j - 1
                            while self.board.grid[m][k] == 'B' and k >= 0 and m < 8:
                                k = k - 1
                                m = m + 1
                                if k < 0 or m > 7:
                                    break
                            if k >= 0 and m < 8:
                                if self.board.grid[m][k] != 'W':
                                    move_list.append([m, k])

        return move_list

    def evaluatingFunction(self, turn):
        return len(self.getPossibleMoves(turn))

    def setMoveB(self, coordinates):
        f = False
        self.board.grid[coordinates[0]][coordinates[1]] = 'B'

        r = coordinates[0]
        c = coordinates[1] + 1
        # update row right
        if c < 7:
            if self.board.grid[r][c] == 'W':
                for i in range(c + 1, 8):
                    if self.board.grid[r][i] == 'B':
                        f = True
                if f is True:
                    while c < 8 and self.board.grid[r][c] == 'W':
                        self.board.grid[r][c] = 'B'
                        c = c + 1
            f = False
        r = coordinates[0]
        c = coordinates[1] - 1
        # update row left
        if c > 0:
            if self.board.grid[r][c] == 'W':
                for i in range(c - 1, 0):
                    if self.board.grid[r][i] == 'B':
                        f = True
                if f is True:
                    while c >= 0 and self.board.grid[r][c] == 'W':
                        self.board.grid[r][c] = 'B'
                        c = c - 1
            f = False
        r = coordinates[0] - 1
        c = coordinates[1]
        # update column up
        if r > 0:
            if self.board.grid[r][c] == 'W':
                for i in range(r - 1, 0):
                    if self.board.grid[i][c] == 'B':
                        f = True
                if f is True:
                    while r >= 0 and self.board.grid[r][c] == 'W':
                        self.board.grid[r][c] = 'B'
                        r = r - 1
            f = False
        r = coordinates[0] + 1
        c = coordinates[1]
        # update column down
        if r < 7:
            if self.board.grid[r][c] == 'W':
                for i in range(r + 1, 8):
                    if self.board.grid[i][c] == 'B':
                        f = True
                if f is True:
                    while r < 8 and self.board.grid[r][c] == 'W':
                        self.board.grid[r][c] = 'B'
                        r = r + 1
            f = False
        r = coordinates[0] - 1
        c = coordinates[1] + 1
        # update diagonal right up
        if r > 0 and c < 7:
            if self.board.grid[r][c] == 'W':
                m = c + 1
                i = r - 1
                while m < 8 and i >= 0:
                    if self.board.grid[i][m] == 'B':
                        f = True
                    m = m + 1
                    i = i - 1
                if f is True:
                    while r >= 0 and c < 8 and self.board.grid[r][c] == 'W':
                        self.board.grid[r][c] = 'B'
                        r = r - 1
                        c = c + 1
            f = False
        r = coordinates[0] + 1
        c = coordinates[1] + 1
        # update diagonal right bottom
        if r < 7 and c < 7:
            if self.board.grid[r][c] == 'W':
                i = r + 1
                m = c + 1
                while m < 8 and i < 8:
                    if self.board.grid[i][m] == 'B':
                        f = True
                    m = m + 1
                    i = i + 1
                if f is True:
                    while r < 8 and c < 8 and self.board.grid[r][c] == 'W':
                        self.board.grid[r][c] = 'B'
                        c = c + 1
                        r = r + 1
            f = False
        r = coordinates[0] - 1
        c = coordinates[1] - 1
        # update diagonal left up
        if r > 0 and c > 0:
            if self.board.grid[r][c] == 'W':
                i = r - 1
                m = c - 1
                while m >= 0 and i >= 0:
                    if self.board.grid[i][m] == 'B':
                        f = True
                    m = m - 1
                    i = i - 1
                if f is True:
                    while c >= 0 and r >= 0 and self.board.grid[r][c] == 'W':
                        self.board.grid[r][c] = 'B'
                        c = c - 1
                        r = r - 1
            f = False
        r = coordinates[0] + 1
        c = coordinates[1] - 1
        # update diagonal left down
        if r < 7 and c > 0:
            if self.board.grid[r][c] == 'W':
                m = r + 1
                i = c - 1
                while m < 8 and i >= 0:
                    if self.board.grid[m][i] == 'B':
                        f = True
                    m = m + 1
                    i = i - 1
                if f is True:
                    while c >= 0 and r < 8 and self.board.grid[r][c] == 'W':
                        self.board.grid[r][c] = 'B'
                        c = c - 1
                        r = r + 1
            flag = False

    def calculateScore(self):
        countB = 0
        countW = 0
        for i in range(0, 8):
            for j in range(0, 8):
                if self.board.grid[i][j] == 'B':
                    countB = countB + 1
                else:
                    countW = countW + 1
        print(f"User Score:{countB}")
        print(f"Computer Score:{countW}")

    def setmoveW(self, coordinates):
        f = False
        self.board.grid[coordinates[0]][coordinates[1]] = 'W'
        r = coordinates[0]
        c = coordinates[1] + 1
        # update row right
        if c < 8:
            if self.board.grid[r][c] == 'B':

                for i in range(c + 1, 8):

                    if self.board.grid[r][i] == 'W':
                        f = True
                if f is True:

                    while c < 8 and self.board.grid[r][c] == 'B':
                        self.board.grid[r][c] = 'W'
                        c = c + 1
            f = False

        r = coordinates[0]
        c = coordinates[1] - 1
        # update row left
        if c > 0:
            if self.board.grid[r][c] == 'B':
                for i in range(c - 1, 0):
                    if self.board.grid[r][i] == 'W':
                        f = True
                if f is True:
                    while c >= 0 and self.board.grid[r][c] == 'B':
                        self.board.grid[r][c] = 'W'
                        c = c - 1
            f = False
        r = coordinates[0] - 1
        c = coordinates[1]
        # update column up
        if r > 0:
            if self.board.grid[r][c] == 'B':
                for i in range(r - 1, 0):
                    if self.board.grid[i][c] == 'W':
                        f = True
                if f is True:
                    while r >= 0 and self.board.grid[r][c] == 'B':
                        self.board.grid[r][c] = 'W'
                        r = r - 1
            f = False
        r = coordinates[0] + 1
        c = coordinates[1]
        # update column down
        if r < 8:
            if self.board.grid[r][c] == 'B':
                for i in range(r + 1, 8):
                    if self.board.grid[i][c] == 'W':
                        f = True
                if f is True:
                    while r < 8 and self.board.grid[r][c] == 'B':
                        self.board.grid[r][c] = 'W'
                        r = r + 1
            f = False
        r = coordinates[0] - 1
        c = coordinates[1] + 1
        # update diagonal right up
        if r > 0 and c < 8:
            if self.board.grid[r][c] == 'B':
                m = c + 1
                i = r - 1
                while m < 8 and i >= 0:
                    if self.board.grid[i][m] == 'W':
                        f = True
                    m = m + 1
                    i = i - 1
                if f is True:
                    while r >= 0 and c < 8 and self.board.grid[r][c] == 'B':
                        self.board.grid[r][c] = 'W'
                        r = r - 1
                        c = c + 1
            f = False
        r = coordinates[0] + 1
        c = coordinates[1] + 1
        # update diagonal right bottom
        if r < 8 and c < 8:
            if self.board.grid[r][c] == 'B':
                i = r + 1
                m = c + 1
                while m < 8 and i < 8:
                    if self.board.grid[i][m] == 'W':
                        f = True
                    m = m + 1
                    i = i + 1
                if f is True:
                    while r < 8 and c < 8 and self.board.grid[r][c] == 'B':
                        self.board.grid[r][c] = 'W'
                        c = c + 1
                        r = r + 1
            f = False
        r = coordinates[0] - 1
        c = coordinates[1] - 1
        # update diagonal left up
        if r > 0 and c > 0:
            if self.board.grid[r][c] == 'B':
                i = r - 1
                m = c - 1
                while m >= 0 and i >= 0:
                    if self.board.grid[i][m] == 'W':
                        f = True
                    m = m - 1
                    i = i - 1
                if f is True:
                    while c >= 0 and r >= 0 and self.board.grid[r][c] == 'B':
                        self.board.grid[r][c] = 'W'
                        c = c - 1
                        r = r - 1
            f = False
        r = coordinates[0] + 1
        c = coordinates[1] - 1
        # update diagonal left down
        if r < 8 and c > 0:
            if self.board.grid[r][c] == 'B':
                m = r + 1
                i = c - 1
                while m < 8 and i >= 0:
                    if self.board.grid[m][i] == 'W':
                        f = True
                    m = m + 1
                    i = i - 1
                if f is True:
                    while c >= 0 and r < 8 and self.board.grid[r][c] == 'B':
                        self.board.grid[r][c] = 'W'
                        c = c - 1
                        r = r + 1
            flag = False

    def minMax(self, o, turn, move, l):
        if l == 2:
            val = 1000
            moves = o.getPossibleMoves('W')
            for x in moves:
                otemp = Othello()
                for i in range(0, 8):
                    for j in range(0, 8):
                        otemp.board.grid[i][j] = o.board.grid[i][j]
                otemp.setmoveW(x)
                val = min(otemp.evaluatingFunction('B'), val)
                if val == otemp.evaluatingFunction('B'):
                    move = x
            return [val, move]

        if turn == 'W':
            eval = 1000
            cur_mov = []
            moves = o.getPossibleMoves('W')
            for x in moves:
                move = x
                otemp = Othello()
                for i in range(0, 8):
                    for j in range(0, 8):
                        otemp.board.grid[i][j] = o.board.grid[i][j]
                otemp.setmoveW(x)
                eval = min(self.minMax(otemp, 'B', move, l + 1)[0], eval)
                if eval == self.minMax(otemp, 'B', move, l + 1)[0]:
                    move = (x)
            return [eval, move]
        else:
            eval = 0
            cur_mov = []
            moves = o.getPossibleMoves('B')
            for x in moves:
                otemp = Othello()
                for i in range(0, 8):
                    for j in range(0, 8):
                        otemp.board.grid[i][j] = o.board.grid[i][j]
                otemp.setMoveB(x)
                eval = max(self.minMax(otemp, 'W', move, l + 1)[0], eval)
                if eval == self.minMax(otemp, 'W', move, l + 1)[0]:
                    move = x
            return [eval, move]

    def takeWhiteTurn(self):
        cur_mov = []
        cur_mov = self.minMax(self, 'W', cur_mov, 0)
        self.setmoveW(cur_mov[1])


choice = input(print("Hello! Click any button to play 'Othello'"))
o = Othello()
turn = 'B'
f = False
while f is not True:
    print(f"{turn}'s turn!")
    if len(o.getPossibleMoves(turn)) == 0:
        f = True
    else:
        if turn == 'B':
            moves = o.getPossibleMoves('B')
            print("Select a Move:")
            print(moves)
            x = int(input())
            y = int(input())
            cur_mov = [x, y]
            o.setMoveB(cur_mov)
            turn = 'W'
            o.board.printBoard()
        else:
            o.takeWhiteTurn()
            turn = 'B'
            o.board.printBoard()
o.calculateScore()
