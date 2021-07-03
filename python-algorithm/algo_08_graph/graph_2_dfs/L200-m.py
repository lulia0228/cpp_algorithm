#--coding:utf-8--

# 前提:可以假设该网格的四条边均被水包围。
class Solution:
    def __init__(self, *args, **kwargs):
        self.m = 0
        self.n = 0
        self.oris = [(1,0),(-1,0),(0,1),(0,-1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        self.m = len(grid)
        self.n = len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    cnt += 1
        return cnt

    def dfs(self, grid, x, y):
        if grid[x][y] == "0":
            return
        grid[x][y] = "0"
        for ori in self.oris:
            new_x = x + ori[0]
            new_y = y + ori[1]
            if 0<=new_x<self.m and 0<=new_y<self.n:
                self.dfs(grid, new_x, new_y)



