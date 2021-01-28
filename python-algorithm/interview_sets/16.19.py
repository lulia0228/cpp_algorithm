#--coding:utf-8--
class Solution:
    def __init__(self, *args, **kwargs):
        self.ori = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        self.m = 0
        self.n = 0

    def inArea(self, x, y):
        return x >= 0 and x < self.m and y >= 0 and y < self.n

    def pondSizes(self, land: List[List[int]]) -> List[int]:
        self.m, self.n = len(land), len(land[0])
        res = []
        for i in range(self.m):
            for j in range(self.n):
                if land[i][j] == 0:
                    res.append(self.dfs(land, i, j))
        return sorted(res)

    def dfs(self, land, x, y):
        res = 0
        if land[x][y] != 0:
            return 0
        if land[x][y] == 0:
            res += 1
            land[x][y] = 100
            for item in self.ori:
                new_x = x + item[0]
                new_y = y + item[1]
                if self.inArea(new_x, new_y):
                    res += self.dfs(land, new_x, new_y)
        return res




