# -*- coding: utf-8 -*-
# dp[i][j] 表示在s[i:]的子序列中t[j:]出现的个数
# 边界情况：
# 当j=n时，t[j:]为空字符串，由于空字符串是任何字符串的子序列，因此对任意0≤i≤m，有dp[i][n]=1;
# 当i=m 且 j<n 时，s[i:]为空字符串，t[j:]为非空字符串，由于非空字符串不是空字符串的子序列，因此对任意0≤j<n，有dp[m][j]=0

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    # 考虑 t[j+1:]作为 s[i+1:]的子序列和
                    # t[j:] 作为 s[i+1:]的子序列两种情况
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    # 只能考虑t[j:] 作为 s[i+1:]的子序列的情况
                    dp[i][j] = dp[i + 1][j]

        return dp[0][0]
