# -*- coding: utf-8 -*-

# dp[i][j]表示以A[i] A[j]作为结尾的等差子序列
# 每到一个点，向前探有没有可以连接起来组队的点

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [[2 for _ in range(n)] for _ in range(n)]
        r_d = collections.defaultdict(int)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                pre = A[i] * 2 - A[j]
                if pre in r_d:
                    dp[i][j] = dp[r_d[pre]][i] + 1  #以 A[i]  A[j]为结尾的等差数组
                res = max(res, dp[i][j])
            r_d[A[i]] = i

        return res

