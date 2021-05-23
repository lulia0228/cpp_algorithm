# -*- coding: utf-8 -*-

# 此题十分有助于理解图的DFS

class Solution:
    def __init__(self):
        self.ori = [(0,1), (1,0), (0,-1), (-1,0)]

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, self.dfs(grid, i, j))
        return res

    def dfs(self, grid, x, y):
        if grid[x][y] == 0: return 0
        nxt = 0
        tmp = grid[x][y]
        grid[x][y] = 0 # 防止回头

        for ori in self.ori:
            new_x = x + ori[0]
            new_y = y + ori[1]
            if 0<=new_x<len(grid) and 0<=new_y<len(grid[0]) :
                nxt = max(nxt, self.dfs(grid, new_x, new_y))

        grid[x][y] = tmp

        return tmp + nxt
