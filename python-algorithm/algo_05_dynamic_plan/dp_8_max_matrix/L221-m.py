#--coding:utf-8--


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        # dp[i][j]表示以matrix[i-1][j-1]作为右下角的正方的边长
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1])+1
                    res = max(res, dp[i][j])
        return res*res


