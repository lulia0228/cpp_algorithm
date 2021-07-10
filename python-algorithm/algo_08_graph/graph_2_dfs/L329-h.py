#--coding:utf-8--

from typing import *
import collections

# 1  记忆化搜索
class Solution:
    m, n = 0, 0
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        ans = 0
        self.m, self.n = len(matrix), len(matrix[0])
        memo = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                ans = max(ans, self.dfs(matrix, i, j, memo))
        return ans

    def dfs(self, matrix, row, column, memo) -> int:
        if memo[row][column] != 0:
            return memo[row][column]
        memo[row][column] = 1
        for dx, dy in self.DIRS:
            newRow, newColumn = row + dx, column + dy
            if 0 <= newRow < self.m and 0 <= newColumn < self.n and matrix[newRow][newColumn] > matrix[row][column]:
                memo[row][column] = max(memo[row][column], self.dfs(matrix, newRow, newColumn, memo) + 1)
        return memo[row][column]


class Solution:
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        @lru_cache(None)
        def dfs(row: int, column: int) -> int:
            best = 1
            for dx, dy in Solution.DIRS:
                newRow, newColumn = row + dx, column + dy
                if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[row][column]:
                    best = max(best, dfs(newRow, newColumn) + 1)
            return best

        ans = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                ans = max(ans, dfs(i, j))
        return ans


# 2 拓扑排序
'''
基于出度的概念，可以使用拓扑排序求解。从所有出度为0的单元格开始广度优先搜索，
每一轮搜索都会遍历当前层的所有单元格，更新其余单元格的出度，并将出度变为0的单元格加入下一层搜索。
当搜索结束时(队列空)，搜索的总层数即为矩阵中的最长递增路径的长度。
'''


class Solution:
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        rows, columns = len(matrix), len(matrix[0])
        outdegrees = [[0] * columns for _ in range(rows)]
        queue = collections.deque()
        for i in range(rows):
            for j in range(columns):
                for dx, dy in Solution.DIRS:
                    newRow, newColumn = i + dx, j + dy
                    if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[i][j]:
                        outdegrees[i][j] += 1
                if outdegrees[i][j] == 0:
                    queue.append((i, j))

        ans = 0
        while queue:
            ans += 1
            size = len(queue)
            print(queue)
            print(outdegrees)
            for _ in range(size):
                row, column = queue.popleft()
                print(row, column)
                for dx, dy in Solution.DIRS:
                    newRow, newColumn = row + dx, column + dy
                    if 0<=newRow<rows and 0<=newColumn<columns and matrix[newRow][newColumn]<matrix[row][
                        column]:
                        outdegrees[newRow][newColumn] -= 1
                        if outdegrees[newRow][newColumn] == 0:
                            queue.append((newRow, newColumn))

        return ans


matrix = [[9,9,4],[6,6,8],[2,1,1]]
res = Solution().longestIncreasingPath(matrix)
print(res)