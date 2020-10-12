#--coding:utf-8--
'''
@Time   : 2020/10/12
@Author : No Name
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # m n 别搞反了
        m, n = len(grid), len(grid[0])
        dp = [[0]*n for i in range(m)]
        dp[0][0] = grid[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1]+grid[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]