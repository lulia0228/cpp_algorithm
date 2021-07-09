#--coding:utf-8--

# 有返回值的dfs
class Solution:
    def __init__(self, *args, **kwargs):
        self.m = 0
        self.n = 0
        self.oris = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def InArea(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        ans = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    ans = max(ans, self.dfs(grid, i, j))
        return ans

    def dfs(self, grid, x, y):
        if grid[x][y] == 0: return 0
        res = 0
        # res = 1
        # 防止回头路
        grid[x][y] = 0
        for ori in self.oris:
            new_x = x + ori[0]
            new_y = y + ori[1]
            if self.InArea(new_x, new_y):
                res += self.dfs(grid, new_x, new_y)
        return res + 1
        # return res