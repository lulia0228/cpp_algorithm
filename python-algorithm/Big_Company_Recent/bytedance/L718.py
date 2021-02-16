# -*- coding: utf-8 -*-
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        max_len = 0
        m, n = len(A), len(B)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = 0
                max_len = max(max_len, dp[i][j])
        return max_len

# 二分+hash
# 滑窗