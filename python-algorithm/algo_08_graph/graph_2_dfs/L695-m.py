#--coding:utf-8--
'''
@Time   : 2020/9/10
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''

# 有返回值的dfs递归

class Solution:

    def __init__(self, **kwargs):
        self.m = 0
        self.n = 0
        self.ori = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def inArea(self, x, y):
        return x >= 0 and x < self.m and y >= 0 and y < self.n

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        self.m = len(grid)
        if self.m == 0:
            return 0
        self.n = len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1 :
                    tmp_area = self.dfs(grid, i, j)
                    res = max(res, tmp_area)
        return res

    def dfs(self, grid, x, y):
        if grid[x][y] == 0:
            return 0
        grid[x][y] = 0 # 不走回头路
        area = 1
        for i in range(len(self.ori)):
            new_x = x + self.ori[i][0]
            new_y = y + self.ori[i][1]
            if self.inArea(new_x, new_y):
                area += self.dfs(grid, new_x, new_y)
        return area