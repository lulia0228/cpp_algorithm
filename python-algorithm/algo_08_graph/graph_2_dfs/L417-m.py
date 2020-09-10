#--coding:utf-8--
'''
@Time   : 2020/9/10
@Author : Heng Li
@Email  : liheng_lulia@163.com
'''


class Solution:
    def __init__(self, **kwargs):
        self.m = 0
        self.n = 0
        self.ori = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def inArea(self, x, y):
        return x >= 0 and x < self.m and y >= 0 and y < self.n

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        self.m = len(matrix)
        if self.m == 0:
            return res
        self.n = len(matrix[0])
        arrive_Pc = [[False for j in range(self.n)] for i in range(self.m)]
        arrive_Ac = [[False for j in range(self.n)] for i in range(self.m)]

        # 从边界出发，看看能到达哪些地方
        for j in range(self.n):
            self.dfs(matrix, 0, j, arrive_Pc)  # 上边界出发可达
            self.dfs(matrix, self.m - 1, j, arrive_Ac)  # 下边界出发可达
        for i in range(self.m):
            self.dfs(matrix, i, 0, arrive_Pc)  # 左边界出发可达
            self.dfs(matrix, i, self.n - 1, arrive_Ac)  # 右边界出发可达

        for i in range(self.m):
            for j in range(self.n):
                if arrive_Ac[i][j] and arrive_Pc[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, matrix, x, y, visited):
        if visited[x][y]:
            return
        visited[x][y] = True
        for i in range(len(self.ori)):
            new_x = x + self.ori[i][0]
            new_y = y + self.ori[i][1]
            if self.inArea(new_x, new_y) and matrix[new_x][new_y] >= matrix[x][y]:
                self.dfs(matrix, new_x, new_y, visited)
