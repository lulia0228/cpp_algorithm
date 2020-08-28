#--coding:utf-8--
'''
@Time   : 2020/8/28
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

class Solution:
    def __init__(self, **kwargs):
        self.m = 0
        self.n = 0
        self.orient = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def inArea(self, x, y):
        return x >= 0 and x < self.m and y >= 0 and y < self.n

    def exist(self, board, word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(board, word, 0, i, j):
                    return True
        return False

    def dfs(self, board, word, idx, x, y):
        if idx == len(word) - 1:
            return board[x][y] == word[idx]
        if board[x][y] == word[idx]:
            tmp = word[idx]
            board[x][y] = '0' # 防止走回头路（即元素被重复使用）
            for i in range(4):
                new_x = x + self.orient[i][0]
                new_y = y + self.orient[i][1]
                if self.inArea(new_x, new_y) and self.dfs(board, word, idx + 1, new_x, new_y):
                    return True
            board[x][y] = tmp
        return False



# 另一种写法，可以额外设计一个数组标记是否访问
class Solution1:
    def __init__(self, **kwargs):
        self.m = 0
        self.n = 0
        self.orient = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.flag = []

    def inArea(self, x, y):
        return x >= 0 and x < self.m and y >= 0 and y < self.n

    def exist(self, board, word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        self.flag = [[False for j in range(self.n)] for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(board, word, 0, i, j):
                    return True
        return False

    def dfs(self, board, word, idx, x, y):
        if idx == len(word) - 1:
            return board[x][y] == word[idx]
        if board[x][y] == word[idx]:
            self.flag[x][y] = True
            for i in range(4):
                new_x = x + self.orient[i][0]
                new_y = y + self.orient[i][1]
                if self.inArea(new_x, new_y) and not self.flag[new_x][new_y] and \
                self.dfs(board, word, idx + 1, new_x, new_y):
                    return True
            self.flag[x][y] = False
        return False




if __name__ == "__main__":

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    res = Solution1().exist(board, word)
    print(res)