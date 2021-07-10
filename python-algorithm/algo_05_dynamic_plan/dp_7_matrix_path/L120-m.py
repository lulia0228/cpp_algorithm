# -*- coding: utf-8 -*-

# 可以优化空间复杂度为2行O(n)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        lines = len(triangle)
        if lines==1:
            return triangle[0][0]
        ans = float("inf")
        dp = [[0]*(i+1) for i in range(lines)]
        dp[0][0] = triangle[0][0]
        for i in range(1,lines):
            for j in range(i+1):
                if j==0:
                    dp[i][j] = dp[i-1][j]+triangle[i][j]
                elif j==i:
                    dp[i][j] = dp[i-1][j-1]+triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j])+triangle[i][j]
                if i==lines-1:
                    ans = min(ans, dp[i][j])
        return ans
