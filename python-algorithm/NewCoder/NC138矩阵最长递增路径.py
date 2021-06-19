#--coding:utf-8--

# 暴力搜索同lc329


class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.oris = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def inArea(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n

    def solve(self, matrix):
        # write code here
        ans = 1
        self.m, self.n = len(matrix), len(matrix[0])
        for i in range(self.m):
            for j in range(self.n):
                ans = max(ans,self.dfs(matrix, i, j))
        return ans

    def dfs(self, matrix, x, y):
        best = 1
        for ori in self.oris:
            new_x = x + ori[0]
            new_y = y + ori[1]
            if self.inArea(new_x, new_y) and matrix[new_x][new_y]>matrix[x][y]:
                best = max(best,self.dfs(matrix, new_x, new_y)+1)
        return best



class Solution1:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.oris = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def inArea(self, x, y):
        return 0 <= x < self.m and 0 <= y < self.n

    def solve(self, matrix):
        # write code here

        def dfs(matrix, x, y):
            best = 1
            for ori in self.oris:
                new_x = x + ori[0]
                new_y = y + ori[1]
                if self.inArea(new_x, new_y) and matrix[new_x][new_y] > matrix[x][y]:
                    best = max(best, dfs(matrix, new_x, new_y) + 1)
            return best

        ans = 1
        self.m, self.n = len(matrix), len(matrix[0])
        for i in range(self.m):
            for j in range(self.n):
                ans = max(ans, dfs(matrix, i, j))
        return ans




mm = [[1,2,3],[4,5,6],[7,8,9]]
res = Solution1().solve(mm)
print(res)