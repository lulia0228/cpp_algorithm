#--coding:utf-8--
#
# 判断岛屿数量
# @param grid char字符型二维数组
# @return int整型
#
class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.oris = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def inArea(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n

    def solve(self, grid):
        # write code here
        self.m = len(grid)
        self.n = len(grid[0])
        cnt = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    cnt += 1
                    self.dfs(grid, i, j)
        return cnt

    def dfs(self, grid, x, y):
        if grid[x][y] == "0":
            return
        grid[x][y] = "0"
        for ori in self.oris:
            new_x = x + ori[0]
            new_y = y + ori[1]
            if self.inArea(new_x, new_y):
                self.dfs(grid, new_x, new_y)
