# -*- coding: utf-8 -*-


class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.ori = [(0,1),(1,0),(0,-1),(-1,0)]

    def inArea(self, i, j):
        return i>=0 and j>=0 and i<self.m and j<self.n

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(board, 0, i, j, word):
                    return True
        return False

    def dfs(self, board, idx, i, j, word):
        # 注意是len(word)-1不是len(word)
        if idx == len(word)-1:
            return board[i][j] == word[idx]
        if board[i][j] == word[idx]:
            tmp = board[i][j]
            board[i][j] = "#"
            for d in self.ori:
                new_i = i + d[0]
                new_j = j + d[1]
                if self.inArea(new_i, new_j) and self.dfs(board, idx+1, new_i, new_j, word):
                    return True
            board[i][j] = tmp
        return False
