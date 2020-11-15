# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.k = 0
        self.cnt = 0
        self.ori = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def inArea(self, i, j):
        return i >= 0 and j >= 0 and i < self.m and j < self.n

    def boarder(self, i, j):
        return (i % 10 + i // 10 + j % 10 + j // 10) <= self.k

    def movingCount(self, m: int, n: int, k: int) -> int:
        self.m, self.n, self.k = m, n, k
        visited = [[0] * n for i in range(m)]
        return self.dfs(0, 0, visited)
        # self.dfs1(0, 0, visited)
        # return self.cnt

    # 不使用外部变量
    def dfs(self, i, j, visited):
        cnt = 0
        if not visited[i][j]:
            visited[i][j] = 1
            cnt += 1
            for d in self.ori:
                new_i = i + d[0]
                new_j = j + d[1]
                if self.inArea(new_i, new_j) and self.boarder(new_i, new_j):
                    cnt += self.dfs(new_i, new_j, visited)
        return cnt

    # 使用外部变量
    def dfs1(self, i, j, visited):
        if not visited[i][j]:
            visited[i][j] = 1
            self.cnt += 1
            for d in self.ori:
                new_i = i + d[0]
                new_j = j + d[1]
                if self.inArea(new_i, new_j) and self.boarder(new_i, new_j):
                    self.dfs1(new_i, new_j, visited)
        return


