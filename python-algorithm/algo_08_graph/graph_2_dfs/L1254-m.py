#--coding:utf-8--

class Solution:
    def __init__(self):
        self.ori = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.m = 0
        self.n = 0

    def InArea(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n

    def closedIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        res = 0
        # 先把与边界联通的陆地填充上，剩下的0才是岛
        for i in range(self.m):
            if grid[i][0] == 0:
                self.dfs(grid, i, 0)
            if grid[i][self.n - 1] == 0:
                self.dfs(grid, i, self.n - 1)
        for j in range(self.n):
            if grid[0][j] == 0:
                self.dfs(grid, 0, j)
            if grid[self.m - 1][j] == 0:
                self.dfs(grid, self.m - 1, j)

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, x, y):
        if grid[x][y] == 1:
            return
        grid[x][y] = 1
        for ori in self.ori:
            new_x = x + ori[0]
            new_y = y + ori[1]
            if self.InArea(new_x, new_y):
                self.dfs(grid, new_x, new_y)


