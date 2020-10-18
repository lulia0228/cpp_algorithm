#--coding:utf-8--


class Solution:
    def __init__(self, **kwargs):
        self.m = 0
        self.n = 0
        self.ori = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def inArea(self, x, y):
        return x >= 0 and x < self.m and y >= 0 and y < self.n

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m = len(board)
        if self.m == 0:
            return board
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if (i == 0 or j == 0 or i == self.m - 1 or j == self.n - 1) and board[i][j] == 'O':
                    self.dfs(board, i, j)
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'

    def dfs(self, board, x, y):
        if board[x][y] != 'O':
            return
        if board[x][y] == 'O':
            board[x][y] = '#' # 已经可以防止4个方向中的回头路方向了
            for i in range(4):
                new_x = x + self.ori[i][0]
                new_y = y + self.ori[i][1]
                if self.inArea(new_x, new_y):
                    self.dfs(board, new_x, new_y)




# 额外写访问数组，其实没必要
class Solution1:
    def __init__(self, **kwargs):
        self.m = 0
        self.n = 0
        self.ori = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.flag = []

    def inArea(self, x, y):
        return x >= 0 and x < self.m and y >= 0 and y < self.n

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m = len(board)
        if self.m == 0:
            return board
        self.n = len(board[0])
        self.flag = [[False for j in range(self.n)] for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if (i == 0 or j == 0 or i == self.m - 1 or j == self.n - 1) and board[i][j] == 'O':
                    self.dfs(board, i, j)
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'

    def dfs(self, board, x, y):
        if board[x][y] != 'O':
            return
        if board[x][y] == 'O':
            self.flag[x][y] = True
            board[x][y] = '#'
            for i in range(4):
                new_x = x + self.ori[i][0]
                new_y = y + self.ori[i][1]
                if self.inArea(new_x, new_y) and not self.flag[new_x][new_y]:
                    self.dfs(board, new_x, new_y)
            self.flag[x][y] = False



