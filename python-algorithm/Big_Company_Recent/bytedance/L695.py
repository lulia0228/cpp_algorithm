# -*- coding: utf-8 -*-
class Solution:
    def __init__(self, *args, **kwargs):
        self.m = 0
        self.n = 0
        self.ori = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def InArean(self, x, y):
        return x >= 0 and y >= 0 and x < self.m and y < self.n

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        max_area = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid, i, j))
        return max_area

    def dfs(self, grid, x, y):
        if grid[x][y] == 0:
            return 0
        cnt = 1
        grid[x][y] = 0
        for ori in self.ori:
            new_x = x + ori[0]
            new_y = y + ori[1]
            if self.InArean(new_x, new_y):
                cnt += self.dfs(grid, new_x, new_y)
        return cnt


