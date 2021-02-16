# -*- coding: utf-8 -*-

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    self.dfs(grid, i, j)
        return cnt

    def dfs(self, grid, x, y):
        if grid[x][y] == "0": return
        grid[x][y] = "0"
        for i in [(1,0), (0,-1),(-1,0),(0,1)]:
            new_x = x + i[0]
            new_y = y + i[1]
            if 0<=new_x<len(grid) and 0<=new_y<len(grid[0]) :
                self.dfs(grid, new_x, new_y)